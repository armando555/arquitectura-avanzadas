# Advanced Architectures App

## Authors:
- Armando Rios

# Explanation

Basically this repo has 3 directories: bicicletas, renting and ops.

- Bicicletas is the folder app for the CRUD of the bicycles the basic operations
- Renting is the folder app for the renting bicycle with a date from and date to. Here I expose the route /map with the MAP with https://leafletjs.com/ for rendering markers. Also, I consume an Bicicletas GET API for getting the latitude and longitude for every bicycle that is rented.
- Ops is the folder with the manifest for the Kubernetes deployment


## Coding rules
- Do not create more than one class per file, unless it is really needed.
- Follow PEP 8 https://www.python.org/dev/peps/pep-0008/ (install a code linter and an autoformater like pylance)
- All models will be defined under the app.custom_models module, and must be imported in app.models file.
- All views will be defined under the app.custom_views module, and must be imported and registered in the app.views.file.

## Installation
### Install virtualenv
Run
```bash
python3 -m pip install virtualenv
```
### Create virtual environment
Run
```bash
python3 -m virtualenv --system-site-packages venv
```
### Activate virtual environment
Run
```bash
source ./venv/bin/activate
```
Optionally check if the virtual environment is working correctly with:
```bash
which python3
```
This should output the path to the currently used python3 interpreter and should look something like this.

```bash
/path/to/your/venv/bin/python3
```
## Running application

__Note:__ Running applications on the ports 80 and 443 is restricted. For that you should setup a proper web server or run them as root/sudo.

### Install the requirements
```bash
pip install -r requirements.txt
```

## in repo.template.fastapi/app execute the next commands
```bash
uvicorn main:app --reload
```

### In docker
# build the latest image from source
```bash
docker build -t twelve/fast-api .
```

# Stop container
```
docker stop bicicletas2 && docker rm bicicletas2
```
# run backends
```
docker run -p 8009:8000 --name bicicletas -d bicicletas
```
```
docker run -p 8002:8000 --name renting -e "HOST_BICYCLES=http://bicicletas:8000" --link bicicletas:bicicletas -d bicicletas2
```
# login to the container administrator
```
docker exec -i -t bicicletas sh
```
# see errors in the docker
```
docker logs bicicletas
```
