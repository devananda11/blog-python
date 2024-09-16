import bcrypt
import pickle
import os

# File to store user data
USER_DATA_FILE = 'user_data.pkl'

def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'rb') as f:
            return pickle.load(f)
    return {}

def save_users(users):
    with open(USER_DATA_FILE, 'wb') as f:
        pickle.dump(users, f)

def register_user(username, password):
    users = load_users()
    if username in users:
        print("User already exists.")
        return False

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = hashed_password
    save_users(users)
    print("User registered successfully.")
    return True

def login_user(username, password):
    users = load_users()
    hashed_password = users.get(username)

    if hashed_password and bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        print("Login successful.")
        return True

    print("Invalid username or password.")
    return False
