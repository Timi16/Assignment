import unittest
import os
import pandas as pd
from src.utils import load_data, save_statistics, plot_party_votes

class TestUtils(unittest.TestCase):

    def test_load_data_valid(self):
        # Test loading a valid CSV file
        data = load_data('data/EditedData.csv')
        self.assertIsInstance(data, pd.DataFrame)  # Ensure data is loaded as DataFrame
        self.assertTrue('Candidate Name' in data.columns)  # Ensure the 'Candidate Name' column exists

    def test_load_data_invalid(self):
        # Test invalid file path
        data = load_data('data/non_existent_file.csv')
        self.assertIsNone(data)  # Should return None for invalid file path

    def test_save_statistics(self):
        # Test saving statistics to a file
        stats = ["Party A: 5000 votes", "Party B: 4000 votes"]
        save_statistics(stats, "test_output.txt")
        
        # Verify the file is created
        self.assertTrue(os.path.exists("test_output.txt"))
        
        # Verify the contents of the file
        with open("test_output.txt", "r") as file:
            content = file.readlines()
        self.assertEqual(content[0].strip(), "Party A: 5000 votes")
        self.assertEqual(content[1].strip(), "Party B: 4000 votes")
        
        # Clean up the test file
        os.remove("test_output.txt")

    def test_plot_party_votes(self):
        # Test plotting function (check if it runs without errors)
        data = pd.DataFrame({
            'Party': ['Party A', 'Party B', 'Party C'],
            'Votes': [5000, 4000, 3000]
        })
        try:
            plot_party_votes(data)  # If no errors, the test passes
            plot_success = True
        except Exception as e:
            plot_success = False
        self.assertTrue(plot_success)  # Ensure the plot function runs successfully

if __name__ == "__main__":
    unittest.main()
