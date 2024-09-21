import requests
import base64

# GitHub Personal Access Token (replace with your token)
GITHUB_TOKEN = 'your_github_token_here'
# Your GitHub Username
GITHUB_USER = 'botboy223'
# Repository Name
REPO_NAME = 'pythonwe'
# File to be created
FILE_PATH = 'README.md'
# Commit message
COMMIT_MESSAGE = 'first commit'
# Branch
BRANCH = 'main'

# GitHub API URL to create a repository
REPO_URL = f"https://api.github.com/user/repos"

def create_repo():
    """Create a new GitHub repository"""
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        "name": REPO_NAME,
        "private": False,  # Make the repository public or private
    }
    response = requests.post(REPO_URL, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Repository '{REPO_NAME}' created successfully!")
    else:
        print(f"Failed to create repository: {response.json()}")

def create_file_in_repo():
    """Create a file in the repository"""
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    
    # File content in base64 format
    content = base64.b64encode(b"# pythonwe\n").decode('utf-8')
    data = {
        "message": COMMIT_MESSAGE,
        "content": content,
        "branch": BRANCH,
    }
    response = requests.put(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"File '{FILE_PATH}' created successfully in '{REPO_NAME}'!")
    else:
        print(f"Failed to create file: {response.json()}")

if __name__ == '__main__':
    create_repo()
    create_file_in_repo()
