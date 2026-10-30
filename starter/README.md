# Rótulo Claro — ponto de partida comum

Este repositório não contém uma implementação. Implemente o produto usando o prompt recebido, `BENCH_CONFIG.json` e o contrato em `contracts/`.

`fixtures/dev` contém imagens sintéticas de desenvolvimento. O comportamento deve generalizar para imagens arbitrárias. Não consulte pastas externas ou outras execuções do experimento. Nenhuma imagem foi criada como rótulo regulatório ou recomendação alimentar.

A chave da IA de visão pertence ao ambiente do backend, por `VISION_API_KEY`. O nome do modelo será `VISION_MODEL` ou o valor congelado em `BENCH_CONFIG.json`. Não leia chaves de outras contas nem suponha que login do agente dá acesso à API.

Contrato de avaliação: `POST /api/extract`, upload multipart no campo `image`, retorna o corpo JSON definido no schema. Extração bruta deve ficar separada da revisão humana. O contrato não exige que a API de histórico use formato específico.
