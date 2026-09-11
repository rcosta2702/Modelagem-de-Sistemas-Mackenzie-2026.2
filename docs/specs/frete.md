RF-01: WHEN o usuário calcular o frete e o carrinho atingir o limite regional, THE SYSTEM SHALL zerar o frete

RB-01: WHILE a região for 'Norte', o limite é R$300,00. Demais regiôes: R$ 200,00.

RB-02: IF valor <= 0, THEN exibir erro 'Valor de carrinho inválido'.

RF-02: WHEN o usuário informar o CEP de destino, THE SYSTEM SHALL identificar a região correspondente.

RF-03: WHEN o carrinho não atingir o limite de frete grátis, THE SYSTEM SHALL calcular e exibir o valor do frete.

RB-03: IF o CEP informado for inválido ou não atendido, THEN exibir a mensagem "CEP inválido ou região não atendida".