import re
import os
import openai
from octomachinery.app.server.runner import run as run_app
from octomachinery.routing import process_event_actions
from octomachinery.routing.decorators import process_webhook_payload
from octomachinery.runtime.context import RUNTIME_CONTEXT

BOT_NAME = "trIAge"
MODEL_NAME = "gpt-4.0-turbo"

def set_api_key():
    api_key = os.getenv('OPENAI_KEY')
    if not api_key:
        raise ValueError("Missing OpenAI API key!")
    openai.api_key = api_key

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
    if re.search(r'\@{}\b'.format(BOT_NAME), comment['body']):
        comment_reactions_api_url = f"{comment['url']}/reactions"
        await github_api.post(
            comment_reactions_api_url,
            preview_api_version="squirrel-girl",
            data={"content": "eyes"},
        )

        # Get issue details
        issue_api_url = issue['url']
        issue_details = await github_api.get(issue_api_url)
        issue_title = issue_details['title']
        issue_description = issue_details['body']
        issue_tags = [label['name'] for label in issue_details['labels']]

        # Get repository details
        repo_name = repository['name']
        repo_description = repository['description']

        # Get comments details
        comments_api_url = f"{issue_api_url}/comments"
        comments = await github_api.get(comments_api_url)
        comments_data = [
            {'text': comment['body'], 'author': comment['user']['login']}
            for comment in comments
            if comment['id'] != comment['id']  # Exclude the triggering comment
        ]

        # Construct issue data
        issue_data = {
            'title': issue_title,
            'description': issue_description,
            'tags': issue_tags,
            'repository': {
                'name': repo_name,
                'description': repo_description
            },
            'comments': comments_data
        }

        # Generate the GPT-4 metaprompt
        issue_metaprompt = generate_metaprompt(issue_data)

        # Triggering comment as the user prompt
        user_prompt = comment['body']
        
        # Create a chat history for the GPT-4 chat model
        chat_history = [
            {"role": "system", "content": issue_metaprompt},
            {"role": "user", "content": user_prompt},
        ]

        # Generate a response using GPT-4
        completion = openai.ChatCompletion.create(
            model=MODEL_NAME,
            messages=chat_history
        )
        response = completion.choices[0].message['content']

        # Post the response as a comment to the issue
        issue_comments_api_url = f"{issue['url']}/comments"
        await github_api.post(
            issue_comments_api_url,
            data={"body": response},
        )

def generate_metaprompt(issue_data):
    """
    Generate a metaprompt (system-level prompt) for the chat model from the issue details.

    This function takes in a dictionary of issue details, including the issue title, description, tags, 
    repository information, and comments. It then constructs a metaprompt, a system-level message 
    providing context for the model about the issue being addressed. The metaprompt includes details 
    such as the issue title, repository name, tags associated with the issue, and the history of comments 
    on the issue.
    """
    prompt = (
        f"Issue titled '{issue_data['title']}' was raised in the repository '{issue_data['repository']['name']}' which is described as '{issue_data['repository']['description']}'. "
        f"The issue is tagged with {', '.join(issue_data['tags'])} and its description reads as follows: '{issue_data['description']}'. "
        "Here are the comments on the issue:\n"
    )
    for idx, comment in enumerate(issue_data['comments'], 1):
        prompt += f"\nComment {idx} by {comment['author']}: {comment['text']}\n"
    return prompt

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
set_api_key()

run_app(
    name=BOT_NAME,
    version='0.0.1',
    url='https://github.com/apps/triage-bot-app',
)
