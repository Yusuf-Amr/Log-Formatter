
from utils.get_log_parser import get_log_parser
from utils.display_menu import display_menu

def main_loop():
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == '0':
            print("Exiting the log formatter. Goodbye!")
            break

        log = input("Please enter the log: ").strip()
        if not log:
            print("Log cannot be empty. Please enter a valid log.")
            continue

        try:
            parser = get_log_parser(choice, log)
            parser.parse()
            parser.display()
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An error occurred: {e}")



