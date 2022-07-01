# ENTR

ENTR is a distribution of existing tools, frameworks, and standards, 
packaged together to accelerate the transition to clean energy.

The ENTR runtime provides a containerized environment with a Spark server, a version 
of Python compatible with OpenOA, a Jupyter notebook server and dbt. This runtime can
be used for development and learning in place of the stack components used in
production by renewable generator operators.

## Quickstart

1. Install Docker Desktop on your workstation \(see [instructions](https://www.docker.com/products/docker-desktop)\).
    - We recommend following [this guide](https://docs.docker.com/docker-for-windows/install/) to install Docker on Windows. After installing the WSL 2 backend and Docker you should be able to run containers using Windows PowerShell.
2. Pull our image:

```docker pull ghcr.io/entralliance/entr_runtime:dev```

3. Run the entr runtime container, forwarding the necessary ports:

```docker run -p 8888:8888 ghcr.io/entralliance/entr_runtime:dev```

4. Click on the Jupyter link printed to the terminal.

## Developing ENTR Runtime Components

The ENTR runtime contains the following preinstalled components: OpenOA, entr_warehouse. To develop these components, you check out development versions of these packages to your local filesystem, and then start the entr image with these paths mounted as volumes. If `$ENTR_HOME` is the directory you'd like to work from:

1. `cd $ENTR_HOME`
2. `git pull https://github.com/entralliance/entr_warehouse.git`
3. `git pull https://github.com/entralliance/OpenOA.git`
4. `git pull https://github.com/entralliance/entr_runtime.git`
5. Optionally, build the entr image. You can also use the dev image from the container registry as discussed in Quickstart.
6. Now, start the entr container in dev mode:
`docker run -p 8888:8888 -p 8080:8080 -p 4040:4040 -v $ENTR_HOME/OpenOA:/home/jovyan/src/OpenOA -v $ENTR_HOME/entr_warehouse:/home/jovyan/src/entr_warehouse`
7. Once inside the container, you will then need to re-install OpenOA in editable mode, or run `dbt run` as needed to update the container with the new code.
    - To install OpenOA in editable mode:
        - `cd /home/jovyan/src/OpenOA`
        - `pip install -e .`
    - To re-run DBT: 
        - `cd /home/jovyan/src/entr_warehouse`
        - `dbt run`

### To Update the Warehouse

Changes to the warehouse may require re-running dbt. To do this:

1. Open a terminal from Jupyter (File > New > Terminal) and navigate to the location where your dbt project is installed (see section "Assumed Repository Structure" section below) using `cd ~/host/entr_warehouse` and run `dbt debug` to test your connection to the Spark warehouse.
2. Once the connection to the warehouse is confirmed, install the dbt packages for your project using `dbt deps`
3. Seed the example data contained in the entr_warehouse repo using `dbt seed` to instantiate them in the Spark warehouse
4. Run `dbt run` to build all models in the Spark warehouse, which can now be consumed by any application connected to the Spark warehouse such as OpenOA

## Building the entr_runtime image

In most cases, we reccomend using the pre-built entr_runtime image avaialble from the github container registry (see quickstart). If you need to rebuild the image yourself, navigate to the entr_runtime directory and run:

```
docker build -t entr/entr-runtime docker
```

### Running the entr runtime container

Basic mode, forwarding all ports to localhost:

```
docker run -p 8888:8888 -p 8080:8080 -p 4040:4040 entr/entr-runtime
# use the option --no-cache to force rebuilding of each layer
```

Dev mode, overload OpenOA and entr_warehouse with development versions

```
docker run -p 8888:8888 -p 8080:8080 -p 4040:4040 -v <path-to-local-clone-of-OpenOA>:/home/jovyan/src/OpenOA -v <path-to-local-clone-of-entr_warehouse>:/home/jovyan/src/entr_warehouse entr/entr-runtime-dev
```
Note, you will then need to re-install OpenOA in editable mode, or run `dbt run` as needed to update the container with the new code.

```
!connect jdbc:hive2://localhost:10000
```

## Roadmap

Coming soon!
