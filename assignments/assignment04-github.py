# assignment04-github.py
# Program that commits & pushes changes on file to github repo.
# Author: Eoghan Walsh
# References:
# [1] https://pygithub.readthedocs.io/en/stable/introduction.html
# [2]

from github import Github
from github import Auth
from config import config as cfg
import requests

# api key
auth = Auth.Token(cfg["githubkey"])

# github instance
g = Github(auth=auth)

for repo in g.get_user().get_repos():
    print(repo.name)

repo = g.get_repo("eoghanpw/")