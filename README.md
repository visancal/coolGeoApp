# coolGeoApp API

**CoolGeoApp** is a test REST API to provide data to the CoolGeoApp web client.
It has been developed with [FastAPI](https://fastapi.tiangolo.com/) framework and [Pydantic](https://pydantic-docs.helpmanual.io/) library.

The API runs over a [Uvicorn](https://www.uvicorn.org/) server and the data is stored in a [PostgreSQL](https://www.postgresql.org/) database with the spatial extension [PostGIS](https://postgis.net/).
Both components, server with API and database, are available as images of [Docker](https://www.docker.com/) to facilitate their instalation and use. You can find them hosted in [Docker Hub](https://hub.docker.com/r/visancal/coolgeoapp)


## Installation

You need **Docker engine** and **Docker compose** installed in your computed to run the CoolGeoApp API. If you don't have docker installed, please check this [link](https://docs.docker.com/engine/install/).

You have the following options to run this API:

### 1. Downloading source code

```bash
    git clone https://github.com/visancal/coolGeoApp.git
    cd coolGeoApp
    docker-compose up -d --build
```
### 2. Using images from Docker Hub (No available yet)

* Run database container 
  
```bash
    docker run -d -p 5432:5432 visancal/coolgeoapp:db
```
* Run server container
  
```bash
    docker run -d -p 8000:8000 visancal/coolgeoapp:server
```

## Usage

When the two docker containers (API server and spatial database) are running you can go to your favorite browser and write [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redoc).
This link shows the API [Swagger UI](https://swagger.io/), where you can see all the available endpoints of the API and you can test all of them.  

## Improvements
* Publish geometries with WKB format
* Cache with Redis
* Add a security layer

## License
[MIT](https://choosealicense.com/licenses/mit/)