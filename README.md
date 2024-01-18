# rtclient

rtclient is the front end of the real time software pipeline. It is only used data acquisition on the microscope, launching and closing services that help with data analysis (segmentation, dot detection, etc). For segmentation code see `rtseg` package.

### Instructions to install the client

Client is meant to be install on the native desktop running the microscope, while analysis services can be installed else where such as a cluster running services. Analysis services are containerized to make operations easy. The clinet will launch the analysis service on the microscope desktop as default.

Commands to create .venv to isolate the requirements for running the client.
```
python3 -m venv .venv
sournce .venv/bin/activate
```

To install the package and dependencies, run the following commands from the root of the client code
```
# if you want editable mode
pip install -e ./ 
# else for installing the .venv paths
pip install .
```

### Developer instructions

Install optional dependencies using commands during development to smooth out integration with github runners

```
# this will install additional dependencies for linting, type-checking, etc
pip install -e ".[linting]"
# or 
pip install -e ".[testing]"

```
