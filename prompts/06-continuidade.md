# Roteiro do operador — dez turnos na mesma conversa

Módulo adicional para os finalistas, em cópia descartável do produto pronto. Reserve até 25 minutos e teto de gasto próprio. Envie **um bloco por vez**, espere concluir, registre evidências e só então envie o próximo. Não cole este arquivo inteiro no agente. Não use o histórico de outra ferramenta. Se o requisito anterior não estiver implementado, registre a falha e evite dicas particulares para resgatar somente um candidato.

O avaliador registra três regras-alvo: extração original imutável; não converter massa em volume sem densidade; não salvar extração sem confirmação humana. Registre também se o agente persistiu essas regras espontaneamente em arquivo: isso é um mecanismo de continuidade válido, mas diferente de retenção só pelo chat.

## Turno 1 — referência inicial

```text
Vamos continuar o Rótulo Claro nesta mesma conversa. Mantenha três regras durante toda esta sequência: preservar a extração original; não converter g em ml ou ml em g sem densidade explícita; não salvar automaticamente sem confirmação humana. Adicione um selo visual que distinga a leitura ainda não confirmada da leitura revisada. Integre-o ao fluxo existente sem criar uma segunda fonte de verdade para o estado. Use texto e cor, com contraste legível, e verifique a mudança. Respeite BENCH_CONFIG.json.
```

## Turno 2 — referência à mudança anterior

```text
Naquele selo que acabamos de criar, deixe o estado pendente em azul. Preserve o significado dos estados e a legibilidade. Verifique que você alterou o componente certo sem mudar a lógica de salvamento.
```

## Turno 3 — decisão a preservar até o turno 10

```text
Agora use exatamente os textos “Aguardando sua revisão” e “Revisado por você” naquele mesmo selo. Não renomeie os estados internos só para trocar os textos. Verifique e mostre o trecho alterado.
```

Após o turno 3: feche/reabra o cliente, alterne de workspace e volte. Não encerre processos de outras tarefas nem reinicie o computador. Registre histórico visível, estado do agente e arquivo atual separadamente.

## Turno 4 — recuperação após reabrir

```text
Antes de alterar qualquer coisa, diga quais textos escolhemos para os dois estados do selo e quais três regras de negócio estamos preservando. Confira a implementação e aponte qualquer divergência. Não mude arquivos neste turno.
```

## Turno 5 — continuidade funcional

```text
Verifique o comportamento daquele selo quando o usuário edita um valor e ainda não confirma a revisão. Se houver inconsistência, corrija preservando o fluxo de confirmação e os dados originais. Faça uma verificação focada e relate o resultado.
```

## Turno 6 — controle antes do resumo

```text
Sem modificar arquivos, resuma o que já concluímos nesta sequência, os textos finais do selo, as três regras de negócio e qualquer falha ainda aberta. Distinga o que verificou do que apenas supõe.
```

## Passo do operador antes do turno 7

Registre consumo e origem da métrica, quando disponíveis. Observe uma compactação natural ou use apenas o mecanismo documentado do agente/ADE. Preserve a sessão. Se indisponível, registre “compactação não suportada/não observada” e prossiga sem alegar que testou retenção após compactação. Não substitua por nova sessão sem identificar a mudança de procedimento. Não envie de novo as regras como ajuda.

## Turno 7 — retenção após resumo

```text
Retome a sequência: quais são os textos finais daquele selo e as três regras que continuamos obrigados a preservar? Confira os arquivos relevantes e identifique a próxima verificação útil. Não implemente funcionalidade nova neste turno.
```

## Turno 8 — erro sem perda do estado

```text
Verifique se uma falha de rede durante uma nova análise pode apagar dados já revisados ou apresentar a leitura como confirmada indevidamente. Use uma falha simulada identificada, sem chamada paga. Corrija somente se necessário e preserve as decisões anteriores.
```

## Turno 9 — inspeção do trabalho acumulado

```text
Mostre o resumo do diff desta sequência e aponte mudanças que possam afetar captura, extração original, salvamento e histórico. Apenas inspecione; não edite nem reverta nada neste turno.
```

## Turno 10 — referência distante

```text
Volte àquele selo do início. Confirme que a cor e os dois textos que decidimos ainda estão corretos nos layouts mobile e desktop, e que a revisão continua explícita. Corrija apenas divergências comprovadas. Não refaça o componente nem amplie o escopo. Relate as três regras preservadas e a evidência dos testes.
```

## Correção do roteiro

Nos turnos 2/3/10: registrar referência resolvida, decisão preservada, mudança correta e informação repetida pelo operador. No turno 4: verificar retorno após reabrir. No turno 7: comparar as três regras com o controle do turno 6 e identificar se houve consulta de arquivo/histórico/resumo. No turno 10: textos exatos do turno 3, pendência azul e nenhuma regressão nas três regras. Qualidade de código fica na ficha do produto; clareza de retomada e retenção observada, no pilar E. Registre resultado do modelo/harness e apresentação do ADE separadamente.
