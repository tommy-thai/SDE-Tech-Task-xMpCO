import requests

def get_posts():
    """
    Function to retrieve data from the /posts endpoint of the JSONPlaceholder API.
    Returns a list of posts.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve posts. Status code: {response.status_code}")
        return []

def get_users():
    """
    Function to retrieve data from the /users endpoint of the JSONPlaceholder API.
    Returns a list of users.
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve users. Status code: {response.status_code}")
        return []
