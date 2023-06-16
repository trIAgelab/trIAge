import re
from octomachinery.app.server.runner import run as run_app
from octomachinery.routing import process_event_actions
from octomachinery.routing.decorators import process_webhook_payload
from octomachinery.runtime.context import RUNTIME_CONTEXT


class EyeingBot:
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
