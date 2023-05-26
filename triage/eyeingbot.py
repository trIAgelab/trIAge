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


run_app(
    name=BOT_NAME,
    version='0.0.1',
    url='https://github.com/apps/eyeingbot',
)
