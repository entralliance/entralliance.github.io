### Manually Running ENTR in Dev Mode

The ENTR runtime contains the following preinstalled components: OpenOA, entr_warehouse, and py-entr. To develop these components, you check out development versions of these packages to your local filesystem, and then start the entr image with these paths mounted as volumes. You then install the packages from these volumes in editable mode. This allows you to edit the code in these components on your local machine, and see the changes immediately reflected in the runtime. If `$ENTR_HOME` is the directory you'd like to work from:

1. `cd $ENTR_HOME`
2. `git clone https://github.com/entralliance/entr_warehouse.git`
3. `git clone https://github.com/entralliance/OpenOA.git`
4. `git clone https://github.com/entralliance/py_entr.git`
4. `git clone https://github.com/entralliance/entr_runtime.git`
5. Optionally, build the entr image. You can also use the dev image from the container registry as discussed in the quickstart guide.
6. Now, start the entr container in dev mode, mapping the directories you checked out to paths within the container:
`docker run -p 8888:8888 -v $ENTR_HOME/OpenOA:/home/jovyan/src/OpenOA -v $ENTR_HOME/entr_warehouse:/home/jovyan/src/entr_warehouse -v $ENTR_HOME/py-entr:/home/jovyan/src/py-entr`.
7. Once inside the container, you will then need to re-install OpenOA in editable mode, or run `dbt run` as needed to materialize any changes to the dbt model code in the warehouse.
    - To install OpenOA in editable mode:
        - `cd /home/jovyan/src/OpenOA`
        - `pip install -e .`
    - To re-run DBT: 
        - `cd /home/jovyan/src/entr_warehouse`
        - `dbt run`

### To Update the Warehouse

Changes to the warehouse may require re-running dbt. To do this:

1. Open a terminal from Jupyter (File > New > Terminal) and navigate to the location where your dbt project is installed (see section "Assumed Repository Structure" section below) using `cd ~/src/entr_warehouse` and run `dbt debug` to test your connection to the Spark warehouse.
2. Once the connection to the warehouse is confirmed, install the dbt packages for your project using `dbt deps`
3. Seed the metadata tables contained in the entr_warehouse repo using `dbt seed` to instantiate them in the Spark warehouse
4. (Re-)register example or newly added source data files with `dbt run-operation stage_external_sources`
5. Run `dbt run` to build all models in the Spark warehouse, which can now be consumed by any application connected to the Spark warehouse such as OpenOA

### Advanced Topics

Extra ports:

```
docker run -p 8888:8888 -p 8080:8080 -p 4040:4040 entr/entr-runtime
```

Override OpenOA and entr_warehouse with local versions:

```
docker run -p 8888:8888 -p 8080:8080 -p 4040:4040 -v <path-to-local-clone-of-OpenOA>:/home/jovyan/src/OpenOA -v <path-to-local-clone-of-entr_warehouse>:/home/jovyan/src/entr_warehouse entr/entr-runtime-dev
```
Note, you will then need to re-install OpenOA in editable mode, or run `dbt run` as needed to update the container with the new code.

Beeline connect string for ENTR warehouse:

```
beeline
!connect jdbc:hive2://localhost:10000
```

#### Using VSCode Dev Container

We provide an [example VSCode Dev Container](https://github.com/jordanperr/entr_dev_environment.git) config which can be used to get up and running quickly developing the ENTR platform. This is the recommended method if you use VSCode and are familliar with VSCode Dev Containers.

`git clone https://github.com/jordanperr/entr_dev_environment.git`
`cd entr_dev_environment`
`git submodule update --init --remote`

Then, open the project with VSCode and follow the prompts to initialize the dev container.
