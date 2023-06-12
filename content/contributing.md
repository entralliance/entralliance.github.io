Contributing Guidelines
=======================

## Issue Tracking

New feature requests, changes, enhancements, non-methodology features, and bug reports can be filed as new issues in the
[GitHub.com issue tracker](https://github.com/entralliance/entr_runtime/issues) at any time. Please be sure to fully describe the
issue.

<!---For other issues, please email the ENTR distribution list at `xx`.--->

## Repository

The entr_runtime and entr_warehouse repositories are hosted on GitHub, and located here: https://github.com/entralliance/entr_runtime and https://github.com/entralliance/entr_warehouse

These repositories are organized using a modified git-flow system. Branches are organized as follows:

- master: Stable release version. Must have good test coverage and may not have all the newest features.
- dev: Development branch which contains the newest features. Tests must pass, but code may be unstable.
- feature/xxx: Branch from dev, should reference a GitHub issue number.

To work on a feature, please fork entr_runtime or entr_warehouse first. Then clone your fork locally when you are ready to get to work. If your git status is unclean after you clone  (e.g., lots of untracked files and changes), chances are you are dealing with a Unicode normalization issue (specifically, the Unicode decomposition of filenames under macOS). This can be an issue on projects with contributors using a mix of MacOS, Linux, and Windows. To resolve it, delete your clone. Then issue `git config --global core.precomposeunicode true` and clone your fork again.

Once you have successfully cloned your fork, create a feature branch from the dev branch. Work out of this feature branch and push changes to your fork before submitting a pull request.
Be sure to periodically synchronize the upstream dev branch into your feature branch to avoid conflicts in the pull request. GitHub will prompt you to create a pull request back to the original project after the first push from your feature branch to your fork. You can continue to iterate on your feature branch until you are ready to submit your pull request.

When the feature branch is ready, make a pull request to entralliance/entr_runtime or entralliance/entr_warehouse through the GitHub.com UI. 

<!-- You will need to accept the Contributor License Agreement(CLA) for pull requests greater than 20 lines in length. [CLA Language](. . . ) -->

<!---[![CLA assistant](https://cla-assistant.io/readme/badge/IEA-Task-43/digital_wra_data_standard)](https://cla-assistant.io/IEA-Task-43/digital_wra_data_standard) *need to update-->


## Pull Request

Pull requests must be made for any changes to be merged into release branches.
They must include updated documentation and pass all unit tests and integration tests.
In addition, code coverage should not be negatively affected by the pull request.

**Scope:** Encapsulate the changes of ideally one, or potentially a couple, issues.
It is greatly preferable to submit three small pull requests than it is to submit one large pull request.
Write a complete description of these changes in the pull request body.

**Tests:** Coming soon

<!--For any changes to the JSON schema, the contributor should

* Make sure that the changes result in a valid JSON schema
* Adjust the [demo file](https://github.com/IEA-Task-43/digital_wra_data_standard/blob/master/demo_data/iea43_wra_data_model.json) to reflect the changes
Tools like [jsonschemavalidator](https://www.jsonschemavalidator.net/) can help with these tasks-->



**Documentation:** Document any relevant changes using inline documentation. If relevant, please also update the RST files located in the ENTR documentation repository to describe code enhancements or new features: https://github.com/entralliance/entralliance.github.io.

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


## New Tag Names

The dbt-entr package contains a list of approximately 2500 data tag names ([available here](https://github.com/entralliance/dbt-entr/blob/main/seeds/seed_entr_tag_list.csv)). Most of these tag names describe wind turbine SCADA data channels based on the IEC 61400-25 standard obtained from [SCADA International](https://scada-international.com). However, there may be data channels that are missing from this list. If you would like to include new data channels in the ENTR data stack, please submit a pull request to the [dbt-entr repository](https://github.com/entralliance/dbt-entr/) with the proposed new tag names added to the end of the [current list of tage names](https://github.com/entralliance/dbt-entr/blob/main/seeds/seed_entr_tag_list.csv). 

ENTR tage names should be of the form {Logical Node}.{Sensor Name}, where the logical node indicates the category to which the data belong (e.g., WMET for meteorological information and WROT for rotor information) and the sensor name describes the specific channel (e.g., HorWdSpd for horizontal wind speed and RotSpd for rotor speed). When possible, for wind energy data, logical nodes and sensor names defined in the IEC 61400-25-2 standard should be used. However, logical nodes and sensor names from other IEC standards (e.g., IEC 61850 - Communication Networks and Systems for Power Utility Automation) can be used as well. For example, the ENTR tag list uses the logical node MMTR from the IEC 61850 standard to represent the revenue meter. If you cannot find an existing logical node or sensor name for a new tag name, you may create a new name, which should be based on existing names as much as possible. For example, to represent reanalysis weather data, the ENTR tag list uses the WMETR logical node, which is based on the existing WMET logical node; to indicate the U and V components of horizontal wind speed, the sensor names HorWdSpdU and HorWdSpdV, which are based on the existing HorWdSpd sensor name, are used.

When contributing a new tag name to the ENTR tag list, the following fields should be specified: the ENTR tag ID, the tag subtype ID (if a tag name can correspond to multiple data channels), the ENTR tag name, the tag subtype description (if applicable), the logical node, the sensor name, the full tag name description, and the units.