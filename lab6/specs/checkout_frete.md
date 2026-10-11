# Checkout e frete - especificação EARS

## Versão 2 - Exercício 3

- **REQ-01 (Ubiquitous):** THE SYSTEM SHALL calcular o total adicionando a taxa padrão de R$ 15,00 ao subtotal do carrinho, salvo a isenção de REQ-02.
- **REQ-02 (IF/THEN):** IF o subtotal for maior ou igual a R$ 250,00, THEN THE SYSTEM SHALL conceder frete grátis (R$ 0,00).

Histórico: o exercício 1 usava R$ 200,00. No exercício 3, a especificação foi atualizada primeiro para R$ 250,00; depois foram alterados os testes e, por último, o código. A versão anterior está em evidence/spec-v1.md.
- **REQ-03 (Unwanted behavior, decisão explícita de domínio):** IF o subtotal não for um número finito estritamente positivo, ou tiver fração de centavo, THEN THE SYSTEM SHALL rejeitar o cálculo com ValueError e mensagem "Valor do carrinho inválido".

## Contrato

`calcular_frete(subtotal)` retorna somente a taxa; `calcular_total(subtotal)` retorna subtotal mais taxa. Ambas retornam Decimal. Aceitar int, float, str decimal e Decimal; rejeitar booleanos e outros tipos. Valores devem ter no máximo duas casas decimais significativas. Não arredondar silenciosamente.

## Escopo e divergências do material

Os slides 7 e 13 definem REQ-01/REQ-02 como regras principais. O exemplo do slide 9 menciona taxa de R$ 20, regiões e identificadores RF/RB diferentes. O trecho do slide 12 também menciona Sudeste, mas o passo A do slide 13 manda atualizar REQ-02. Este laboratório segue a regra principal uniforme de R$ 15, sem CEP ou região. Não altera a aplicação de atividades anteriores. REQ-03 explicita a validação solicitada na revisão de segurança e o exemplo de valor inválido do material.

Cupons, descontos, banco de dados, API e interface web estão fora desta tarefa.
