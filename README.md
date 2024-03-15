<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

# Base AI Deployment API
<b>Developer: </b>John Markton M. Olarte <a href="mailto:markton.operations@gmail.com" data-bs-toggle="tooltip" data-bs-placement="right" title="Send an e-mail">`📧`</a>
<br>
<b>Status: </b>`Under Development`
## About
This is a base API for deploying AI, ML, or DL models using containerization. It provides a RESTful interface for easy integration and deployment of your models.

## License
This file is part of Base AI Deployment API.

Base AI Deployment API is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Base AI Deployment API is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Base AI Deployment API. If not, see <https://www.gnu.org/licenses/>.


# INITIAL SETUP
## Required Softwares & Tools
1. <a href="https://www.docker.com/" data-bs-toggle="tooltip" data-bs-placement="right" title="Visit Docker's Homepage"> Docker </a>
2. <a href="https://www.python.org" data-bs-toggle="tooltip" data-bs-placement="right" title="Visit Python's Homepage">Python</a> <br><i>(This software was developed using version 3.12)</i>
3. <a href="https://www.mongodb.com/" data-bs-toggle="tooltip" data-bs-placement="right" title="Visit MongoDB's Homepage"> MongoDB </a>

## Other setups
### Create `main.env` on the root directory
<i> See `.env` file for the example template </i>
```python
MONGODB_NAME=api
MONGODB_USERNAME=root
MONGODB_PASSWORD=
MONGODB_HOST=127.0.0.1
MONGODB_PORT=27017
```

### Create `db.env` on the root directory
<i> See `.env` file for the example template </i>
```python
MONGO_INITDB_DATABASE=api
MONGO_HOST=127.0.0.1
MONGO_PORT=27017
```

### Create `docker-compose.yml`
<i> You may extend this based on your additional requirements/needs.</i>
```yml
version: "3.8"
name: "breadcrumbs.ai"
services:
  main:
    container_name: "breadcrumbs"
    build: ./breadcrumbs
    ports:
      - 8080:8080
    env_file:
      - main.env
  mongo_db:
    container_name: "mongo_db"
    image: "mongo:4.0"
    ports:
      - 27017:27017
    volumes:
      - api_db:/data/db
    environment:
      - MONGO_INITDB_ROOT_USERNAME=admin
      - MONGO_INITDB_ROOT_PASSWORD={password}
    env_file:
      - db.env
volumes:
  api_db:
```
# Usage
`TO FOLLOW`