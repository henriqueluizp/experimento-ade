"""Inspecao local somente leitura, sem rede, sem ler segredos."""
import json
import platform
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inspect():
    result = {"timestamp_utc": datetime.now(timezone.utc).isoformat(),
              "os": platform.platform(), "machine": platform.machine(), "tools": {}}
    for name in ("node", "npm", "git", "python", "docker", "claude", "codex"):
        executable = shutil.which("npm.cmd" if name == "npm" and platform.system() == "Windows" else name)
        item = {"found": bool(executable), "path": executable}
        # Nao iniciar agentes nem Docker, nem sondar suas contas.
        if executable and name in ("node", "npm", "git", "python"):
            try:
                proc = subprocess.run([executable, "--version"], capture_output=True, text=True, timeout=10)
                item["version"] = proc.stdout.strip() or proc.stderr.strip()
                item["exit_code"] = proc.returncode
            except (OSError, subprocess.SubprocessError) as exc:
                item["error"] = type(exc).__name__
        result["tools"][name] = item
    result["manual_pending"] = ["Fixar ADE/CLI/modelos e permissoes", "Validar login/saldo sem registrar segredo",
                                "Configurar visao real e teto de custo", "Fixar lockfile comum",
                                "Coletar corpus real", "Testar HTTPS/camera e acesso remoto no telefone"]
    return result


if __name__ == "__main__":
    report = inspect()
    target = ROOT / "environment-check.json"
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print(f"Registro salvo em {target}")
