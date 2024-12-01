from utils import load_data, save_statistics, plot_party_votes
from menu import display_menu, get_user_option

def main():
    # Load the data
    data = load_data("data/EditedData.csv")
    if data is None:
        return

    while True:
        # Display the menu
        display_menu()
        
        # Get user input
        option = get_user_option()

        # Handle menu options
        if option == "1":
            print(data[['Candidate Name', 'Party']])
        elif option == "2":
            print(data.groupby('Party')['Votes'].sum())
        elif option == "3":
            print(data[['Constituency', 'Votes Cast']])
        elif option == "4":
            data['Percentage'] = (data['Votes'] / data['Votes Cast']) * 100
            print(data[['Candidate Name', 'Percentage']])
        elif option == "5":
            stats = ["Total Votes by Party",str(data.groupby('Party')['Votes'].sum())]
            save_statistics(stats, "output.txt")
        elif option == "6":
            plot_party_votes(data)
        elif option == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
