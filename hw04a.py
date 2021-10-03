import requests
import json
import numpy as np

def getGitInfo(_id: str) -> dict:

    req = requests.get(f'https://api.github.com/users/{_id}/repos')

    repo_list = json.loads(req.text)

    repo_info = {}
    for repo in repo_list:
        repo_name = repo['name']
        commit_req = requests.get(f'https://api.github.com/repos/{_id}/{repo_name}/commits')
        commit_lst = json.loads(commit_req.text)

        repo_info[repo_name] = len(commit_lst)
    
    return repo_info


if __name__ == "__main__":

    user = input("Enter the username of your GitHub account: ")

    gitInfo = getGitInfo(user)
    print(f'Github User ID: {user}')
    for key, val in gitInfo.items():
        print(f'Repo: {key}, Number of Commits: {val}')