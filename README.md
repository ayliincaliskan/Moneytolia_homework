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
#### Response
```bash
{
    "id": 1,
    "username": "exampleuser",
    "password": "pbkdf2_sha256$600000$l9aFpR77NoWUxcvYf5o1be$4V06PNfXGrRFBj791XZSe04YBdk8Yc8fk7DzEwaIgWw="
}
```
### Create API Key
URL: /api/accounts/create-api-key
METHOD: POST
#### Request Body
```bash
{
    "user": 1   #user_id
}
```
#### Response
```bash
{
    "user": 1,
    "key": "95n4b6uBaQcaQWPPhcrFdbSi6Wjtl5"
}
```
### Shorten URL
URL: /api/control/shorten-url
METHOD: POST
#### Request Headers
```bash
{
    Api-Key: "95n4b6uBaQcaQWPPhcrFdbSi6Wjtl5"
}
```
#### Request Body
```bash
{
    "url_request": "www.twitter.com"
}
```
#### Response
```bash
{
    "short_url": "660328",
    "limit": 1
}
```
### Original URL
URL: /api/control/original-url/?short_url=660328
METHOD: GET
#### Request Headers
```bash
{
    Api-Key: "95n4b6uBaQcaQWPPhcrFdbSi6Wjtl5"
}
```
#### Request Params
```bash
{
    short_url: "660328"
}
```
#### Response
```bash
{
    "original_url": "www.twitter.com"
}
```
#### Analytics
URL: /api/control/analytics
METHOD: GET
#### Request Headers
```bash
{
    Api-Key: "95n4b6uBaQcaQWPPhcrFdbSi6Wjtl5"
}
```
#### Response
```bash
[
    {
        "original_url": "www.twitter.com",
        "short_url": "660328",
        "click_count": 3
    },
    {
        "original_url": "www.facebook.com",
        "short_url": "660328",
        "click_count": 3
    }
]
```