# Auditoria de rastreabilidade - Lab 6

## Matriz final

| Cláusula | Status | Teste coberto | Arquivo:linha |
| --- | --- | --- | --- |
| REQ-01: taxa de 15 e total | Atendido | tests/test_frete.py:10 | src/frete.py:5, src/frete.py:22, src/frete.py:28 |
| REQ-02: isenção a partir de 250 | Atendido | tests/test_frete.py:17 | src/frete.py:6, src/frete.py:25 |
| REQ-03: valor válido | Atendido | tests/test_frete.py:25 | src/frete.py:9 |
| Contrato monetário | Atendido | tests/test_frete.py:31 | src/frete.py:14 |
| Cupom sem spec | Drift detectado e removido | Não havia teste funcional do cupom | evidence/frete-com-drift.py.txt:34; ausente de src/frete.py final |

## Exercício 2: detecção e correção

A função temporária aplicar_cupom presumiu desconto de 10% sobre o total. Nenhuma cláusula define cupom, base de cálculo ou elegibilidade. A função foi rejeitada por sobre-implementação, mesmo com os 37 testes passando. Evidências: ex2-com-drift.txt e frete-com-drift.py.txt. Após a remoção, os 37 testes continuaram aprovados (ex2-corrigido.txt).

O experimento foi executado pelo Codex diretamente nos arquivos locais. Não se atribui uma interação fictícia ao Antigravity ou ao plugin do PyCharm. A revisão documentada é do agente; a validação humana do aluno ainda deve ser realizada por ele.

## Passe multidimensional

- **Arquitetura:** funções pequenas e determinísticas; somente decimal da biblioteca padrão. Sem classes, serviços ou persistência desnecessários. A validação é compartilhada. O total chama a função de frete, que revalida o Decimal; custo constante e simplicidade aceitável neste escopo.
- **Performance:** nenhuma consulta externa ou laço de negócio. A quantidade de operações é constante, embora a conversão dependa do tamanho da entrada. Não há benchmark nem garantia de latência. Para uma API pública futura seria necessário limitar o tamanho da entrada antes da conversão.
- **Segurança:** booleanos, valores não finitos, não positivos e frações de centavo são rejeitados. Nenhum print, log de entrada, segredo, arquivo ou chamada de rede. A precisão padrão de Decimal limita a magnitude processável; valores além dessa precisão podem ser rejeitados. Isso não é uma auditoria de uma aplicação web.
- **Observabilidade:** nomes claros, docstrings com REQ e mensagens de erro estáveis; resultados pytest preservados em evidence/. Logs de produção não são necessários para uma função pura.

## Divergências do enunciado

Adotadas as cláusulas REQ-01/REQ-02 dos slides 7 e 13: taxa 15 e limite final 250 para todos os cálculos. O exemplo regional/taxa 20 dos slides 9 e 12 não foi misturado a esta tarefa. A atividade anterior permanece independente. REQ-03 e o contrato monetário foram explicitados antes da implementação.

## Evidências e limites

Exercício 1: Red por módulo ausente; Green com 37 testes. Exercício 2: 37 testes com e sem o drift. Exercício 3: 3 falhas e 36 aprovações antes de mudar o código; resultado final em evidence/ex3-green.txt.

Execuções realizadas com Python 3.14 e pytest no ambiente local via ferramentas do Codex. Não são capturas de execução dentro do PyCharm. A revisão visual na IDE e a publicação no GitHub dependem da etapa de integração.
