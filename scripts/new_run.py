"""Cria projeto independente; jamais copia evaluator ou conversa original."""
import argparse
import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def tree_hash(folder):
    digest = hashlib.sha256()
    for file in sorted(p for p in folder.rglob("*") if p.is_file() and ".git" not in p.parts):
        digest.update(file.relative_to(folder).as_posix().encode())
        digest.update(b"\0")
        digest.update(file.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True)
    parser.add_argument("--tool", required=True, choices=["baseline", "orca", "paseo", "maestri", "thinkrail", "pi-baseline", "superset", "conductor", "overclock"])
    parser.add_argument("--config", type=Path, default=ROOT / "config.template.json")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]{2,79}", args.id):
        parser.error("ID deve ter 3-80 caracteres: letras minusculas, numeros, _ ou -")
    git = shutil.which("git")
    if not git:
        parser.error("Git nao encontrado; instale/configure antes de criar uma execucao")
    config = json.loads(args.config.read_text(encoding="utf-8-sig"))
    config_text = json.dumps(config)
    pending = "PREENCHER" in config_text or not all([
        config.get("vision", {}).get("real_access_verified"),
        config.get("limits", {}).get("budget_accepted"),
        config.get("dependency_lockfile_frozen")])
    target = ROOT / "runs" / args.id
    if target.exists():
        parser.error("ID ja existe; nenhum arquivo foi sobrescrito")
    target.mkdir(parents=True)
    project = target / "project"
    shutil.copytree(ROOT / "starter", project)
    (project / "BENCH_CONFIG.json").write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    shutil.copytree(ROOT / "prompts", target / "prompts")
    shutil.copyfile(ROOT / "FORMULARIO.md", target / "FORMULARIO.md")
    manifest = {"id": args.id, "tool": args.tool, "created_utc": datetime.now(timezone.utc).isoformat(),
                "status": "preparacao_pendente" if pending else "pronto_para_piloto",
                "config": config, "starter_sha256": tree_hash(project),
                "prompt_sha256": {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in (target / "prompts").glob("*.md")},
                "notes": "Abrir somente project no agente. Gabaritos permanecem fora deste diretorio."}
    subprocess.run([git, "init", "--quiet", str(project)], check=True)
    # Identidade apenas deste commit; nao altera configuracao global do usuario.
    subprocess.run([git, "-C", str(project), "add", "."], check=True)
    subprocess.run([git, "-C", str(project), "-c", "user.name=ADE Benchmark", "-c", "user.email=benchmark@localhost",
                    "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", "Common benchmark starting point"], check=True)
    manifest["initial_commit"] = subprocess.check_output([git, "-C", str(project), "rev-parse", "HEAD"], text=True).strip()
    (target / "run.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Criado: {project}\nEstado: {manifest['status']}\nSHA256: {manifest['starter_sha256']}")
    if pending:
        print("Nao iniciar rodada oficial: complete a configuracao. Esta copia serve para preparar/pilotar.")


if __name__ == "__main__":
    main()
