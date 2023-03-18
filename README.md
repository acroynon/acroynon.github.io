# acroynon's devlog

This is a static site generated using Pelican (Python) to hold content for my personal devlog.

# Requirements

- Python 3.+
- Pip

# How to Run Locally

## Windows 
```bash
## Create venv
python -m venv env
## Activate venv
.\Scripts\activate.ps1
## Install requirements
pip install pipreqs
```

## Unix/Mac
```bash
## Create venv
python -m venv env
## Activate venv
source env/bin/activate
## Install requirements
pip install pipreqs
```

## Generate and Run
```bash
## Build and serve
invoke build serve
## Or run live reload
invoke livereload
```

# How to Publish to Github Pages

This will generate the site and push the static content to the remote gh-pages branch.

```bash
invoke publish
```
