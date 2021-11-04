# Exchange Rate Api using GraphQL


## Get Code

```
git clone https://github.com/alaturqua/exchangerate-graphql.git
```
## Create .env file with following content and set your creds for postgres
```
POSTGRESQL_USERNAME=example
POSTGRESQL_PASSWORD=example

PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=example
```

## To run execute command:
```
docker-compose up -d --build
```

Go to page:
http://localhost:5000/graphql


## Example GraphQL Query:

```
query fetchAllExchangeRates {
  exchangerates {
    success
    errors
    exchangerates{
      id
      base
      rate
      currency_code
      date
    }
  }
}
```

## Screenshot from GUI

![Example Image](images/example.png?raw=true "Example Image")

## Backlog:

- Move backlog to proper place
- Redesign front page
- Implement docker, docker-compose for dev, test and production
- Implement production level web server (nginx, wsgi, uvicorn, select proper)
- Implement/Fix manual currency insertion into database
- Implement logging
- Implement automated unit, integration and end-2-end testing
- Implement currency conversion
- Implement historical currency data
- Implement base currency selection / insert data with different base currencies into db.
- Implement CI/CD
- Implement Kubernetes
- Implement Register/login for Web Page
- Implement oauth / token or any authorization concept for API
- Implement Monetization / Free / Monthly / Yearly / Developer / Pro / Enterprise? and create proper web pages.


