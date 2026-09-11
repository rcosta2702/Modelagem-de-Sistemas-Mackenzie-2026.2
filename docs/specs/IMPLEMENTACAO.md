# Execução e premissas

Na raiz do projeto:

```powershell
uv sync
uv run python docs/specs/app.py
```

Abra http://127.0.0.1:5000. Para executar os testes:

```powershell
uv run python -m unittest discover -s docs/specs -p "test_*.py" -v
```

`POST /calcular` recebe JSON como `{"valor_carrinho": 150, "cep": "01001-000"}`.
O sucesso retorna HTTP 200 com `{"regiao": "Sudeste", "frete": 20.0}`;
entradas inválidas retornam HTTP 400 com `{"erro": "mensagem"}`.

## Premissas pendentes de confirmação

A especificação não define a tarifa paga nem a cobertura de CEPs, e o arquivo
de testes original estava vazio. Esta implementação adota provisoriamente:

- Frete fixo de R$ 20,00 abaixo do limite regional, definido em `FRETE_PADRAO`.
- Atendimento às cinco regiões por faixas postais, incluindo Rondônia e
  Tocantins na região Norte.
- Validação local do formato e da faixa do CEP. Não verifica se o endereço
  existe: isso exigiria uma base de CEPs ou integração com um serviço externo.
- Valores monetários numéricos ou strings decimais com ponto na API.

O formato postal tem oito dígitos, conforme o
[Guia de Endereçamento dos Correios](https://www.correios.com.br/enviar/precisa-de-ajuda/guia-de-enderecamento/guia-de-enderecamento).
A interface também aceita o hífen entre o quinto e o sexto dígito.

Os testes adicionados cobrem as regras documentadas e essas premissas.
