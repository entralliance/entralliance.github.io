.. entr_docs documentation master file, created by
   sphinx-quickstart on Tue Jun  7 16:38:12 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _index:

ENTR Foundation
===============================================

Welcome to the ENTR Foundation docs site!

This documentation can be used to learn more about the technology built by the ENTR Foundation to support our mission of establishing open data standards for the clean energy industry.

- Find out more about ENTR: `<https://www.entrfoundation.org>`_
- `Sign up for the ENTR Newsletter <https://share.hsforms.com/1KkvJPJorSK2P2-3yY4m7Hw8mogq>`_
- `Follow us on LinkedIn <https://www.linkedin.com/company/90693649>`_
- `Join us on Slack <https://join.slack.com/t/entralliance/shared_invite/zt-1x6945h00-iDxalk2w9cHO~n2Dw4btyg>`_

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install.rst
   openoa_examples.rst
   data_integration.rst
   production_deployment.rst
   dev_install.rst
   contributing.md
   troubleshooting.rst
   Readme.md

The `ENTR Runtime <https://github.com/entralliance/entr_runtime>`_
------------------------------------------------------------------------
The ENTR runtime is a distribution of 
tools, frameworks, and standards relevant to renewable energy data analysis,
packaged together in a Docker container to enable efficient and reproducible analysis workflows. The ENTR runtime is managed by the `ENTR Foundation <https://www.entrfoundation.org>`_ initiative. Currently, the ENTR
runtime is designed for wind energy data, but other technologies are planned for future releases (e.g., solar, battery storage).
The ENTR runtime is based on Jupyter's Spark Notebook container, and includes the ENTR warehouse, the OpenOA operational analysis Python package, and example data.
The runtime containerizes the required set of software to run the ENTR warehouse and OpenOA methods within a single environment,
and it provides a sandbox environment enabling analysts and developers in the ENTR ecosystem to get started quickly.
For example, analysts can perform operational assessments with OpenOA using example wind plant data,
and developers can start customizing data transformations in the ENTR warehouse.

.. figure:: ./images/entr_runtime_diagram.svg
   :width: 700
   :alt: Block diagram of the ENTR Runtime container. The image is based on Jupyter all spark notebook, which in turn is based on Ubuntu. The runtime adds the OpenOA, Entr Warehouse, and example data to this stack.

   Block diagram of the ENTR Runtime container. The image is based on Jupyter all spark notebook, which in turn is based on Ubuntu. The runtime adds the OpenOA, Entr Warehouse, and example data to this stack.

The ENTR runtime is implemented as a Docker container (`hosted here <https://ghcr.io/entralliance/entr_runtime>`_), providing a unified analysis environment in which the ENTR environment can be deployed in a “write once, run anywhere” and platform-independent way.
(`Docker <https://www.docker.com>`_ is a cross-platform containerization software that has become the de facto standard for
deploying self-contained software environments and services for virtually any computer application.)

The `ENTR Warehouse <https://github.com/entralliance/entr_warehouse>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ENTR Warehouse provides template Data Build Tool (dbt) macros and scripts to assist in building and orchestrating a data warehouse for operational wind plant data. (`dbt <https://www.getdbt.com>`_ is an open-source command-line tool designed to build and run data transformations in a data warehouse.)
The ENTR warehouse provides an open foundation for data analysis, on which methods can be built and standardized.
The warehouse materializes database objects in the Spark database provided by the ENTR runtime for each type of wind plant data
(e.g., supervisory control and data acquisition (SCADA), revenue meter), using the standard ENTR data model,
which includes data transformations and table schema.

Python Packages `OpenOA <https://github.com/entralliance/OpenOA>`_ and `py-entr <https://github.com/entralliance/py-entr>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OpenOA (Open Operational Assessment) is used within the ENTR environment to perform operational assessments of wind plants using data stored in the ENTR warehouse.
OpenOA consists of modules for organizing different types of data
(e.g., revenue meter, SCADA, meteorological tower, and reanalysis),
low-level data analysis toolkits (e.g., filtering, power curve fitting),
and high-level operational assessment methods (such as long-term energy production estimation).
OpenOA is maintained and primarily developed by the National Renewable Energy laboratory (`more information <https://www.nrel.gov/wind/openoa.html>`_).

In addition to OpenOA, the entr_runtime distributes a python package called `entr`,
which provides connection classes to interface with and query from the built-in Spark ENTR warehouse,
as well as a constructor for OpenOA which facilitates the creation of OpenOA PlantData objects using ENTR data.



..
   Once Pandoc issue is fixed for the github actions, add the following to the toctree above after install.rst: examples_combined

..
   Indices and tables
   ==================

   * :ref:`genindex`
   * :ref:`modindex`
   * :ref:`search`
