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

The `ENTR runtime <https://github.com/entralliance/entr_runtime>`_
----
The ENTR Runtime is a distribution of 
tools, frameworks, and standards relevant to wind energy data analysis,
packaged together in a Docker container to enable efficient and reproducible analysis workflows.
The ENTR runtime is based on Jupyter's Spark Notebook container, adding the ENTR warehouse, the OpenOA operational analysis Python package, and example data.
The runtime containerizes the required set of software to run ENTR warehouse and OpenOA methods within a single environment,
and it provides a sandbox environment enabling analysts and developers in the ENTR ecosystem to get started quickly.
For example, analysts can perform operational assessments with OpenOA using example wind plant data,
and developers can start customizing the data transformations in the ENTR warehouse.
The `ENTR Docker containiner <ghcr.io/entralliance/entr_runtime>`_ provides a unified analysis environment in
which the ENTR environment can be deployed in a “write once, run anywhere” and platform-independent way.
Docker is a cross-platform containerization software that has become the de facto standard for
deploying self-contained software environments and services for virtually any computer application.

The `ENTR warehouse <https://github.com/entralliance/entr_warehouse>`_
^^^^^
The ENTR Warehouse provides template Data Build Tool (DBT) macros and scripts to assist in building and orchestrating for operational wind plant data.
The ENTR warehouse provides an open foundation for data analysis, on which methods can be built and standardized.
The warehouse materializes database objects in the Spark database provided by the ENTR runtime for each type of wind plant data
(e.g., supervisory control and data acquisition (SCADA), revenue meter), using the standard ENTR data model,
which includes data transformations and table schema.

The `OpenOA Python package <https://github.com/entralliance/OpenOA>`_
^^^^^
OpenOA (Open Operational Assessment) is used within the ENTR environment to perform operational assessments of wind plants using data stored in the ENTR warehouse.
OpenOA consists of modules for organizing different types of data
(e.g., revenue meter, SCADA, meteorological tower, and reanalysis),
low-level data analysis toolkits (e.g., filtering, power curve fitting),
and high-level operational assessment methods (such as long-term energy production estimation).
OpenOA is maintained and primarily developed by the National Renewable Energy laboratory (`more information <https://www.nrel.gov/wind/openoa.html>`_).

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install.rst
   openoa_examples.rst
   data_integration.rst
   production_deployment.rst
   dev_install.rst
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
