# assignment04-github.py
# Program that updates file and commits & pushes changes to github repo.
# Author: Eoghan Walsh
# References:
# [1] https://pygithub.readthedocs.io/en/stable/introduction.html
# [2] https://pygithub.readthedocs.io/en/stable/examples/Repository.html#get-a-specific-content-file
# [3] https://pygithub.readthedocs.io/en/stable/examples/Repository.html#update-a-file-in-the-repository

from github import Github
from github import Auth
from config import config as cfg
import requests

# api key
auth = Auth.Token(cfg["githubkey"])  # Ref[1]

# create github instance
g = Github(auth=auth)

# get content file
filename = "assignment04.txt"
repo = g.get_repo("eoghanpw/WSAA-coursework")  # Ref[2]
contents = repo.get_contents("assignments/" + filename)

# get the file contents
url = contents.download_url
response = requests.get(url)
file_contents = response.text
print(f"Existing content: {file_contents}")

# update file contents
name1 = "Andrew"
name2 = "Eoghan"

if file_contents.find(name1) == -1:
    updated_contents = file_contents.replace(name2, name1)
else:
    updated_contents = file_contents.replace(name1, name2)

print(f"Updated content: {updated_contents}")

# update file and commit to github  Ref[3]
github_response = repo.update_file(contents.path,
                                   f"update name in {filename} with prog",
                                   updated_contents, contents.sha)

print(github_response)
