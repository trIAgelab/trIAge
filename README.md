
<br />
<div align="center">
  <h1>trIAge</h1>



  <p><b>An AI assistant for open source communities</b></p>


<div align="center">
<img src="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif" width=32 />
</div>

<div align="left">


# About

We develop trIAge, an AI-driven assistant that supports users, maintainers and contributors of open source projects. 


Leveraging the capabilities of Large Language Models (LLMs), trIAge is able to analyze issues, discussions and pull requests on collaboration platforms (e.g. GitHub, GitLab) and provide users and maintainers with hints and suggested solutions by responding on the discussion thread. trIAge has access to the context of the project (code, documentation, guidelines) and can be configured by maintainers to become gradually active as needed. The bot automates part of the workload of maintainers and helps users to solve their issues faster, e.g. by automatically answering questions from documentation, or generating test cases for reported issues.  Current chat models like GPT-4 have shown remarkable abilities in the relevant natural language and code understanding tasks. This enables a wide range of automation with respect to issue triage, issue quality control, debugging, user support, testing and documentation. As an open-source project, we are aiming to eventually base the bot’s capabilities on emerging open-source models (e.g. Vicuna, Orca), whose capabilities are rapidly catching up to the current gold standard (GPT-4).


The MVP of trIAge can easily be deployed by open source maintainers on their repositories in the form of a GitHub app, which we host as a service for demonstration purposes. We also create the option for self-hosting of the application. We add a convenient user interface for maintainers to customize the desired capabilities and action triggers of the assistant. Subsequently we plan to support other code hosting platforms (e.g. GitLab) as well. 


## Target Functionality

- Support: answer questions based on documentation, generate explanatory code examples
- Issue Quality Control: analyze issues for quality of description and reproducibility, provide feedback for improvement
- Issue Triage: Automatically categorize issues by content (feature request, bug, support) and tag them, detect duplicates, prioritize issues (e.g. security issues), link related issues
- Debugging: Analyze error causes, generate solution suggestions
- Testing: automatic generation of test cases based on issues
- Pull Request Review: Analysis of pull requests regarding code quality, code style, documentation, test coverage, etc.
- Documentation: Generation of documentation proposals from the project context
- Changelogs: Generation of changelogs from the project history




  
#  Prototype Test

## Setup

1. Clone the repository
2. Install the dependencies from `requirements.txt`
3. Obtain a GitHub API token and store it in the first line of a file called `secrets/github_token.txt` 
4. Obtain an OpenAI API token and store it in the first line of a file called `secrets/openai_token.txt`

## Test

1. Instantiate the `trIAge` class

```python
from triage.bot import TrIAge, get_secret

trIAge = TrIAge(
    model_provider="openai",
    model_api_key=get_secret("openai_token"),
    hub_api_key=get_secret("github_token"),
)
````

1. Start sending messages to the bot

```python
trIAge.tell("Who are you and what can you do?")
````

2. Let the bot scan a Github repository.

```python
trIAge.see_repo("https://github.com/tatsu-lab/stanford_alpaca")
```

3. Get a GitHub issue from the repository an let the bot read it.

```python
issues = trIAge.get_issues()
an_issue = random.choice(issues)
trIAge.see_issue(an_issue)
````

4. Start asking the bot questions about the issue.

```python
trIAge.tell("Rate the issue quality on a scale from 0 to 10")
```




</div>

