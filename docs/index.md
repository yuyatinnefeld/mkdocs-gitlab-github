# Welcome to mkdocs / mkdocstrings

MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation.
Documentation source files are written in Markdown, and configured with a single YAML configuration file.


## Setup Mkdocs Environment
```bash
# install mkdocs and project relevant python packages
pip install -r requirements.txt

# create mkdocs files
mkdocs new .

# edit mkdocs file
vi ./mkdocs.yml

# edit docs/index.md
vi docs/index.md

# create a python script which generates the markdown files and nav automatically
# source: https://github.com/oprypin/mkdocs-gen-files
touch docs/gen_mkdocs_pages.py

```

## Start MkDocs
```bash

# see the documenation
mkdocs serve

# build mkcods file
mkdocs build

# verify
ls public

# deploy your documentation thought the Gitlab CICD Pipeline
git push origin master
```