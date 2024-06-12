import requests

def get_pull_requests(owner, repo, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    headers = {
        'Authorization': f'token {token}'
    }
    params = {
        'state': 'all'
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error: {response.status_code} - {response.text}')

def get_file_changes(owner, repo, pull_request_number, token):
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{pull_request_number}/files'
    headers = {
        'Authorization': f'token {token}'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        file_changes = response.json()
        file_names = [file['filename'] for file in file_changes]
        return file_names
    else:
        raise Exception(f'Error: {response.status_code} - {response.text}')

def add_comment_to_pull_request(owner, repo_name, pull_request_number, comment, access_token):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/issues/{pull_request_number}/comments"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "body": comment
    }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        return True
    else:
        print(f"Failed to add comment: {response.status_code} - {response.text}")
        return False
