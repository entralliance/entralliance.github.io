Please read the following guidelines for how to contribute to the ENTR Foundation.

## Issue Tracking

New feature requests, changes, enhancements, non-methodology features, and bug reports can be filed as new issues in the in GitHub at any time.

Please search for through open issues the entralliance GitHub organization (type "user:entralliance type:issue state:open" with any additional search terms in the GitHub search bar)
to make sure your issue isn't already being worked on - if not, create a new issue in the appropriate repository.
If you're unsure about which repository to use, you can [create a new issue in this docs repo](https://github.com/entralliance/entralliance.github.io/issues/new/choose).

*Please be sure to fully describe any new issues.*

**Note:** it may be helpful to engage in a discussion before submitting a new issue on GitHub. We encourage opening conversations on Slack (see above) if you'd like to involve the community in the brainstorming effort before opening an issue!

## Code Contributions

The ENTR Foundation's free, open-source code repositories are hosted on GitHub in the [entralliance GitHub organization](https://github.com/entralliance).

Pull requests must be made for any changes to be merged into release branches. New pull requests will be reviewed and approved by the ENTR maintainers before they are merged.
They must include updated documentation and pass all unit tests and integration tests.
In addition, code coverage should not be negatively affected by the pull request.

### Submitting Pull Requests

To contribute code changes, please fork the repository first and clone your fork locally when you are ready to get to work.

**IMPORTANT NOTE**: you will need to sign the [Contributor License Agreement](https://docs.google.com/forms/d/e/1FAIpQLSe4Idku1IEvjEUqbxYby-vDI5BmESSJC0m1xeQUuEssRtODNQ/viewform?usp=sharing) before any proposed changes can be merged.

Once you have successfully cloned your fork, create a branch from the `dev` branch following the "other branches" naming conventions in the Branching Strategy section below. Work out of this feature branch and push changes to your fork before submitting a pull request.
Be sure to periodically synchronize the upstream dev branch into your feature branch to avoid conflicts in the pull request. When ready to submit your changes and open a pull request, GitHub will prompt you to create a pull request back to the original project after the first push from your feature branch to your fork. Please fill out the appropriate details in the pull request template (automatically generated for new pull requests). You can continue to iterate on your feature branch until you are ready to submit your pull request.

A good pull request should have the following components:

- **Scope:** the changes in the PR address ideally one, or potentially a couple of open GitHub issues.
It is greatly preferable to submit three small pull requests than it is to submit one large pull request.
Write a complete description of these changes in the pull request body.

- **Documentation:** Document any relevant changes using inline documentation. If relevant, please also update the README or other descriptive guideline fiels to describe code enhancements or new features.

- **Tests:** the changes made in the pull request are tested through unit and/or integration tests (included in the pull request). If you've foregone this step, please make note of it in the pull request description, and the ENTR maintainers may help add appropriate tests.

### Branching Strategy

The ENTR Foundation's repositories are organized using a modified git-flow system. Branches are generally organized as follows:

- `main`: Latest stable release. These branches must have good test coverage and may not have all the newest features.
- `dev`: Development branch which contains the latest features that are being staged for stable release (via merge into main). Tests must pass, but code may be unstable.
- other branches: branches containing candidate changes to be merged into dev. All pull requests opened by non-maintainers should target dev branches. These should typically resolve and open GitHub issue, which a contributor will be prompted to specify when creating a pull request (via our pull request templates). Naming conventions for "other" branches:
    - `feature/{description}`: indicates that a branch contains a new feature
    - `fix/{description}`: indicates that a branch contains a fix

### Troubleshooting Guidelines

If your git status is unclean after you clone your fork (e.g., lots of untracked files and changes), chances are you are dealing with a Unicode normalization issue, specifically, the Unicode decomposition of filenames under macOS. This can be an issue on projects with contributors using a mix of MacOS, Linux, and Windows. To resolve it, delete your local clone. Then issue `git config --global core.precomposeunicode true` and clone your fork again.

<!---[![CLA assistant](https://cla-assistant.io/readme/badge/IEA-Task-43/digital_wra_data_standard)](https://cla-assistant.io/IEA-Task-43/digital_wra_data_standard) *need to update-->

<!--For any changes to the JSON schema, the contributor should

* Make sure that the changes result in a valid JSON schema
* Adjust the [demo file](https://github.com/IEA-Task-43/digital_wra_data_standard/blob/master/demo_data/iea43_wra_data_model.json) to reflect the changes
Tools like [jsonschemavalidator](https://www.jsonschemavalidator.net/) can help with these tasks-->

<!-- **Changelog:** For pull requests that encapsulate a user-facing feature, or is significant to users of entr_runtime for some other reason, please add a line to CHANGELOG.md in the [Unreleased] section. -->

<!--- ## Documentation Style
TBD
Documentation is written using RST, and is located both inline and within the /sphinx directory.
Any changes to the analysis methodology should be discussed there or offline. Once a methodology change is decided,
create new tickets in this repository towards implementing the change.-->

<!--- ## Testing
TBD but may define guidelines for validating the schema
All code should be paired with a corresponding unit or integration test.
entr_runtime uses pytest and the built in unittest framework.
For instructions on running tests, please see the [Readme](testing link).-->


## Standard Tag Changes

The `dbt-entr` package contains a list of standard tag names ([available here](https://github.com/entralliance/dbt-entr/blob/main/seeds/seed_entr_tag_list.csv)). The initial set of standard tags were contributed [SCADA International](https://scada-international.com) and based on the IEC 61400-25 standard for wind power plants. However, there may be data channels that are missing from this list. If you would like to include new data channels in the ENTR data stack, please submit a pull request to the [dbt-entr repository](https://github.com/entralliance/dbt-entr/) with the proposed new tag names added to the end of the [current list of tage names](https://github.com/entralliance/dbt-entr/blob/main/seeds/seed_entr_tag_list.csv). 

ENTR tage names should be of the form {Logical Node}.{Sensor Name}, where the logical node indicates the category to which the data belong (e.g., WMET for meteorological information and WROT for rotor information) and the sensor name describes the specific channel (e.g., HorWdSpd for horizontal wind speed and RotSpd for rotor speed). When possible, for wind energy data, logical nodes and sensor names defined in the IEC 61400-25-2 standard should be used. However, logical nodes and sensor names from other IEC standards (e.g., IEC 61850 - Communication Networks and Systems for Power Utility Automation) can be used as well. For example, the ENTR tag list uses the logical node MMTR from the IEC 61850 standard to represent the revenue meter. If you cannot find an existing logical node or sensor name for a new tag name, you may create a new name, which should be based on existing names as much as possible. For example, to represent reanalysis weather data, the ENTR tag list uses the WMETR logical node, which is based on the existing WMET logical node; to indicate the U and V components of horizontal wind speed, the sensor names HorWdSpdU and HorWdSpdV, which are based on the existing HorWdSpd sensor name, are used.

When contributing a new tag name to the ENTR tag list, the following fields should be specified: the ENTR tag ID (a globally unique integer key for the tag), the tag subtype ID (if a tag name can correspond to multiple data channels), the ENTR tag name, the tag subtype description (if applicable), the logical node, the sensor name, the full tag name description, and the units.
