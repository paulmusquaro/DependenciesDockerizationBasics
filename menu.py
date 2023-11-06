# import importlib
import os
from abc import ABC, abstractmethod
from calend import calend_main
from Addressbook import start as start_ab
from notebook.nb_main import NoteManager
from file_sorter import start as start_fs
from exchanger import ex_main


class UserInterface(ABC):
    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_commands(self):
        pass


class ConsoleUserInterface(UserInterface):
    def display_menu(self):
        pass

    def display_contacts(self, contacts):
        pass

    def display_notes(self, notes):
        pass

    def display_commands(self):
        pass


class Menu:
    def __init__(self, user_interface):
        self.choices = {
            1: ("file_sorter", start_fs),
            2: ("Addressbook", start_ab),
            3: ("notebook.nb_main", "nb_main"),
            4: ("calend", calend_main),
            5: ("exchanger", ex_main)
        }

        self.user_interface = user_interface

    def make_decision(self, choice):
        module_name, function_name = self.choices.get(choice)
        
        if not module_name:
            return
        
        if choice == 3:
            note_folder = "notebook/notes"
            note_manager = NoteManager(note_folder)
            note_manager.nb_main()
            return True

        try:

            if choice == 1:
                directory_path = input("Enter the path to directory: ")
                if os.path.exists(directory_path) and os.path.isdir(directory_path):
                    function_name(directory_path)
                else:
                    print("Invalid directory path. Please enter a valid directory path.")
            else:
                function_name()
        except ModuleNotFoundError:
            print("Module not found.")
        except AttributeError:
            print("Function not found in the module.")


def main():
    print("Choose an option:")
    print("1. File Sorter")
    print("2. Address Book")
    print("3. Notebook")
    print("4. Calendar")
    print("5. Exchanger")
    print("6. Exit")

    user_interface = ConsoleUserInterface()
    menu = Menu(user_interface)

    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 6:
                break
            menu.make_decision(choice)

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
