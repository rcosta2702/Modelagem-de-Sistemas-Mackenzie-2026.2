# Exercício 2 - experimento controlado

Prompt ambíguo do enunciado: "Implemente a funcionalidade de aplicação de cupom de desconto 'DESCONTO10' para a classe de frete."

Este prompt foi tratado como objeto do exercício, não como alteração autorizada da especificação. Para demonstrar o desvio, foi acrescentada temporariamente a função aplicar_cupom ao módulo local. A interpretação deliberada foi desconto de 10% sobre o total, algo que não está definido no prompt nem na spec.

O código temporário está preservado em frete-com-drift.py.txt. Não é resultado de uma segunda IA nem de uma interação no plugin do PyCharm: o experimento foi produzido pelo Codex nesta sessão.

A auditoria rejeita a função inteira por ausência de cláusula EARS. Não são necessárias funções de cupom extras, logs ou persistência para demonstrar o problema. A correção consiste em remover a função e executar a suíte novamente.
