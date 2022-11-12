# Welcome to mkdocs / mkdocstrings

MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation.
Documentation source files are written in Markdown, and configured with a single YAML configuration file.

## Example Docs Site

### Gitlab
- https://yuyatinnefeld.gitlab.io/mkdocs-gitlab-github/

### Github
- https://yuyatinnefeld.github.io/mkdocs-gitlab-github/

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

### Gitlab Docs Site

```bash
# check the page
<username>.<gitlab>.io/<your-mkdocs-repo>

# example gitlab site
https://yuyatinnefeld.gitlab.io/mkdocs-gitlab-github

# details about gitlab url
https://docs.gitlab.com/ee/user/project/pages/getting_started_part_one.html
```


### Github Docs Site

```bash
# setup gh-pages branch as source
repo > settings > pages
Source: Deploy from a branch
Branch: gh-pages + Selectfolder: root > Save

# check the page
<username>.<github>.io/<your-mkdocs-repo>

# example gitlab site
https://yuyatinnefeld.github.io/mkdocs-gitlab-github

# details about gitlab url
https://docs.gitlab.com/ee/user/project/pages/getting_started_part_one.html
```