import re
from octomachinery.app.server.runner import run as run_app
from octomachinery.routing import process_event_actions
from octomachinery.routing.decorators import process_webhook_payload
from octomachinery.runtime.context import RUNTIME_CONTEXT


class EyeingBot:
    """
    A class representing a GitHub bot that reacts to comments on issues.

    This bot, when mentioned in a comment on an issue, responds by 
    reacting to the comment with "eyes" and posting a response stating 
    it has read the issue.
    """
    name = "eyeingbot"

    @process_event_actions("issue_comment", {"created"})
    @process_webhook_payload
    async def on_comment(
        self,
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
        """  
        Asynchronously responds to comments on issues where the bot is mentioned.

        This method is triggered when a comment is created on an issue. If the bot is 
        mentioned in the comment, it reacts to the comment with "eyes" and posts a 
        response stating it has read the issue.
        """
        github_api = RUNTIME_CONTEXT.app_installation_client
        if re.search(r"\@{}\b".format(self.name), comment["body"]):
            comment_reactions_api_url = f"{comment['url']}/reactions"
            await github_api.post(
                comment_reactions_api_url,
                preview_api_version="squirrel-girl",
                data={"content": "eyes"},
            )

            issue_comments_api_url = f"{issue['url']}/comments"
            await github_api.post(
                issue_comments_api_url,
                data={"body": "I have read the issue."},
            )


bot = EyeingBot()

run_app(
    name=bot.name,
    version="0.0.1",
    url="https://github.com/apps/eyeingbot",
)
