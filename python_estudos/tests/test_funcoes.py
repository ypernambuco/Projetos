import importlib.util
import tempfile
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def carregar_modulo(nome: str, caminho: Path):
    spec = importlib.util.spec_from_file_location(nome, caminho)
    modulo = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(modulo)
    return modulo


class TestClassificacaoIdade(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modulo = carregar_modulo(
            "classificacao_idade",
            ROOT / "01_inicio" / "02_classificacao_idade.py",
        )

    def test_classifica_crianca_adolescente_e_adulto(self):
        self.assertEqual(self.modulo.classificar_idade(8), "criança")
        self.assertEqual(self.modulo.classificar_idade(15), "adolescente")
        self.assertEqual(self.modulo.classificar_idade(30), "adulto")

    def test_idade_negativa_nao_e_aceita(self):
        with self.assertRaises(ValueError):
            self.modulo.classificar_idade(-1)


class TestMaioridade(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modulo = carregar_modulo(
            "maioridade",
            ROOT / "01_inicio" / "03_maioridade.py",
        )

    def test_calcula_anos_para_maioridade(self):
        self.assertEqual(self.modulo.anos_para_maioridade(10), 8)
        self.assertEqual(self.modulo.anos_para_maioridade(18), 0)
        self.assertEqual(self.modulo.anos_para_maioridade(25), 0)


class TestCadastroPessoasCsv(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modulo = carregar_modulo(
            "cadastro_pessoas_csv",
            ROOT / "01_inicio" / "04_cadastro_pessoas_csv.py",
        )

    def test_conta_adultos(self):
        pessoas = [
            {"nome": "Ana", "idade": 17, "profissao": "estudante"},
            {"nome": "Bia", "idade": 18, "profissao": "analista"},
            {"nome": "Caio", "idade": 30, "profissao": "dev"},
        ]

        self.assertEqual(self.modulo.contar_adultos(pessoas), 2)

    def test_salva_e_carrega_csv(self):
        pessoas = [
            {"nome": "Ana", "idade": 20, "profissao": "dev"},
            {"nome": "Bruno", "idade": 16, "profissao": "estudante"},
        ]

        with tempfile.TemporaryDirectory() as pasta:
            caminho = Path(pasta) / "pessoas.csv"
            self.modulo.salvar_csv(pessoas, caminho, mostrar_mensagem=False)
            pessoas_carregadas = self.modulo.carregar_csv(caminho)

        self.assertEqual(pessoas_carregadas, pessoas)


class TestControleEstoque(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modulo = carregar_modulo(
            "controle_estoque",
            ROOT / "02_exercicios" / "01_controle_estoque.py",
        )

    def test_calcula_total_item(self):
        item = {"produto": "Caderno", "preco": Decimal("12.50"), "quantidade": 4}
        self.assertEqual(self.modulo.calcular_total_item(item), Decimal("50.00"))

    def test_calcula_total_estoque(self):
        estoque = [
            {"produto": "Caderno", "preco": Decimal("12.50"), "quantidade": 4},
            {"produto": "Caneta", "preco": Decimal("2.00"), "quantidade": 3},
        ]

        self.assertEqual(self.modulo.calcular_total_estoque(estoque), Decimal("56.00"))

    def test_formata_moeda(self):
        self.assertEqual(self.modulo.formatar_moeda(Decimal("12.5")), "R$ 12.50")


class TestMiniEtlVendas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.modulo = carregar_modulo(
            "mini_etl_vendas",
            ROOT / "03_preparacao_etl" / "01_mini_etl_vendas.py",
        )

    def test_normaliza_coluna(self):
        self.assertEqual(self.modulo.normalizar_coluna("Preço Unitário"), "preco_unitario")

    def test_calcula_valor_total(self):
        total = self.modulo.calcular_valor_total(
            quantidade=2,
            preco_unitario=Decimal("80.50"),
            desconto=Decimal("10.00"),
        )

        self.assertEqual(total, Decimal("151.00"))

    def test_descarta_venda_com_data_invalida(self):
        venda = self.modulo.transformar_venda(
            {
                "ID Venda": "1003",
                "Data Venda": "data invalida",
                "Cliente": "Carla Lima",
                "Produto": "Teclado",
                "Quantidade": "1",
                "Preco Unitario": "230.90",
                "Desconto": "10.90",
            }
        )

        self.assertIsNone(venda)

    def test_transforma_venda_valida(self):
        venda = self.modulo.transformar_venda(
            {
                "ID Venda": "1002",
                "Data Venda": "02/05/2026",
                "Cliente": " Bruno Costa ",
                "Produto": "Mouse",
                "Quantidade": "2",
                "Preco Unitario": "80.50",
                "Desconto": "0",
            }
        )

        self.assertEqual(venda["data_venda"], "2026-05-02")
        self.assertEqual(venda["cliente"], "Bruno Costa")
        self.assertEqual(venda["valor_total"], "161.00")


if __name__ == "__main__":
    unittest.main()
