# Blog Application

This is a terminal-based blog application implemented in Python. It allows users to create, delete, modify, and read blog posts. It includes user authentication with encrypted passwords, ensuring secure access to personal blogs.

## Features

- **User Registration**: New users can register by providing a username and password.
- **User Login**: Registered users can log in using their credentials.
- **Create Blog Post**: Users can create new blog posts with a title and content.
- **Delete Blog Post**: Users can delete existing blog posts by title.
- **Modify Blog Post**: Users can update the title and content of existing posts.
- **Read Blog Posts**: Users can view all their blog posts.

## Requirements

- Python 3.x
- `bcrypt` library for password hashing
- `pickle` for data storage

## Installation

1. **Clone the Repository**

   -First, clone the repository to your local machine using Git

2. **Install Dependencies**
   
   -pip install bcrypt

3.**Run the application**
   
   -python main.py

## Data Storage

-**User Data**: Stored in user_data.pkl using pickle, with passwords encrypted by bcrypt.
-**Blog Data**: Stored in blog_data.pkl under each user’s profile.

## File Overview

-**auth.py**: Contains functions for user registration and login, including password encryption and verification. It handles user authentication.

-**blog.py**: Manages blog posts, including creation, deletion, modification, and reading. It handles blog data storage and retrieval.

-**main.py**: The entry point of the application. It provides the terminal interface for users to interact with the blog system, handling user choices and invoking functions from auth.py and blog.py.
  
