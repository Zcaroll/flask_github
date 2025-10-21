# TODO make requests to github API

import requests
import logging

def get_github_user(username):

    # return a tuple of (data, error)
    # if it works return (data, None)

    # if it fails, or there is an error return (None, error)

    try:
        response = requests.get(f'https://api.github.com/users/{username}') # github user API
        if response.status_code == 404: # not found. 
            return None, f'Username {username} not found'
        response.raise_for_status()  # throw an exception for 500 errors(where github's server isnt working)
        response_json = response.json()
        user_info = extract_user_info(response_json)
        return user_info, None # return data, error
    except Exception as e:
        logging.exception(e)
        return None, 'Error connecting to GitHub'

# method for extracting useful info from github API response
def extract_user_info(json_response):
    # extract useful info from github_data dict
    return {
        'login': json_response.get('login'),
        'name': json_response.get('name'),
        'avatar_url': json_response.get('avatar_url'),
        'home_page': json_response.get('html_url'),
        'repos': json_response.get('public_repos'),
    }