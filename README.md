
<br />
<div align="center">
  <h1>trIAge</h1>



  <p><b>An AI assistant for open source communities</b></p>


<div align="center">
<img src="https://c.tenor.com/I6kN-6X7nhAAAAAj/loading-buffering.gif" width=32 />
</div>

<div align="left">


# About

## Target Functionality

- Support: answer questions based on documentation, generate explanatory code examples
- Issue Quality Control: analyze issues for quality of description and reproducibility, provide feedback for improvement
- Issue Triage: Automatically categorize issues by content (feature request, bug, support) and tag them, detect duplicates, prioritize issues (e.g. security issues), link related issues
- Debugging: Analyze error causes, generate solution suggestions
- Testing: automatic generation of test cases based on issues
- Pull Request Review: Analysis of pull requests regarding code quality, code style, documentation, test coverage, etc.
- Documentation: Generation of documentation proposals from the project context
- Changelogs: Generation of changelogs from the project history


## Demo

The following is a dialog demo:

> **@trIAge Who are you and what can you do?**


> Hello! I am trIAge, a helpful bot designed to assist users and maintainers of open source projects. I am capable of assessing and rating the quality of issues, giving suggestions on how to improve the quality of issues, pointing users to relevant documentation and other resources, and suggesting solutions to issues. 

<br>

> **See this repository: https://github.com/tatsu-lab/stanford_alpaca**


> Thank you for providing me with that information. How may I assist you with the stanford_alpaca repository?

<br>

> **What do you know about this repo?**

> This repository is called stanford_alpaca, and it contains code and documentation to train Stanford's Alpaca models and generate data. The Alpaca project is an instruction-following LLaMA model, which stands for Latent language learners and models from ambiguity. 

<br>

> **See [this issue](https://github.com/tatsu-lab/stanford_alpaca/issues/63)**

> This issue, labeled as empty and filed by user jordancole21, requests support for a specific model, gpt-3.5-turbo, in the data generator. It seems that the user is asking for a new feature to be added to the tool. However, it is not clear whether such support is already available or planned for implementation. 


<br>

> **"Rate the issue quality on a scale from 0 to 10**

> Based on the information provided, I would rate the issue quality as a 7 out of 10. While the issue is clear and concise, it lacks some details such as the desired functionality and use case for the requested feature.

<br>

> **Respond to the user with suggestions to make the issue a 10**

> Hi @jordancole21, thank you for submitting this issue! To make it easier for maintainers to understand your request, it would be helpful to provide some additional details. Specifically, it would be good to know how the gpt-3.5-turbo model would be used with the data generator, and what sorts of functionality you would like the new version of the data generator to have. Additionally, if there are any relevant research or use cases that might inform the desired functionality of the new feature, please share those as well. The more information and context you can provide, the better we can evaluate your request and create a solution that meets your needs.


<br>

> **Suggest how to resolve the issue**

> Based on the information provided, it seems that the user is requesting a new version of the data generator that is compatible with the gpt-3.5-turbo model. Here is a possible way to resolve the issue:
>1. Research the capabilities of the gpt-3.5-turbo model and determine what modifications would need to be made to the existing data generator to support this model.
>2. Based on the research, develop a set of requirements for the new version of the data generator that would support the gpt-3.5-turbo model.
>3. Implement the necessary modifications to the data generator code to support the new model, ensuring that the new code meets the requirements developed in step two.
>4. Test the new version of the data generator with the gpt-3.5-turbo model, and make any necessary adjustments to ensure that the generated data meets the desired quality > standards.
> 5. Release the new version of the data generator as an update to the existing code base, including thorough documentation about the changes made and the requirements for use.
> 


# Setup

1. Clone the repository
2. Install the dependencies from `requirements.txt`
3. Obtain a GitHub API token and store it in the first line of a file called `secrets/github_token.txt` 
4. Obtain an OpenAI API token and store it in the first line of a file called `secrets/openai_token.txt`
  
#  Prototype Test

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

