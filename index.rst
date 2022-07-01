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

The ENTR data environment is a distribution of existing tools, frameworks, and standards, packaged together to enable efficient analysis of operational wind energy data. The ENTR environment consists of the ENTR runtime, ENTR warehouse, and OpenOA operational analysis Python package, all integrated into an easy-to-run Docker container. These copmonents are provided as separate repositories maintained by the ENTR Alliance.

TODO: few sentences about runtime and what it is used for.

TODO: few sentences about warehouse and what it is used for.

The `Open Operational Assessment (OpenOA) Python package <https://github.com/entralliance/OpenOA>`_ is used within the ENTR environment to perform operational assessments of wind plants using data stored in the ENTR warehouse. OpenOA consists of modules for organizing different types of data (e.g., revenue meter, supervisory control and data acquisition (SCADA), meteorological tower, and reanalysis), low-level data analysis toolkits (e.g., filtering, power curve fitting), and high-level operational assessment methods (such as long-term energy production estimation). OpenOA is maintained and primarily developed by the National Renewable Energy laboratory (`more information <https://www.nrel.gov/wind/openoa.html>`_).

TODO: few sentences about Docker containiner and what it is used for.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install.rst
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
