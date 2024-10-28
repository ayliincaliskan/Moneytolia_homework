# Moneytolia Homework

## Local development
1. Install Docker.
2. From the repo's root run: `source tools/docker-development.sh`.

## Technologies Used
1. Django
2. Docker
3. Redis
4. SQlite

## Project Content
- Accounts can be created via a dedicated API.
- After creating an account, an API is available to generate an API key using the account ID.
- Authorized users can shorten URLs through an API that accepts their API key.
- A separate API retrieves the original URL from a given shortened URL.
- The service also provides an API that tracks the total number of URLs shortened.

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
    "password": "your-password-here"
}
```
### Create API Key
- URL: /api/accounts/create-api-key
- METHOD: POST
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
    "key": "your-api-key-here"
}
```
### Shorten URL
- URL: /api/control/shorten-url
- METHOD: POST
#### Request Headers
```bash
{
    Api-Key: "your-api-key-here"
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
- URL: /api/control/original-url
- METHOD: GET
#### Request Headers
```bash
{
    Api-Key: "your-api-key-here"
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
- URL: /api/control/analytics
- METHOD: GET
#### Request Headers
```bash
{
    Api-Key: "your-api-key-here"
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