""" This is a test bot for GitHub based on the octomachinery library."""
import re

from octomachinery.app.server.runner import run as run_app
from octomachinery.routing import process_event_actions
from octomachinery.routing.decorators import process_webhook_payload
from octomachinery.runtime.context import RUNTIME_CONTEXT

# Define the bot's name
BOT_NAME = "eyeingbot"

@process_event_actions("issue_comment", {"created"})
@process_webhook_payload
async def on_comment(
    *,
    action,
    issue,
    comment,
    repository=None,
    sender=None,
    installation=None,
    assignee=None,
    changes=None,
    organization=None,
):
    github_api = RUNTIME_CONTEXT.app_installation_client
   # Check if the bot was mentioned in the comment using a regex
    if re.search(r'\@{}\b'.format(BOT_NAME), comment['body']):
        comment_reactions_api_url = f"{comment['url']}/reactions"
        await github_api.post(
            comment_reactions_api_url,
            preview_api_version="squirrel-girl",
            data={"content": "eyes"},
        )

        # Collect issue name, description, and all comment history
        # issue_api_url = issue['url']
        # issue_details = await github_api.get(issue_api_url)
        # issue_name = issue_details['title']
        # issue_description = issue_details['body']

        # comments_api_url = f"{issue_api_url}/comments"
        # comments = await github_api.get(comments_api_url)

        # issue_data = {
        #     'name': issue_name,
        #     'description': issue_description,
        #     'comments': [
        #         {'id': comment['id'], 'body': comment['body'], 'user': comment['user']['login']}
        #         for comment in comments
        #     ],
        # }

        await github_api.post(
            comments_api_url, 
            data={'body': "I have read the issue."}
        )

        

        



run_app(
    name=BOT_NAME,
    version='0.0.1',
    url='https://github.com/apps/eyeingbot',
)
