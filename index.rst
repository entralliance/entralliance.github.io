.. entr_docs documentation master file, created by
   sphinx-quickstart on Tue Jun  7 16:38:12 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ENTR Alliance Renewable Energy Data Environment
===============================================

.. ::

    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

The ENTR data environment is a distribution of existing tools, frameworks, and standards, packaged together to enable efficient analysis of operational wind energy data. The ENTR environment consists of the ENTR warehouse, ENTR runtime, and OpenOA operational analysis Python package, all integrated into an easy-to-run Docker container. These components are provided as separate repositories maintained by the ENTR Alliance.

* The `ENTR warehouse <https://github.com/entralliance/entr_warehouse>`_ is an environment for building data stores for operational wind plant data. The ENTR warehouse provides an open foundation for data analysis, on which methods can be built and standardized. The warehouse includes computational resources and queryable database tables for each type of wind plant data (e.g., supervisory control and data acquisition (SCADA), revenue meter), using standard ENTR data schema.

* The `Open Operational Assessment (OpenOA) Python package <https://github.com/entralliance/OpenOA>`_ is used within the ENTR environment to perform operational assessments of wind plants using data stored in the ENTR warehouse. OpenOA consists of modules for organizing different types of data (e.g., revenue meter, SCADA, meteorological tower, and reanalysis), low-level data analysis toolkits (e.g., filtering, power curve fitting), and high-level operational assessment methods (such as long-term energy production estimation). OpenOA is maintained and primarily developed by the National Renewable Energy laboratory (`more information <https://www.nrel.gov/wind/openoa.html>`_).

* The `ENTR runtime <https://github.com/entralliance/entr_runtime>`_ provides the set of open-source technologies required to implement the ENTR warehouse. The runtime bundles the required set of data models and datasets, as well as OpenOA, and provides a sandbox environment enabling analysts and developers in the ENTR ecosystem to get started quickly. For example, analysts can perform operational assessments with OpenOA using example wind plant data, and developers can start customizing the data transformations in the ENTR warehouse.

* The `ENTR Docker containiner <ghcr.io/entralliance/entr_runtime>`_ provides a stable, predictable container in which the ENTR environment can be deployed in a “write once, run anywhere” way. Docker is a cross-platform containerization software that has become the de facto standard for deploying self-contained software environments and services for virtually any computer application. The Docker container bundles the ENTR warehouse (including data for an example wind plant), ENTR runtime, OpenOA, and any other dependencies as a platform-independent executable. 

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install.rst
   openoa_examples.rst
   data_integration.rst
   production_deployment.rst
   contributing.rst
   troubleshooting.rst

..
   Once Pandoc issue is fixed for the github actions, add the following to the toctree above after install.rst: examples_combined

..
   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
