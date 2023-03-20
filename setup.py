from setuptools import setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="triage",
    description="A helpful bot assisting users and maintainers of open source projects.",
    version="0.1",
    packages=["triage"],
    install_requires=requirements,
)
