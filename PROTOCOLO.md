# Protocolo do participante - v1.2

## 6. Critérios para avaliar a ferramenta — cinco pilares

Notas de 0 a 10 com evidência. Âncoras: 0 = impossível ou perde trabalho; 2 = bloqueios frequentes; 5 = conclui com ajuda ou atrito considerável; 8 = conclui com pequeno atrito; 10 = conclui com clareza, pouco esforço e recuperação verificada. Para cada pilar dê nota a cada subitem previsto e use a média simples; não premie quantidade de recursos sem executar as tarefas.

| Pilar | Peso | Subitens e evidências |
|---|---:|---|
| A. Isolamento e Git | 20% | Criar ambiente/branch isolado; identificar diretório e branch de cada tarefa; preservar alterações de outra tarefa; visualizar e resolver conflito preparado sem perda de trabalho |
| B. UX e ergonomia cognitiva | 25% | Encontrar estado/próxima ação; distinguir concluído, aguardando e erro; reduzir/ocultar ruído; retomar foco após interrupção; esforço em cliques/trocas de tela e avaliação pessoal de carga |
| C. Flexibilidade e custo operacional | 15% | Configurar o agente escolhido; verificar o que pode trocar/exportar; medir setup; identificar consumo/custos e restrições de licença/plano |
| D. Revisão e integrações | 20% | Ler diff; comentar trecho e encaminhar correção; revisar resultado e desfazer seletivamente; verificar fluxo PR/CI quando habilitado |
| E. Continuidade e contexto | 20% | Referências nos turnos 2/3/10; persistência após reabrir; retomada em sessão nova; preservar regras após resumo/compactação; entender origem/limites da indicação de contexto |

Nota ADE desktop = soma(nota do pilar × peso) / 100. Esta tabela substitui os oito critérios da v1.0, sem somar as notas antigas novamente. Tempos, esforço, intervenções e custos continuam publicados como medidas brutas. Não inclua estética do aplicativo na nota do ADE. Mobile recebe nota própria, na seção 9.

Todos fazem os testes básicos A1–A4, B1–B5, C1–C4, D1–D3 e E1–E4 da seção 12. Para subitem exigido e sem suporte, registre 0; falta de medição é “não testado” e impede fechar aquele pilar. Integração PR/CI (D4), troca de agente (E5) e orquestração simultânea são módulos adicionais: ficam fora da média básica, salvo se vocês os tornarem obrigatórios para todos antes da rodada. A ausência desses módulos não transforma a rodada de um agente em nota zero.

Licença, preço e abertura são fatos do inventário, não escalas morais. Um produto gratuito não recebe automaticamente 10, e um pago não recebe automaticamente 0. Em C4 avalie se custo, direitos de uso, plano necessário, dependências e limites podem ser identificados e se cabem no orçamento pré-definido. Se código aberto for requisito eliminatório de vocês, aplique esse filtro antes de comparar usabilidade, separando candidatos com licença não confirmada.


## 9. Mobile: dois testes distintos

**Aplicativo nutricional:** usar câmera, revisar e salvar no navegador do telefone. Faz parte da nota de produto.

**ADE no telefone:** use `03-mobile.md` como tarefa comum e execute os oito itens abaixo. Para cada item: 0 = não conclui; 5 = conclui com atrito, atraso relevante ou ajuda; 10 = conclui sem ajuda e cumpre o alvo proposto. Registre tempo, toques e observações; esses alvos são critérios experimentais, não padrões clínicos.

| Item | Alvo observável para 10 pontos |
|---|---|
| Pareamento e retorno | Parear e depois voltar à sessão correta sem auxílio no desktop |
| Estado imediato | Identificar tarefa, estado e próxima ação em até 5 segundos após abrir a tela |
| Alertas úteis | Nos eventos concluído, aguardando permissão e erro, distinguir o evento; nenhum alerta de cada linha de log com configurações equivalentes |
| Intervenção | Aprovar e negar ações previstas sem digitar comando; registrar quantidade de toques a partir do alerta, sem exigir um toque quando isso eliminaria a leitura da ação |
| Enviar tarefa | Enviar texto e verificar recebimento na tarefa correta; áudio/transcrição é subteste opcional com origem nativa ou teclado do SO registrada |
| Revisar | Localizar arquivo/trecho alterado e enviar comentário com contexto suficiente |
| Interromper/retomar | Parar uma execução e retomar sem duplicar a tarefa ou perder alterações |
| Reconectar | Após 60 s sem rede, recuperar a sessão sem reenviar a tarefa concluída |

