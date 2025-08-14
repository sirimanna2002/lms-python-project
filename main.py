# main.py
from library_ui import LibraryUI
from user import UserManager
import os

class MainSystem:
    def __init__(self):
        self.user_manager = UserManager()
        self.library_ui = LibraryUI()
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_main_menu(self):
        print("\n=== Library Management System ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
    def register(self):
        self.clear_screen()
        print("\n=== User Registration ===")
        
        full_name = input("Enter Full Name: ")
        address = input("Enter Address: ")
        id_number = input("Enter ID Number: ")
        contact_number = input("Enter Contact Number: ")
        email = input("Enter Email Address: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        
        success, message = self.user_manager.register_user(
            full_name, address, id_number, contact_number, 
            email, username, password
        )
        
        print(f"\n{message}")
        input("Press Enter to continue...")
        return success
        
    def login(self):
        self.clear_screen()
        print("\n=== User Login ===")
        
        username = input("Username: ")
        password = input("Password: ")
        
        success, message = self.user_manager.login(username, password)
        print(f"\n{message}")
        
        if not success and "Username not found" in message:
            print("Would you like to register first?")
            if input("Enter 'y' to register: ").lower() == 'y':
                return self.register()
        
        input("Press Enter to continue...")
        return success
        
    def run(self):
        while True:
            self.clear_screen()
            self.display_main_menu()
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == '1':
                if self.register():
                    print("\nPlease login with your new account.")
                    
            elif choice == '2':
                if self.login():
                    self.library_ui.run()
                    
            elif choice == '3':
                print("\nThank you for using the Library Management System!")
                break
                
            else:
                print("\nInvalid choice. Please try again.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    system = MainSystem()
    system.run()