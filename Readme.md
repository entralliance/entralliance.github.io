This repository contains the documentation for ENTR.
View the documentation at [entralliance.github.io](entralliance.github.io)

## Quickstart

To develop and build docs locally, first install dependencies:

```
pip install -r requirements.txt
```

Then, (re)build the documentation:

```
make html
```

Finally, open the HTML that is built in `./_build/html/index.html` with your web browser.

## Github Actions Publishing

This documentation is automatically built and served through Github Pages using the `gh_pages` branch. This is configured in `.github/workflows/gh-pages-deploy.yml`

View the documentation live at [entralliance.github.io](entralliance.github.io)