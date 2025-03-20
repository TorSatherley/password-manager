# Password Manager

## Intro

This project is a simple command-line application used to store and retrieve passwords using AWS Secrets Manager. 

The application allows the user to: 

- Store a user ID and a password as a secret in Secrets Manager.
- List the amount of stored secrets.
- Retrieve a secret by storing in a file.
- Delete a secret.

All using the command-line of their terminal.

## Purpose

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

