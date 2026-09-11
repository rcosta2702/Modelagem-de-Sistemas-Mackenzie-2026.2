import unittest

from app import app
from frete import calcular_frete, identificar_regiao


class FreteTest(unittest.TestCase):
    def test_limites_regionais(self):
        for cep, limite in [("69005010", 300), ("01001000", 200),
                            ("40020000", 200), ("70040900", 200), ("90010000", 200)]:
            with self.subTest(cep=cep):
                self.assertEqual(calcular_frete(limite - 0.01, cep)["frete"], 20)
                self.assertEqual(calcular_frete(limite, cep)["frete"], 0)
                self.assertEqual(calcular_frete(limite + 1, cep)["frete"], 0)

    def test_regioes_e_fronteiras(self):
        for cep, regiao in [("01001-000", "Sudeste"), ("65999999", "Nordeste"),
                            ("66000000", "Norte"), ("69999999", "Norte"),
                            ("70000000", "Centro-Oeste"), ("76799999", "Centro-Oeste"),
                            ("76800000", "Norte"), ("77001002", "Norte"),
                            ("78000000", "Centro-Oeste"), ("80000000", "Sul")]:
            with self.subTest(cep=cep):
                self.assertEqual(identificar_regiao(cep), regiao)

    def test_valores_invalidos(self):
        for valor in [0, -1, None, True, False, "", "abc", "NaN", "Infinity", [], {}]:
            with self.subTest(valor=valor):
                with self.assertRaisesRegex(ValueError, "^Valor do carrinho inválido$"):
                    calcular_frete(valor, "01001000")

    def test_ceps_invalidos_mesmo_com_frete_gratis(self):
        for cep in [None, 1001000, "", "00000000", "123", "abcdefgh", "01001--000", "010010000"]:
            with self.subTest(cep=cep):
                with self.assertRaisesRegex(ValueError, "^CEP inválido ou região não atendida$"):
                    calcular_frete(1000, cep)


class AppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_pagina_principal(self):
        resposta = self.client.get("/")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn('id="form-frete"', resposta.get_data(as_text=True))

    def test_calculo(self):
        for valor, frete in [(100, 20), (300, 0)]:
            with self.subTest(valor=valor):
                resposta = self.client.post("/calcular", json={"valor_carrinho": valor, "cep": "69005010"})
                self.assertEqual(resposta.status_code, 200)
                self.assertEqual(resposta.json, {"regiao": "Norte", "frete": frete})

    def test_erros_de_dominio(self):
        for dados, mensagem in [({}, "Valor do carrinho inválido"),
                                ({"valor_carrinho": 0, "cep": "01001000"}, "Valor do carrinho inválido"),
                                ({"valor_carrinho": 100}, "CEP inválido ou região não atendida")]:
            with self.subTest(dados=dados):
                resposta = self.client.post("/calcular", json=dados)
                self.assertEqual(resposta.status_code, 400)
                self.assertEqual(resposta.json, {"erro": mensagem})

    def test_json_invalido(self):
        for corpo in ["{", "null", "[]", "42", '"texto"']:
            with self.subTest(corpo=corpo):
                resposta = self.client.post("/calcular", data=corpo, content_type="application/json")
                self.assertEqual(resposta.status_code, 400)
                self.assertIn("erro", resposta.json)
        self.assertEqual(self.client.post("/calcular", data="texto").status_code, 400)


if __name__ == "__main__":
    unittest.main()
