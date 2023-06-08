This repository contains the documentation for ENTR.
View the documentation at [entralliance.github.io](https://entralliance.github.io)

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

### Overriding External Repo Branches

If you want to change the branches from which external files are retrieved, you can specify environment variables in your `make` command to override defaults. For example:
```
make html ENTR_WAREHOUSE_GITBRANCH="0.0.1"
```

You can also optionally change all of the default branches used to their development branches by specifying the `DEFAULT_GITBRANCH` environment variable when building the docs. For example, the following would use the "dev" branches for all external repos except for `dbt-entr`:
```
make html DEFAULT_GITBRANCH="dev" DBT_ENTR_GITBRANCH="0.0.2"
```

## Github Actions Publishing

This documentation is automatically built and served through Github Pages using the `gh_pages` branch. This is configured in `.github/workflows/gh-pages-deploy.yml`

View the documentation live at [entralliance.github.io](https://entralliance.github.io)
