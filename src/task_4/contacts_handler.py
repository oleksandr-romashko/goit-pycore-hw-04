"""
Simple contact management module.

This module provides basic functions to manage a contact list,
including adding, updating, and displaying contact phone numbers.

Functions:
- add_contact(args, contacts): Adds a new contact.
- change_contact(args, contacts): Changes an existing contact's phone number.
- show_phone(args, contacts): Shows the phone number of a contact.
- show_all(_, contacts): Shows all saved contacts.
"""

def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Add a new contact with username and phone number.

    args: [username, phone]
    """
    username, phone = args
    contacts[username] = phone
    return "Contact added."

def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """Update the phone number of an existing contact.

    args: [username, new_phone]
    """
    username, phone = args
    contacts[username] = phone
    return "Contact updated."

def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """Display the phone number for the specified contact.

    args: [username]
    """
    username = args[0]
    return f"{username} number is {contacts[username]}"

def show_all(_: list[str], contacts: dict[str, str]) -> str:
    """Return all saved contacts with their phone numbers."""
    return "\n".join(f"{username} number is {phone}" for username, phone in contacts.items())