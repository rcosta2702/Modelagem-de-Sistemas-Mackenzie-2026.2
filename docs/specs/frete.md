# Especificação: Sistema de Cálculo de Frete

## Requisitos Funcionais

- **RF-01 (Event-Driven):** WHEN o usuário calcular o frete e o carrinho atingir o limite regional, THE SYSTEM SHALL zerar o valor do frete.

- **RF-02 (Event-Driven):** WHEN o usuário informar o CEP de destino, THE SYSTEM SHALL identificar a região correspondente.

- **RF-03 (Event-Driven):** WHEN o carrinho não atingir o limite de frete grátis, THE SYSTEM SHALL calcular e exibir o valor do frete.


## Regras de Negócio e Exceções

- **RB-01 (State-Driven):** WHILE a região selecionada for "Norte", THE SYSTEM SHALL considerar R$ 300,00 como valor limite para frete grátis. Para as demais regiões, THE SYSTEM SHALL considerar R$ 200,00 como valor limite.

- **RB-02 (Unwanted Behavior):** IF o valor total do carrinho for menor ou igual a R$ 0,00, THEN THE SYSTEM SHALL rejeitar a operação e exibir a mensagem de erro "Valor do carrinho inválido".

- **RB-03 (Unwanted Behavior):** IF o CEP informado for inválido ou não for atendido pelo sistema, THEN THE SYSTEM SHALL rejeitar o cálculo e exibir a mensagem "CEP inválido ou região não atendida".