Nota mobile = média dos oito itens. Substitui o cálculo binário da v1.0; não some a antiga nota. Reporte separado: latência das notificações, alertas úteis/total, notificações irrelevantes/10 min e eventos importantes não avisados. Se notificações estiverem bloqueadas pelo SO, registre o impedimento e repita após configurar; não presuma falha do ADE. Se não houver acesso remoto utilizável, marque “não suportado” e 0 na recomendação mobile, sem reduzir a nota desktop.

Repita uma vez no Wi-Fi e uma vez na rede móvel quando houver acesso seguro configurado. Maestri Remote documenta beta público iOS e beta fechado Android; acesso pode exigir preparação. Não atribua ao produto capacidades anunciadas mas inacessíveis no dia. No ThinkRail, interface no navegador não comprova boa usabilidade no celular: medir no aparelho é requisito.


## 12. Roteiros novos: o que executar e a quem atribuir o resultado

### A. Isolamento e conflitos reproduzíveis

**A1:** criar uma tarefa pelo fluxo normal da ferramenta e registrar se branch/worktree é automático, opcional ou manual. **A2:** criar outra tarefa em ambiente separado, sequencialmente na modalidade controlada; registrar diretório, branch e status das duas. **A3:** editar um arquivo no primeiro ambiente e verificar no segundo que a alteração não apareceu. **A4:** sobre clone descartável, preparar duas branches divergentes usando `lab/conflito-base/settings.json` e os prompts `07a`, `07b`, `07c`; avaliar visualização do conflito, encaminhamento da decisão e preservação das mudanças não conflitantes.

No modo controlado execute os dois agentes sequencialmente, um por vez. No modo otimizado repita o laboratório com dois agentes realmente simultâneos e teto total compartilhado. Somente o segundo mede concorrência real. Uma ferramenta que usa diretórios isolados por outro mecanismo pode preservar trabalho; registre esse sucesso e registre separadamente a ausência de worktrees automáticos. Resolver conflito pelo terminal é conclusão com esforço manual, não evidência de recurso visual nativo.

Use só o clone do laboratório; não introduza conflito artificial na entrega nutricional avaliada. Não faça push, merge remoto ou descarte de alterações. O roteiro completo está em `lab/ROTEIRO.md`.

### B. Ergonomia cognitiva e notificações

**B1:** após 60 s olhando outra tela, voltar e apontar tarefa ativa, branch, estado e próxima ação. Medir segundos e erros, com alvo de até 5 s para localização inicial. **B2:** apresentar três estados: concluído, esperando permissão e erro técnico; registrar se os diferencia sem abrir uma sequência de logs. **B3:** durante 10 min padronizados de atividade, contar notificações úteis, redundantes e irrelevantes; anotar se é possível silenciar progresso sem silenciar bloqueios. **B4:** ocultar logs/painéis secundários e depois reencontrar erro/diff; medir passos. **B5:** registrar cliques, trocas de aplicativo, retornos à aba errada e nota pessoal de esforço mental 0–10 após cada bloco, usando a mesma pergunta.

Pergunta comum: “Quanto esforço mental foi necessário para saber o que estava acontecendo e o que fazer em seguida?” 0 = nenhum, 10 = extremo. Essa medida subjetiva é útil e deve ficar identificada como tal; não a apresente como diagnóstico, escala validada ou conclusão sobre todas as pessoas com TDAH. Não infira neurodivergência do participante. Compare cada pessoa com seu próprio baseline; registre brilho, resolução, tema e preferência de notificações para tornar a comparação interpretável.

Para testar pedido de permissão sem depender de um acaso, use em cópia descartável uma ação local inofensiva configurada para exigir confirmação pelo mecanismo documentado da ferramenta. Emita a ação, negue, repita e aprove. Não enfraqueça a segurança para ganhar velocidade. A avaliação verifica se a negação é respeitada, se a ação é compreensível e se a tarefa se recupera. Grave a origem do alerta: ADE, agente, terminal ou sistema operacional.

### C. BYOA, configuração e custo

**C1:** iniciar o mesmo CLI/modelo escolhido para a rodada e verificar a configuração efetiva. **C2:** inventariar agentes suportados nativamente, como comando genérico ou apenas via integração externa; instalar todos não é necessário. Validar um segundo agente, quando disponível, em tarefa pequena separada, sem substituir silenciosamente o agente do teste controlado. **C3:** medir minutos e etapas manuais de setup, abertura do projeto e exportação/execução sem a interface. **C4:** registrar licença, plano/recursos necessários, custo fixo, custo de programação, custo de visão e eventual infraestrutura remota; custos desconhecidos ficam desconhecidos.

Não usar como fatos as listas de agentes, preços em dólares ou existência de apps contidos no rascunho enviado: são hipóteses até consultar documentação e validar na versão testada. T3 Code é apenas exemplo no rascunho e não foi acrescentado à matriz. Inclusão de novos candidatos fica fora desta revisão para manter o experimento viável.

