import auth
import blog

def main():
    while True:
        print("\nBlog System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            auth.register_user(username, password)

        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if auth.login_user(username, password):
                while True:
                    print("\nBlog Menu")
                    print("1. Create Post")
                    print("2. Delete Post")
                    print("3. Modify Post")
                    print("4. Read Blog")
                    print("5. Logout")

                    choice = input("Enter your choice: ")

                    if choice == '1':
                        title = input("Enter post title: ")
                        content = input("Enter post content: ")
                        blog.create_post(username, title, content)

                    elif choice == '2':
                        title = input("Enter post title to delete: ")
                        blog.delete_post(username, title)

                    elif choice == '3':
                        old_title = input("Enter current post title: ")
                        new_title = input("Enter new post title: ")
                        new_content = input("Enter new post content: ")
                        blog.modify_post(username, old_title, new_title, new_content)
                    elif choice == '4':
                        blog.read_posts(username)

                    elif choice == '5':
                        print("Logging out...")
                        break
                    

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
