# Comece aqui - Experimento ADE

**Abra GUIA-VISUAL.pdf.** Ele mostra o roteiro em seis páginas; os prompts ficam separados nesta pasta.

1. Combine agente/modelo, visão e limites com o organizador. Preencha `config.template.json`, sem chaves.
2. Instale Orca, Paseo e ThinkRail pelos links do guia. Maestri, Conductor e Superset são opcionais.
3. No terminal desta pasta, execute `python scripts/preflight.py` e crie uma execução por ferramenta com `scripts/new_run.py`.
4. Abra somente `runs/ID/project` no ADE. Anexe `prompts/01-implementar.md` e peça para executar no projeto atual.
5. Avalie e preserve a entrega. Na mesma conversa, envie `02-evoluir.md`; pelo telefone, quando suportado, use `03-mobile.md`.

## Os arquivos de prompt

O mapa está em [PROMPTS.md](PROMPTS.md). Se o chat não aceitar anexos, abra o `.md` e copie o conteúdo inteiro.
Não envie todos os arquivos de uma vez. `06-continuidade.md` e `08-handoff.md` são roteiros do operador: envie apenas a mensagem da etapa/destinatário indicado. Os arquivos `07a`, `07b` e `07c` pertencem a tarefas diferentes.

## Onde registrar

Preencha [FORMULARIO.md](FORMULARIO.md) por execução. Os critérios detalhados ficam em [PROTOCOLO.md](PROTOCOLO.md), para consultar quando necessário.

Reserva proposta: até 2h25 por ferramenta, incluindo setup, implementação, evolução, mobile e revisão. Pode dividir em dias. Combine limites de gasto antes de executar; assinatura do agente não garante acesso à IA de visão.

O kit contém apenas quatro imagens públicas sintéticas. Gabaritos e lote reservado ficam com o organizador. Nunca envie `.env`, chaves ou dados pessoais na devolutiva.
