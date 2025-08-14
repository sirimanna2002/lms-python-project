# user.py
import json
import re
from pathlib import Path

class User:
    def __init__(self, full_name, address, id_number, contact_number, email, username, password):
        self.full_name = full_name
        self.address = address
        self.id_number = id_number
        self.contact_number = contact_number
        self.email = email
        self.username = username
        self.password = password  # In production, this should be hashed
        
    def to_dict(self):
        return {
            'full_name': self.full_name,
            'address': self.address,
            'id_number': self.id_number,
            'contact_number': self.contact_number,
            'email': self.email,
            'username': self.username,
            'password': self.password
        }

class UserManager:
    def __init__(self):
        self.users_file = Path('users.json')
        self.users = self.load_users()
    
    def load_users(self):
        if self.users_file.exists():
            with open(self.users_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_users(self):
        with open(self.users_file, 'w') as f:
            json.dump(self.users, f, indent=4)
    
    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
    
    def validate_contact_number(self, number):
        pattern = r'^\+?1?\d{9,15}$'
        return re.match(pattern, number) is not None
    
    def register_user(self, full_name, address, id_number, contact_number, email, username, password):
        # Validation checks
        if username in self.users:
            return False, "Username already exists"
        
        if not self.validate_email(email):
            return False, "Invalid email format"
        
        if not self.validate_contact_number(contact_number):
            return False, "Invalid contact number format"
        
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
            
        # Create new user
        user = User(full_name, address, id_number, contact_number, email, username, password)
        self.users[username] = user.to_dict()
        self.save_users()
        return True, "Registration successful"
    
    def login(self, username, password):
        if username not in self.users:
            return False, "Username not found"
        
        if self.users[username]['password'] != password:
            return False, "Incorrect password"
            
        return True, "Login successful"