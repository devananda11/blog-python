import pickle
import os

BLOG_DATA_FILE = 'blog_data.pkl'

def load_blogs():
    if os.path.exists(BLOG_DATA_FILE):
        with open(BLOG_DATA_FILE, 'rb') as f:
            return pickle.load(f)
    return {}

def save_blogs(blogs):
    with open(BLOG_DATA_FILE, 'wb') as f:
        pickle.dump(blogs, f)

def create_post(user, title, content):
    blogs = load_blogs()
    if user not in blogs:
        blogs[user] = []
    
    blogs[user].append({'title': title, 'content': content})
    save_blogs(blogs)
    print("Post created successfully.")

def delete_post(user, title):
    blogs = load_blogs()
    if user in blogs:
        for i, post in enumerate(blogs[user]):
            if post['title'] == title:
                del blogs[user][i]
                save_blogs(blogs)
                print("Post deleted successfully.")
                return
        print("Post not found.")
    else:
        print("No posts for this user.")

def modify_post(user, old_title, new_title, new_content):
    blogs = load_blogs()
    if user in blogs:
        for post in blogs[user]:
            if post['title'] == old_title:
                post['title'] = new_title
                post['content'] = new_content
                save_blogs(blogs)
                print("Post modified successfully.")
                return
        print("Post not found.")
    else:
        print("No posts for this user.")

def read_posts(user):
    blogs = load_blogs()
    if user in blogs:
        if blogs[user]:
            for post in blogs[user]:
                print(f"Title: {post['title']}")
                print(f"Content: {post['content']}\n")
        else:
            print("No posts for this user.")
    else:
        print("User not found.")
