import json


def parse_embedded_json(data):
    """
    Function to parse any embedded JSON structures in the retrieved data.
    Returns the data with embedded JSON structures parsed into dictionaries.
    """
    for item in data:
        # Check if the item has any fields with embedded JSON structures
        for key, value in item.items():
            if isinstance(value, str):
                try:
                    # Try parsing the value as JSON
                    parsed_json = json.loads(value)
                    # Update the item's field with the parsed JSON
                    item[key] = parsed_json
                except json.JSONDecodeError:
                    pass  # Ignore if the value cannot be parsed as JSON
    return data

def add_computed_status(posts):
    """
    Function to add a computed status field to posts based on their length.
    Adds a 'status' field to each post indicating if it is 'lengthy' or 'concise'.
    """
    for post in posts:
        if len(post['body']) > 100:
            post['status'] = 'lengthy'
        else:
            post['status'] = 'concise'
    return posts

def combine_posts_with_users(posts, users):
    """
    Function to combine posts with user details based on the userId field.
    Returns enriched post records with user details included.
    """
    enriched_posts = []
    for post in posts:
        user_id = post['userId']
        # Find the corresponding user details using userId
        user_details = next((user for user in users if user['id'] == user_id), None)
        if user_details:
            # Combine post with user details
            enriched_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body'],
                'status': post['status'],  # Assuming status field is already added
                'user': user_details
            }
            enriched_posts.append(enriched_post)
    return enriched_posts

