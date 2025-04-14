"""Assistant bot application to manage a contact list via command-line interface."""

import sys

from constants import HELP_TIP_STR, PHONE_FORMAT_DESC_STR
from input_parser import parse_input
from contacts_validator import (
    validate_are_two_arguments,
    validate_is_one_argument_username,
    validate_contact_not_in_contacts,
    validate_contact_name_exists,
    validate_phone_number,
    validate_not_phone_duplicate,
    validate_contacts_not_empty
)
from contacts_handler import add_contact, change_contact, show_phone, show_all

# def main():
#     """
#     Використовуйте словник Python для зберігання імен і номерів телефонів. 
#     Ім'я буде ключем, а номер телефону – значенням.
#     """
#     """
#     Ваша програма має вміти ідентифікувати та повідомляти про 
#     неправильно введені команди.
#     """
#     contacts = {}

#     print("Welcome to the assistant bot!")
    
#     while True:
#         user_input = input(f"\nEnter a command (or {HELP_TIP_STR}): ")

#         command, args = parse_input(user_input)

#         match command:
#             # 1 greeting
#             case "hello":
#                 print("How can I help you?")
#             # 2 "add [ім'я] [номер телефону]" -> add_contact() e.g. "add John 1234567890" -> "Contact added."
#             case "add":
#                 print(add_contact(args, contacts))
#             # 3 "change [ім'я] [новий номер телефону]" -> change_contact() e.g. "change John 0987654321" -> "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено
#             case "change":
#                 print(change_contact(args, contacts))
#             # 4 "phone [ім'я]" -> show_phone e.g. "phone John" -> [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено
#             # "phone username" За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.
#             case "phone":
#                 print(show_phone(args, contacts))
#             # 5 "all" -> show_all() e.g. "all" -> усі збережені контакти з номерами телефонів
#             # "all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
#             case "all":
#                 print(show_all(contacts))
#             # 6 "close" або "exit" -> "close" або "exit" -> "Good bye!"
#             # "close", "exit" за будь-якою з цих команд бот завершує свою роботу після того, як виведе у консоль повідомлення "Good bye!" та завершить своє виконання.
#             case "close" | "exit":
#                 print("Good bye!")
#                 sys.exit(0)
#             # 7 help
#             case "help":
#                 print("list of commands")
#             # 8 other -> "Invalid command."
#             case _:
#                 print(f"Invalid command. {HELP_TIP_STR.capitalize()}.")

def main_alternative():
    """
    Main function to run the assistant bot. It handles user input, command dispatching,
    validation, and help generation for a contact book CLI assistant.
    """
    contacts = {}

    def show_greeting():
        """Returns a greeting message to the user."""
        return f"How can I help you?\nMeanwhile, you may {HELP_TIP_STR}."

    def get_help():
        """
        Generate formatted help text from available commands.

        Returns:
            str: Aligned list of commands with their descriptions.
        """
        help_entries = []

        # Prepare all command strings with their details
        for command, metadata in menu.items():
            # Skip commands that are hidden from help (visible=False by design)
            if not metadata.get("visible", True):
                continue

            # Format aliases: "exit (or close)"
            aliases = metadata.get("aliases", [])
            alias_str = f" (or {', '.join(aliases)})" if aliases else ""

            # Build the command string with arguments
            command_str = f"{command}{alias_str} {metadata['arg_str']}".strip()

            # Append command string and description to the help list
            help_entries.append((command_str, metadata['description']))

        # Find the longest command string to align the output
        max_command_length = max(len(cmd_str) for cmd_str, _ in help_entries)

        # Format help lines with aligned commands and descriptions
        formatted_help_lines = [
            f"{cmd_str.ljust(max_command_length)} - {description}"
            for cmd_str, description in help_entries
        ]
        # Add a blank line before the list starts
        formatted_help_lines.insert(0, "")

        return "\n".join(formatted_help_lines)
    
    def exit_program():
        """Exits the program with a goodbye message."""
        print("Good bye!")
        sys.exit(0)

    menu = {
        "hello": {
            "arg_str": "",
            "description": "Greet the user",
            "validators": None,
            "handler": lambda _, __: show_greeting(),
        },
        "add": {
            "arg_str": "<username> <phone>",
            "description": "Add a new contact",
            "validators": (
                    validate_are_two_arguments,
                    validate_phone_number,
                    validate_contact_not_in_contacts
                ),
            "handler": add_contact,
        },
        "change": {
            "arg_str": "<username> <new_phone>",
            "description": "Update contact's phone number",
            "validators": (
                    validate_are_two_arguments,
                    validate_phone_number,
                    validate_contact_name_exists,
                    validate_not_phone_duplicate
                ),
            "handler": change_contact,
        },
        "phone": {
            "arg_str": "<username>",
            "description": f"Show contact's phone number ({PHONE_FORMAT_DESC_STR})",
            "validators": (
                    validate_is_one_argument_username,
                    validate_contact_name_exists
                ),
            "handler": show_phone,
        },
        "all": {
            "arg_str": "",
            "description": "Display all contacts",
            "validators": (validate_contacts_not_empty,),
            "handler": show_all,
        },
        "help": {
            "arg_str": "",
            "description": "Show available commands",
            "validators": None,
            "handler": lambda _, __: get_help(),
        },
        "exit": {
            "aliases": ["close"],
            "arg_str": "",
            "description": "Exit the app",
            "validators": None,
            "handler": lambda _, __: exit_program(),
        },
        "close": {
            "visible": False,
            "arg_str": "",
            "description": "Exit the app",
            "validators": None,
            "handler": lambda _, __: exit_program(),
        },
    }

    # Initial greeting and help menu
    print("\nWelcome to the assistant bot!".upper())
    print("\nHere you have the list of available options for you:")
    print(get_help())
    
    while True:
        # Ask user for command
        user_input = input(f"\nEnter a command (or {HELP_TIP_STR}): ")
        if not user_input:
            print("Invalid empty command, please try again.")
            continue

        # Parse entered command with arguments 
        command, args = parse_input(user_input)

        # Try to match input command with one from the menu
        metadata = menu.get(command)
        if not metadata:
            print(f"Invalid command. {HELP_TIP_STR.capitalize()}.")
            continue

        # Run validation checks (where applicable)
        if metadata["validators"]:
            try:
                # Run all available validators
                for validator in metadata["validators"]:
                    # Execute each validator
                    validator(args, contacts)
            except ValueError as exc:
                print(f"{exc}")
                continue

        # Call handling function
        result = metadata["handler"](args, contacts)
        if result:
            print(result)

if __name__ == "__main__":
    try:
        main_alternative()
    except KeyboardInterrupt:
        print("\nGood bye! (Interrupted by user)")
        sys.exit(0)
