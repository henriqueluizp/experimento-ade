# Roteiro do operador — troca de agente

Módulo opcional em cópia descartável, com até 10 minutos e teto adicional previamente definido. O agente B pode ser diferente de A; registrar ambos, sem misturar os resultados com o teste controlado de um único agente. Enviar cada bloco somente ao destinatário indicado.

## Agente A

```text
Prepare um handoff deste projeto para outro agente. Inspecione o estado atual e escreva HANDOFF.md com objetivo, branch/commit, comandos para rodar, arquivos relevantes, decisões e regras de negócio, testes executados, limitações e exatamente uma próxima tarefa: revisar a preservação da extração original e a exigência de confirmação humana antes de salvar. Não altere o código do aplicativo neste turno. Não inclua segredos, dados pessoais ou afirmações de testes que não executou. Identifique trabalho não commitado sem descartá-lo.
```

## Ação do operador

Registre se o ADE oferece transferência nativa do histórico e se é possível verificar o que o agente B receberá. Abra B sobre o mesmo estado de arquivos, sem rodar A simultaneamente. Mesmo com transferência nativa, mantenha `HANDOFF.md` como evidência comum. Não diga que B recebeu transcript se só puder observar a conversa na interface.

## Agente B

```text
Continue o projeto a partir de HANDOFF.md e do estado real do repositório. Confirme branch e arquivos antes de editar. Execute a próxima tarefa registrada no handoff, verificando as decisões e sem presumir que o relato de A é prova de funcionamento. Corrija somente uma falha reproduzível, se houver. Preserve extração original, revisões e demais funcionalidades. Entregue evidência do que verificou e diga qual informação faltou; não amplie o escopo nem faça chamadas pagas desnecessárias.
```

## Medir

Tempo até a primeira ação útil; informações repetidas pelo operador; regras preservadas; divergências entre handoff e repositório; presença/ausência de transcript recebido; conclusão da tarefa. Separar falha da passagem de informação de falha de raciocínio do segundo agente.
