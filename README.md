# coolGeoApp API

**CoolGeoApp** is a test REST API to provide data to the CoolGeoApp web client.
It has been developed with [FastAPI](https://fastapi.tiangolo.com/) framework and [Pydantic](https://pydantic-docs.helpmanual.io/) library.

The API runs over a [Uvicorn](https://www.uvicorn.org/) server and the data is stored in a [PostgreSQL](https://www.postgresql.org/) database with the spatial extension [PostGIS](https://postgis.net/).
Both components, server with API and database, are available as images of [Docker](https://www.docker.com/) to facilitate their instalation and use. You can find them hosted in [Docker Hub](https://hub.docker.com/r/visancal/coolgeoapp)


## Installation

You need **Docker engine** and **Docker compose** installed in your computed to run the CoolGeoApp API. If you don't have docker installed, please check this [link](https://docs.docker.com/engine/install/).

### Downloading source code

```bash
    sudo docker-compose up -d --build
    sudo docker-compose up 
```
### Images from Docker hub

* Run database container 
  
```bash
docker run visancal/coolgeoapp:db
```
* Run server container
  
```bash
docker run visancal/coolgeoapp:api
```

## Usage

When the two docker containers are running (API server and spatial database) you can go to your favorite browser and write [http://localhost:8000/docs](http://localhost:8000/docs).
This link shows the [Swagger UI](https://swagger.io/) of the API, where you can see all the available endpoints of the API and you can test all of them.  

## Improvements
xxxxx

## License
[MIT](https://choosealicense.com/licenses/mit/)