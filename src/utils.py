import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load election data from a CSV file with error handling for different encodings.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing election data, or None if an error occurs.
    """
    try:
        try:
            data = pd.read_csv(file_path, encoding='utf-8')
        except UnicodeDecodeError:
            print("UTF-8 decoding failed. Trying a different encoding...")
            data = pd.read_csv(file_path, encoding='ISO-8859-1')  # Try latin1 (ISO-8859-1) encoding

        # Clean column names (strip spaces and fix case issues)
        data.columns = data.columns.str.strip()

        # Map columns from the dataset to the expected column names
        data['Candidate Name'] = data['Member first name'] + ' ' + data['Member surname']  # Combine first and surname
        data['Constituency'] = data['Constituency name']
        data['Votes'] = data['Valid votes']  # Assuming 'Valid votes' corresponds to the votes for a candidate
        data['Party'] = data['First party']  # You can add more logic here to handle multiple parties if needed
        data['Votes Cast'] = data['Valid votes'] + data['Invalid votes']  # Assuming total votes cast includes both valid and invalid votes
        
        # Drop unnecessary columns (you can keep or modify these based on your needs)
        data = data[['Candidate Name', 'Party', 'Votes', 'Constituency', 'Votes Cast']]

        # Print cleaned column names to verify
        print("Cleaned columns in the dataset:", data.columns)

        print("Data loaded successfully!")
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    return None

def save_statistics(data, file_path):
    """
    Save the calculated statistics to a file.

    Args:
        data (list): List of statistics to be saved.
        file_path (str): Path to the file where data will be saved.
    """
    try:
        with open(file_path, 'w') as f:
            for line in data:
                f.write(f"{line}\n")
        print(f"Statistics saved to {file_path}")
    except IOError:
        print("Error writing to file.")

def plot_party_votes(data):
    """
    Plot a bar chart of votes for each party.

    Args:
        data (pd.DataFrame): DataFrame containing election data.
    """
    party_votes = data.groupby('Party')['Votes'].sum()
    
    # Create a bar chart
    plt.figure(figsize=(10,6))
    party_votes.plot(kind='bar', color='skyblue')
    plt.title('Votes by Party')
    plt.xlabel('Party')
    plt.ylabel('Total Votes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

