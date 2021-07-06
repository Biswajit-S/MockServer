# MockServer
This is a mock server intended to provide services with basic functionality used for integration testing.

## Registartion

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


