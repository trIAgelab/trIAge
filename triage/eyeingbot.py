""" This is a test bot for GitHub based on the octomachinery library."""

from octomachinery.app.server.runner import run as run_app
from octomachinery.routing import process_event_actions
from octomachinery.routing.decorators import process_webhook_payload
from octomachinery.runtime.context import RUNTIME_CONTEXT


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
):
    github_api = RUNTIME_CONTEXT.app_installation_client
    comment_reactions_api_url = f"{comment['url']}/reactions"
    await github_api.post(
        comment_reactions_api_url,
        preview_api_version="squirrel-girl",
        data={"content": "eyes"},
    )


run_app(
    name='eyeingbot',
    version='0.0.1',
    url='https://github.com/apps/eyeingbot',
)
