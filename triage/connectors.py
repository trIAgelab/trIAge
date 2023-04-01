import re
import github
import getpass
import pandas
from abc import ABC, abstractmethod
import textwrap


class RepoConnector(ABC):
    pass


class GitHubConnector(RepoConnector):
    def __init__(self, access_token):
        self.access_token = access_token
        self.github = github.Github(self.access_token)
        self.repo = None

    def _parse_repo_url(self, url):
        repo_pattern = r"https?://github.com/([^/]+)/(.+)"
        match = re.match(repo_pattern, url)
        if match:
            return match.groups()
        else:
            return None
        
    def connect_repo(self, repo_url):
        """ Connect to a GitHub repository"""
        repo_info = self._parse_repo_url(repo_url)
        if repo_info:
            owner, repo_name = repo_info
            print(repo_info)
        else:
            print("Invalid repository URL")
            return

        # Get the repository object
        self.repo = self.github.get_repo(f"{owner}/{repo_name}")
        return self


    def get_issues(self, state="all"):
        if self.repo is None:
            print("Please connect to a repository first")
            return

        # Retrieve all issues
        issues = self.repo.get_issues(state=state)

        return list(issues)
    
    def get_issue(self, issue_number):
        if self.repo is None:
            print("Please connect to a repository first")
            return

        issue = self.repo.get_issue(issue_number)
        return issue
    
    def get_readme(self, words=None):
        readme = self.repo.get_readme()
        text = readme.decoded_content.decode("utf-8")
        if words:
            text = textwrap.shorten(text, width=words)
        return text
    

    def get_issue_events(self, issue):
        if self.repo is None:
            print("Repository not set")
            return

        if isinstance(issue, int):
            issue_number = issue
            issue = self.repo.get_issue(issue_number)

        comments = list(issue.get_comments())
        events = list(issue.get_events())

        return comments, events
