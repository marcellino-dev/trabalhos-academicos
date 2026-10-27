import unittest

import numpy as np

from funcoes_pertinencia import (
    tempo_rapido, tempo_medio, tempo_lento,
    cordialidade_baixa, cordialidade_media, cordialidade_alta,
)
from regras import avaliar_atendimento


class TestFuncoesPertinencia(unittest.TestCase):
    def test_tempo_rapido(self):
        self.assertEqual(tempo_rapido(10), 1.0)
        self.assertAlmostEqual(tempo_rapido(15), 0.5)
        self.assertEqual(tempo_rapido(20), 0.0)

    def test_tempo_medio(self):
        self.assertEqual(tempo_medio(10), 0.0)
        self.assertEqual(tempo_medio(20), 1.0)
        self.assertAlmostEqual(tempo_medio(25), 0.5)
        self.assertEqual(tempo_medio(30), 0.0)

    def test_tempo_lento(self):
        self.assertEqual(tempo_lento(25), 0.0)
        self.assertAlmostEqual(tempo_lento(30), 0.5)
        self.assertEqual(tempo_lento(60), 1.0)

    def test_cordialidade_baixa(self):
        self.assertEqual(cordialidade_baixa(3), 1.0)
        self.assertAlmostEqual(cordialidade_baixa(4), 0.5)
        self.assertEqual(cordialidade_baixa(5), 0.0)

    def test_cordialidade_media(self):
        self.assertEqual(cordialidade_media(3), 0.0)
        self.assertEqual(cordialidade_media(5), 1.0)
        self.assertAlmostEqual(cordialidade_media(6), 0.5)
        self.assertEqual(cordialidade_media(7), 0.0)

    def test_cordialidade_alta(self):
        self.assertEqual(cordialidade_alta(6), 0.0)
        self.assertAlmostEqual(cordialidade_alta(7), 0.5)
        self.assertEqual(cordialidade_alta(10), 1.0)

    def test_pertinencia_sempre_entre_0_e_1(self):
        funcoes_tempo = (tempo_rapido, tempo_medio, tempo_lento)
        funcoes_cord = (cordialidade_baixa, cordialidade_media, cordialidade_alta)
        for t in np.linspace(0, 60, 121):
            for f in funcoes_tempo:
                self.assertTrue(0.0 <= f(t) <= 1.0)
        for c in np.linspace(0, 10, 101):
            for f in funcoes_cord:
                self.assertTrue(0.0 <= f(c) <= 1.0)


class TestAvaliarAtendimento(unittest.TestCase):
    def test_caso_1_rapido_e_muito_cordial(self):
        r = avaliar_atendimento(8, 9)
        self.assertAlmostEqual(r["excelente"], 1.0)
        self.assertAlmostEqual(r["qualidade_final"], 9.0)

    def test_caso_2_atendimento_medio(self):
        r = avaliar_atendimento(15, 6)
        self.assertAlmostEqual(r["boa"], 0.5)
        self.assertAlmostEqual(r["regular"], 0.5)
        self.assertAlmostEqual(r["qualidade_final"], 6.0)

    def test_caso_3_demorado_e_pouco_cordial(self):
        r = avaliar_atendimento(35, 3)
        self.assertAlmostEqual(r["ruim"], 1.0)
        self.assertAlmostEqual(r["qualidade_final"], 2.0)

    def test_caso_4_bom_atendimento_geral(self):
        r = avaliar_atendimento(12, 8)
        self.assertAlmostEqual(r["excelente"], 0.8)
        self.assertAlmostEqual(r["boa"], 0.2)
        self.assertAlmostEqual(r["qualidade_final"], 8.6)

    def test_caso_4_melhor_que_caso_2(self):
        self.assertGreater(
            avaliar_atendimento(12, 8)["qualidade_final"],
            avaliar_atendimento(15, 6)["qualidade_final"],
        )

    def test_nota_dentro_da_faixa_em_todo_o_dominio(self):
        for t in np.linspace(0, 60, 61):
            for c in np.linspace(0, 10, 21):
                nota = avaliar_atendimento(t, c)["qualidade_final"]
                self.assertTrue(2.0 - 1e-9 <= nota <= 9.0 + 1e-9)

    def test_nenhuma_regra_fica_sem_ativacao(self):
        for t in np.linspace(0, 60, 121):
            for c in np.linspace(0, 10, 101):
                r = avaliar_atendimento(t, c)
                soma = r["excelente"] + r["boa"] + r["regular"] + r["ruim"]
                self.assertGreater(soma, 0.0, f"sem ativacao em tempo={t}, cordialidade={c}")


if __name__ == "__main__":
    unittest.main()
