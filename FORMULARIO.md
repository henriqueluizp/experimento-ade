# Ficha por execução — copiar antes de preencher

## Identificação e controle

- ID anônimo / ID operacional:
- Pessoa / host / SO / hardware / rede:
- Data e modalidade (controlada ou otimizada):
- ADE e versão/commit:
- Agente / versão / modelo / esforço:
- Visão: provedor / ID de modelo / parâmetros:
- Instruções, MCPs, skills, hooks e permissões extras:
- Hash starter / hashes prompts / commit inicial / commit após evolução:
- Orçamentos definidos / limites efetivamente monitorados:
- Cache de dependências / respostas de visão:
- Desvios do protocolo e tarefas não executadas:

## Tempos e recursos

| Fase | Tempo decorrido | Minutos humanos ativos | Intervenções | Tokens/gasto | Evidências |
|---|---:|---:|---:|---|---|
| Setup do ADE | | | | | |
| Inicial | | | | | |
| Evolução | | | | | |
| Mobile Wi-Fi | | | | | |
| Mobile rede móvel | | | | | |
| Recuperação separada | | | | | |

## Nota da ferramenta

| Pilar | Peso | Nota 0–10 | Subitens/evidência/origem do recurso |
|---|---:|---:|---|
| A. Isolamento/Git | 20 | | |
| B. UX/ergonomia cognitiva | 25 | | |
| C. Flexibilidade/custo operacional | 15 | | |
| D. Revisão/integrações | 20 | | |
| E. Continuidade/contexto | 20 | | |

Nota desktop = soma(peso × nota) / 100. Usar subitens básicos A1–A4, B1–B5, C1–C4, D1–D3 e E1–E4 de PROTOCOLO.md; módulos extras são separados. Não fechar pilar com subitem obrigatório não testado.

## Produto

Anexar roteiro dos 12 passos iniciais, 10 cenários de robustez, 6 requisitos da evolução e reexecução dos 12 passos após a evolução. Para cada item: aprovado/reprovado/não executado, versão/commit e evidência.

| Dimensão | Peso | Inicial | Após evolução | Evidência |
|---|---:|---:|---:|---|
| Funcionalidade | 25 | | | |
| Extração | 25 | | | |
| UX/visual/acessibilidade | 20 | | | |
| Robustez | 15 | | | |
| Evolução sem regressão | 10 | não aplicável | | |
| Reprodutibilidade | 5 | | | |

- Nota inicial renormalizada sobre 90%:
- Nota final:
- Bloqueadores e resultado aprovado/não aprovado:
- Precisão / cobertura / F1 / erros de unidade / coluna / preenchimento indevido:
- Corpus sintético / fotos reais / quantidade e repetições:
- Latência mediana e p95 / tamanho da amostra:
- Chamada real de visão verificada? Como?

## Mobile do ADE — Wi-Fi e rede móvel separadamente

Pontuar 0/5/10 os oito itens da seção 9: pareamento/retorno, estado em até 5 s, alertas úteis, intervenção, envio de tarefa, revisão, interrupção/retomada e reconexão. Nota = média dos oito itens. Registrar origem nativa/CLI/SO de cada função.

- Tempo para identificar estado/próxima ação:
- Toques e segundos até aprovar/negar, a partir do alerta:
- Notificações úteis / total / irrelevantes por 10 min / eventos importantes não avisados:
- Texto enviado / áudio enviado / transcrição nativa ou teclado do SO / falhas:
- Wi-Fi / rede móvel / aparelho / permissões do SO:

## Continuidade, contexto e concorrência

| Teste | Resultado | Evidência | Origem: ADE/CLI/modelo/SO/indeterminada |
|---|---|---|---|
| Evolução na mesma conversa | | | |
| Evolução em sessão nova sobre cópia do mesmo commit | | | |
| Referências nos turnos 2/3/10 | | | |
| Reabrir cliente/alternar workspace | | | |
| Reboot opcional: histórico/processo/contexto separados | | | |
| Contexto exposto: tokens/%/limite/cache | | | |
| Resumo/compactação: regras preservadas antes/depois | | | |
| Troca de agente: transcript/resumo/arquivo/Git | | | |
| Arquivos efetivamente lidos e consumo observado | | | |
| Isolamento sequencial e conflito preparado | | | |
| Concorrência real opcional e limites compartilhados | | | |
| PR/CI/issues opcionais: nativo/plugin/CLI/não testado | | | |

- Esforço mental percebido (0 = nenhum, 10 = extremo), por bloco:
- Segundos para retomar foco / erros / cliques / trocas de aplicativo:
- Três regras-alvo preservadas após resumo (0–3), com evidência:
- Repetições de informações exigidas no handoff:
- Limitações de medição: dado não exposto, recurso ausente ou teste não executado:

## Parecer humano antes da discussão

- Eu adotaria no dia a dia? Para qual tarefa?
- Maior atrito:
- Melhor ganho observado:
- Esforço para migrar meu fluxo atual:
- Limitações ou evidências faltantes:
- Parecer da outra IA e pontos de discordância:
