# Password Manager

## Intro

This project is a simple command-line application used to store and retrieve passwords using AWS Secrets Manager. 

The application allows the user to: 

- Store a user ID and a password as a secret in Secrets Manager.
- List the amount of stored secrets.
- Retrieve a secret by storing in a file.
- Delete a secret.

All using the command-line of their terminal.

## About

The main purpose of this project has been for the author to demonstrate some of his functional programming skills, his ability to write high quality unit tests, and to display his understanding of automation and deployment using a Makefile and a GitHub Actions CI/CD Workflow.

## Prerequisites

Before setting up and running this password manager application, ensure you have the following installed and configured:

- Python 3.13 (recommended latest stable version)

    Check if Python is installed: 
```bash
  python --version
```

If not installed, download it from [python.org](https://www.python.org/downloads/).

- pip (Python package manager)

    Check if pip is installed: 
```bash
  pip --version
```

If missing, install it:
```bash
  python -m ensurepip --default-pip
```

- AWS CLI (for interacting with AWS password manager):

  Check installation:
```bash
  aws --version
```

If missing, install from [AWS CLI docs](https://aws.amazon.com/cli/).

- AWS credentials (IAM user with necessary permissions):

  Configure credentials using:
```bash
  aws configure
```

## Run Locally

Fork the repo from https://github.com/TorSatherley/password-manager

Clone the project:

```bash
  git clone https://github.com/TorSatherley/password-manager
```

Go to the project directory:

```bash
  cd password-manager
```

Create a new Virtual Environment (recommended):

```bash
  python -m venv venv
```

Activate venv:
```bash
  source venv/bin/activate  # On Linux/macOS
  venv\Scripts\activate  # On Windows
```

Install dependencies

```bash
  pip install -r requirements.txt
```

You can now utilise the Makefile to automate several processes. In the command line run:

```bash
  make dev-setup
  make run-checks
```
to automate the processes of using:
 - bandit to check for common security issues in Python
 - pip-audit to audit the Python environment for packages with known vulnerabilities
 - black to check for Python PEP 8 compliance
 - pytest to check all unit-tests are running and passing
 - pytest coverage to ensure the test coverage over all Python files exceeds 90%

### Using Password Manager

To actually use the Password Manager application, from the root of the repository run:

```bash
  export PYTHONPATH=$(pwd)
```
to allow Python to access all files in this repository, and then run:

```bash
  python src/password_manager.py
```

to start the application in the command line. Follow the instruction printed to the terminal to enter, retrieve, delete or list secrets in your AWS secrets account, and then press x to exit the application.

## CI/CD

This project has been designed to be maintained using continuous integration and continuous deployment - specifically using GitHub actions. This enables seamless updates of the project into the production environment, and runs all of the same checks as the 'make run-checks' command.

To test this, make a branch of your forked version of the repo, make a change and then merge it with main. Check the "Actions" tab on this repo on your GitHub account to see all unit tests and compliance checks run automatically within the workflow.

## Author

Tor Satherley
