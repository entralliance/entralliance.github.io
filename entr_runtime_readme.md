## Pull and Run the Image

1. Install Docker Desktop on your workstation \(see [instructions](https://www.docker.com/products/docker-desktop)\).
    - We recommend following [this guide](https://docs.docker.com/docker-for-windows/install/) to install Docker on Windows. After installing the WSL 2 backend and Docker you should be able to run containers using Windows PowerShell.

2. Pull and run our image from github container registry:

```docker pull ghcr.io/entralliance/entr_runtime:latest```

*Note: There are numerous security considerations when pulling and running images from the public internet. User should take the necessary steps to ensure operational security.*

3. Run the entr runtime container, forwarding the necessary ports:

```docker run -p 8888:8888 ghcr.io/entralliance/entr_runtime:latest```

4. Open the Jupyter link printed to the terminal in your web browser.

## Building your own Image

In most cases, we reccomend using the pre-built entr_runtime image avaialble from the github container registry. If you need to rebuild the image yourself, follow the instructions below:

1. Install Git and Docker Desktop on your workstation.

2. Clone the ENTR Runtime repository:

```
git clone git@github.com:entralliance/entr_runtime.git
git checkout dev
```

3. Navigate to the `entr_runtime` directory and run the following, replacing `yourname` with your username:

```
docker build -t yourname/entr-runtime docker
```

*Note: Use the option ``--no-cache`` to force rebuilding of each layer*

4. Run the image you just built:

```docker run -p 8888:8888 yourname/entr_runtime```
