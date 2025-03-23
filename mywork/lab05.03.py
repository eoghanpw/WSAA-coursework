from github import Github
from config import config as cfg
import requests

api_key = cfg["githubkey"]

g = Github(api_key)

for repo in g.get_user().get_repos():
    print(repo.name)

repo = g.get_repo("eoghanpw/aprivateone")
print(repo.clone_url)

file_info = repo.get_contents("test.txt")
url_of_file = file_info.download_url
print(url_of_file)

response = requests.get(url_of_file)
file_contents = response.text
print(file_contents)

new_contents = file_contents + "more stuff\n"

print(new_contents)

github_response = repo.update_file(file_info.path, "updated by prog",
                                   new_contents, file_info.sha)

print(github_response)
