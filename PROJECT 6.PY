import os
import datetime

# The file where journal entries will be stored
FILENAME = "journal.txt"

def display_menu():
    """Displays the main menu."""
    print("\nWelcome to Personal Journal Manager!")
    print("Please select an option:")
    print("\n1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

def add_entry():
    """Option 1: Adds a new journal entry with a timestamp."""
    entry_text = input("\nEnter your journal entry:\n")
    
    # Get current date and time in the specified format
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    
    # Append to the file (create if it doesn't exist)
    with open(FILENAME, "a") as file:
        file.write(f"{timestamp}\n{entry_text}\n\n")
        
    print("\nEntry added successfully!")

def view_entries():
    """Option 2: Displays all journal entries."""
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("\nOutput (If the file does not exist):")
        print("No journal entries found. Start by adding a new entry!")
        return

    print("\nOutput (If the file exists):")
    print("Your Journal Entries:")
    print("-" * 26)
    
    with open(FILENAME, "r") as file:
        content = file.read().strip()
        if content:
            print(content)
        else:
            print("No journal entries found. Start by adding a new entry!")

def search_entries():
    """Option 3: Searches for a keyword or date in the journal."""
    # Handle File Not Found Error
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("\nOutput:")
        print("Error: The journal file does not exist. Please add a new entry first.")
        return

    keyword = input("\nEnter a keyword or date to search: ")
    
    found = False
    matching_entries = []
    
    with open(FILENAME, "r") as file:
        # Split entries by double newline (blank line between entries)
        entries = file.read().strip().split("\n\n")
        
        for entry in entries:
            if keyword.lower() in entry.lower():
                matching_entries.append(entry)
                found = True

    if found:
        print("\nOutput (If a match is found):")
        print("Matching Entries:")
        print("-" * 18)
        for entry in matching_entries:
            print(entry)
            print() # Add a blank line between entries
    else:
        print("\nOutput (If no match is found):")
        print(f"No entries were found for the keyword: {keyword}.")

def delete_all_entries():
    """Option 4: Deletes the journal file after confirmation."""
    confirm = input("\nAre you sure you want to delete all entries? (yes/no): ")
    
    if confirm.lower() == "yes":
        if os.path.exists(FILENAME):
            os.remove(FILENAME)
            print("\nOutput (If the file is deleted successfully):")
            print("All journal entries have been deleted.")
        else:
            print("\nOutput (If the file does not exist):")
            print("No journal entries to delete.")

def main():
    """Main program loop to handle user interactions."""
    while True:
        display_menu()
        
        user_input = input("\nUser Input:\n")
        
        if user_input == "1":
            add_entry()
        elif user_input == "2":
            view_entries()
        elif user_input == "3":
            search_entries()
        elif user_input == "4":
            delete_all_entries()
        elif user_input == "5":
            print("\nOutput:")
            print("Thank you for using Personal Journal Manager. Goodbye!")
            break
        else:
            print("\nOutput:")
            print("Invalid option. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()