### D. Review e integração externa

**D1:** localizar uma alteração e comparar antes/depois sem depender de uma mensagem resumida do agente. **D2:** selecionar um trecho e pedir uma correção específica; registrar se existe comentário inline nativo, anotação com arquivo/linha ou somente mensagem textual. **D3:** conferir o novo diff e desfazer somente a alteração escolhida, preservando outra mudança intencional. Use clone descartável e valide arquivos depois da ação.

**D4, opcional:** em repositório de teste previamente autorizado, verificar vínculo com issue, abertura de PR, comentário de review e leitura de CI passando/falhando. Identifique nativo, MCP/plugin, CLI ou navegador externo. GitHub, Linear e CI são capacidades distintas: não exigir conta Linear para aprovar review local. Não crie issues, PRs, comentários ou mensagens em contas reais só para medir uma integração sem autorização específica. Sem acesso, registre “não testado” neste módulo, sem fingir evidência a partir do marketing.

### E. Continuidade, troca de agente e economia de contexto

**E1:** usar o mesmo chat para implementação e evolução; depois, no laboratório de finalistas, enviar os dez turnos de `06-continuidade.md` sequencialmente. Registrar se nos turnos 2/3/10 o agente resolve referências anteriores, mantém decisões e preserva dados sem pedir repetição. **E2:** após o turno 3, fechar e reabrir somente o cliente e alternar de workspace; registrar separadamente histórico visível, processo ainda ativo e regras ainda lembradas. Reinício de computador é subteste opcional numa janela sem outras tarefas: preservar histórico não significa manter um processo vivo durante reboot. **E3:** em cópia do commit inicial, abrir sessão nova e enviar `02-evoluir.md` sem transcript; medir quanto precisa reconstruir a partir dos arquivos. **E4:** inspecionar indicação de uso do contexto, origem da informação, seleção de arquivos e resultado após resumo/compactação, quando disponível.

No E4 registre tokens de entrada/saída, cache, custo, limite e percentual somente quando expostos. “Não exposto” não é 0 tokens nem prova de má gestão. Não estime percentual exato a partir do tamanho do chat. Compactação costuma envolver o agente/harness/provedor; só atribua ao ADE se houver evidência de que ele a executou ou alterou. Um indicador nativo não recebe crédito por “economizar tokens” sem medição de custo e retenção das regras.

Para medir retenção, use o turno 7 do roteiro: registre as três regras-alvo antes de resumir; depois do resumo e de uma tarefa pequena, verifique regras, resultado e eventuais pedidos para repetir. Observe uma compactação natural ou acione apenas o mecanismo documentado da versão instalada. Se não houver, marque o subteste como não suportado e faça separadamente o handoff explícito por arquivo; não chame esse handoff de compactação automática. Não encha o contexto com texto inútil para provocar limite, nem queime orçamento para obter um percentual.

Para seleção de arquivos, inclua no clone do laboratório apenas arquivos fictícios grandes e sem segredo, idênticos para todos, se desejarem esse subteste. Registre arquivos/bytes efetivamente lidos pelo log e impacto nos tokens quando observável. Repositório grande não implica injeção integral; uma busca pode apenas listar nomes. Não afirme que a interface leu tudo ou restringiu contexto sem evidência. A métrica de economia só vale com tarefa e resultado equivalentes.

**E5, opcional:** em clone descartável, pedir ao agente A um handoff conforme `08-handoff.md`; abrir outra sessão com agente B e continuar usando o mesmo arquivo e commit. Registrar se houve transferência nativa de transcript, resumo explícito ou somente estado Git. Acesso ao histórico da interface não garante que o segundo modelo o recebeu. Medir regras preservadas, tempo até primeira ação útil e quantas informações precisaram ser repetidas. Essa etapa sai da modalidade controlada de um único agente e é publicada como integração entre agentes.

### Separar autoria do mecanismo e qualidade da experiência

Para cada medição registre **quem fornece** o recurso (ADE, CLI/harness, modelo/provedor, SO ou integração) e **como o ADE o apresenta**. São duas perguntas diferentes. Falha em retenção de uma regra pode vir do modelo, enquanto ocultar uma permissão pendente é problema de apresentação; quando não puder determinar a origem, registre “indeterminada”.

O baseline executa as mesmas tarefas com os mecanismos que realmente possui. Não lhe atribua revisão visual, compactação ou notificação de um plugin não instalado. Na modalidade otimizada, inventarie todos os complementos e o tempo de configuração. Evite contar o mesmo benefício duas vezes: ergonomia no pilar B; retenção no E; integridade do código no A/D; qualidade do aplicativo na nota produto.

