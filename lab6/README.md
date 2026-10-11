# Lab 6 - SDD e revisão multidimensional

Implementação dos três exercícios com Codex, substituindo o Google Antigravity conforme solicitado.

## Executar

Requer Python 3.14+. Abra esta pasta como projeto no PyCharm, selecione um interpretador Python 3.14 e instale requirements-dev.txt. Execute a pasta tests com o runner pytest.

Também é possível executar localmente:

```console
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Entregas

1. **TDD:** constitution.md, specs/checkout_frete.md, tasks/TASK-01.md, src/frete.py e tests/test_frete.py. As versões iniciais e os resultados Red/Green estão em evidence/.
2. **Auditoria:** audit_report.md e evidence/ex2-experimento.md, incluindo o cupom temporário rejeitado.
3. **Spec viva:** REQ-02 atualizado para 250 antes de testes e código; evidências ex3-red.txt e ex3-green.txt.

Exemplo final: subtotal 249,99 gera frete 15 e total 264,99; subtotal 250 gera frete zero e total 250.

O módulo deste laboratório é independente da aplicação anterior, que tem outra especificação. Execute os testes a partir desta pasta para usar seu pytest.ini e evitar colisão com o frete.py da atividade anterior.

Leia as decisões de escopo em specs/checkout_frete.md e as limitações em audit_report.md. Os testes foram executados localmente pelo Codex; não se afirma execução na interface do PyCharm. A revisão humana prevista no laboratório deve ser feita pelo aluno.
