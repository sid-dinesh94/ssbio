import unittest
import ssbio.databases.bigg

class TestBiGG(unittest.TestCase):
    """Unit tests for BiGG
    """

    def test_get_pdbs_for_gene(self):
        model = 'e_coli_core'
        gene = 'b0118'

        expected = [('1l5j', 'A'), ('1l5j', 'B')]

        self.assertCountEqual(expected, ssbio.databases.bigg.get_pdbs_for_gene(model, gene))

        model = 'e_coli_core'
        gene = 'b0351'

        expected = []

        self.assertCountEqual(expected, ssbio.databases.bigg.get_pdbs_for_gene(model, gene))