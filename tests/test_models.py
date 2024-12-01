import unittest
from src.models import MP, Party, Constituency

class TestModels(unittest.TestCase):
    def test_mp_initialization(self):
        mp = MP("Jane Doe", "Independent", "Somewhere", 5000)
        self.assertEqual(mp.name, "Jane Doe")
        self.assertEqual(mp.votes, 5000)

    def test_party_votes(self):
        party = Party("Independent")
        mp = MP("Jane Doe", "Independent", "Somewhere", 5000)
        party.add_mp(mp)
        self.assertEqual(party.total_votes, 5000)

if __name__ == "__main__":
    unittest.main()
