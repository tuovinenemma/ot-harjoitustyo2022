import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(990)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_saldo_vahenee_jos_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_metodi_palauttaa_true_jos_tarpeeksi_rahaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))

    def test_metodi_palauttaa_false_jos_ei_tarpeeksi_rahaa(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1000))
