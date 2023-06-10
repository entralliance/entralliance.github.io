.. _getting_started:


.. ::

    # with overline, for parts
    * with overline, for chapters
    =, for sections
    -, for subsections
    ^, for subsubsections
    ", for paragraphs

###############
Getting Started
###############

How to get started using the ENTR data stack.

*****************************
Installating the ENTR Runtime
*****************************

This section contains information on how to install and begin using the ENTR Runtime for analysis.
For instructions on how to develop the components of the ENTR runtime itself, please see the Developer Setup section.

.. mdinclude:: ./content/entr_runtime_readme.md


********************************
Developing with the ENTR Runtime
********************************

This section contains information on how to begin developing the components of the ENTR Runtime environment.

.. mdinclude:: ./content/entr_runtime_dev_readme.md


*********************
Run ENTR on Your Data
*********************

If you're already using dbt, you should install dbt-openoa in your dbt project and follow the guidelines below for how to build models to
feed the ENTR transformation pipeline to leverage OpenOA.

The ENTR Warehouse is an example dbt project available on the ENTR runtime - the easiest way to test out the functionality of the ENTR data stack
on your own data if you aren't already using dbt is to load data as a CSV 

.. mdinclude:: ./_external/entr_warehouse_readme.md


Running OpenOA on ENTR
----------------------

The ENTR Runtime includes example analysis notebooks that demonstrate operational wind plant data analytics use cases using OpenOA with example data stored in the ENTR warehouse.
The example notebooks are located at /examples in the `ENTR OpenOA repository <https://github.com/entralliance/OpenOA>`_.
All examples use two years of data for the 4-turbine `"La Haute Borne" <https://opendata-renewables.engie.com>`_ wind plant.

Running the Examples
--------------------

1. Complete the Installation section and open Jupyter Hub in your web browser.
2. On the left-hand side of Jupter Hub, navigate to: ``src/OpenOA/examples/entr``
3. Double click on any example notebook to open it.

List of Examples
----------------

The ENTR runtime contains two example notebooks:

* `Example 1: Basic toolkit functions <https://github.com/entralliance/OpenOA/blob/main/examples/entr/00_toolkit_examples_entr.ipynb>`_
* `Example 2: Long-term AEP assessment <https://github.com/entralliance/OpenOA/blob/main/examples/entr/02_plant_aep_analysis_entr.ipynb>`_

..
   TODO: Use nbsphinx to include notebooks directly in documentation once Pandoc issue is fixed for the github action

OpenOA documentation
--------------------

OpenOA documentation is hosted on `ReadTheDocs <https://openoa.readthedocs.io/en/latest/>`_.

Data are stored and organized in OpenOA using a ``PlantData`` object. The ``PlantData`` class in the OpenOA fork included in the ENTR runtime contains a ``from_entr`` method (`link to source code with documentation <https://github.com/entralliance/OpenOA/blob/main/operational_analysis/types/plant.py#L313>`_), which is used to load data into OpenOA from the ENTR warehouse.
