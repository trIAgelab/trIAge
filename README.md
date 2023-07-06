
<br />
<div align="center">
  <h1>trIAge</h1>

  [![License](https://img.shields.io/github/license/trIAgelab/trIAge?color=green&style=flat-square)](https://github.com/trIAgelab/trIAge/blob/main/LICENSE)


  <p><b>An AI assistant for open source communities</b></p>

<p align="center">
We develop trIAge, an AI-driven assistant that supports users, maintainers and contributors of open source projects. 
</p>

<div align="left">

# About

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





</div>

