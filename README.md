# Moneytolia Homework

## Local development
1. Install Docker.
2. From the repo's root run: `source tools/docker-development.sh`.

## Technologies Used
1. Docker
2. Django
3. Redis
4. SQlite

## Project Content
- There is an API to create an account.
- There is an API that creates an API key with the ID returned from the account.
- There is an API that can make requests with an API key and shorten the URL.
- There is an API that returns the original shortened url.
- There is an API that keeps the number of short urls created.

## API Endpoints
### Create Account
- URL: /api/accounts/create-user
- METHOD: POST
#### Request Body
```bash
{
    "username": "exampleuser",
    "password": "password123"
}
```