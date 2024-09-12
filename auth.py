import json
from user import User
from account import Account
from message import Message

message = Message()

class Auth:
    def __init__(self):
        pass

    def login_again(self, username, password):
        with open('db.json', 'r') as file:
            users = json.load(file)['users']

# 2. Simplified logic to print the message only when necessary.
        for user in users:
            if user['name'] == username:
                if user['password'] == password:
                    message.print("Correct Password!")
                else:
                    message.print("Incorrect password")
            else:
                message.print("Username not found")
            
        return None