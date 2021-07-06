# MockServer
This is a mock server intended to provide services with basic functionality used for integration testing.

## Registartion
* Register a user account and store in DB. Functionality to perform CURD operations.

### Register User
```
POST http://HOST/user

{
    "email": "Jack@email.com",
    "name": "Jack",
    "password": "Passwd"
}

```

### Get User Details
```
GET http://HOST/user/{username}

```

### Update User
```

PUT http://HOST/user

{
    "email": "Jack@email.com",
    "name": "Jack",
    "password": "Passwd"
}

```
### Delete User Details
```
DELETE http://HOST/user/{username}

```

## Status Code Generator
* Generate a status code to test various error scenarios. The API takes a integer code in path parameter and returns the same HTTP status.

'''
GET http://HOST/mock/status/{statuscode}
'''

* This case HTTP 200 (OK) will be returned.

'''
GET http://HOST/mock/status/200

'''

* Similarly to trigger an Internal Server Error, 500 can be passed.

'''
GET http://HOST/mock/status/500

'''

## Timeout Generator
* API to delay the server response. Benificial when it is required to test the timeout in different scenarios.
* The API accepts a delay interval (seconds) as a path parameter and the API responds after the specified time.

'''

GET http://HOST/mock/timeout/{interval}

'''

## URL Shortener
* Generate a short URL for a specified URL.
# Generate Short URL

'''
POST http://HOST/url

POST Body:
{
    "url": "www.google.co.in"
}

'''

# Get the Actual URL
* When the shorter URL is accessed in the browser, the actual URL is called automatically.
'''

GET http://HOST/u/nZUmBLsN

'''
