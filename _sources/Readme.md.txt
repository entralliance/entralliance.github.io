This repository contains the content for the ENTR docs site, which can be viewed at [entralliance.github.io](https://entralliance.github.io)

# Docs Maintenance and Contributions

If you have any questions or find items within these docs that would benefit from further clarification, please open an issue here or start a conversation with us on our [Slack documentation channel](https://app.slack.com/client/TQYRQ0YR4/C05BHMZ3CLW). If you haven't already joined the ENTR Slack workspace, you can sign up [here](https://join.slack.com/t/entralliance/shared_invite/zt-1x6945h00-iDxalk2w9cHO~n2Dw4btyg).

To contribute to the ENTR docs, clone this repository, develop and build your changes locally (see below), and open a pull request targeting the main branch - these changes will be reviewed by the ENTR maintainers before being published.

## Local Development Quickstart

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

If you want to change the branches from which external files are retrieved, you can use any combination of the following options.

Note that these options are listed in order of precedence

#### Option 1: Specify during build

 specify environment variables in your `make` command to override defaults. For example:
```
make html ENTR_WAREHOUSE_GITBRANCH="0.0.1"
```

#### Option 2: Specify during build

One more option is to copy the .env_example into a .env file (`cp .env_example .env`) and populate it with variables you'd like to override.

#### Option 3: Set default branch for all external

You can also optionally change all of the default branches used to their development branches by specifying the `DEFAULT_GITBRANCH` environment variable when building the docs. For example, the following would use the "dev" branches for all external repos except for `dbt-entr`:

```
make html DEFAULT_GITBRANCH="dev" DBT_ENTR_GITBRANCH="0.0.2"
```

## Github Actions Publishing

This documentation is automatically built and served through Github Pages using the `gh_pages` branch. This is configured in `.github/workflows/gh-pages-deploy.yml`

View the documentation live at [entralliance.github.io](https://entralliance.github.io)
