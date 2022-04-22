
# Trip API

These endpoints allows you to upload trip data to a database. 

## Instalation

For local test, you can clone the project using:
```bash
git clone git@github.com:EwertonES/trip-api.git
```  
After opening the terminal inside the folder, create the docker image and run the container with:

```bash
docker build -t trip:Dockerfile .
docker run -e PORT=8000 -p 8000:8000 trip:Dockerfile
```  
It will be running on https://localhost:8000.

## Endpoints

You can see the Swagger documentation using this link: https://app.swaggerhub.com/apis-docs/EwertonES/Jobsity2/1.0.0

## Data flow

![GCP Framework](https://i.imgur.com/z761TnU.png)

## CI/CD

The CI/CD pipeline is inside .github/workflows, in a file named main.yml. It is responsible for setting up an Ubuntu terminal, authenticate it in Google Cloud, building & pushing the container, then finally deploy the app in Cloud Run.

## GCP Access

If you want to see inside Google Cloud Platform, just [SEND](mailto:ewerton@ewerton.com.br?subject=TRIP-API%20GCP%20Access&body=Hello%20Ewerton!%0D%0A%0D%0ACould%20you%20give%20me%20access%20to%20the%20trip-api%20project%20on%20GCP?%0D%0AMy%20email%20is%20name@domain.com.%0D%0A%0D%0ABest%20regards,) your email to me so I can share the project with you.