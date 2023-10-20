# Dynasty-DemoApp
This Demo App is built with FastAPI Framework using `Treblle-Dynasty SDK` built for Treblle. This API provides a wide range of information about fruits and vegetables, including botanical names, type of vitamin present, nutritional benefits, PH values, side effects and preservation method. Whether you're a developer building for the food industry, a nutritionist, chef, or simply a fruit and veggie enthusiast, this API will help you access comprehensive data about various fruits and vegetables. It simply has got you covered.

## Treblle-Dynasty SDK
This is the FastAPI SDK built for Treblle. [Access it here](https://github.com/Certifieddonnie/treblle-dynasty)

# Table of Contents
1. [Getting Started](#getting-started)
2. [API Endpoints](#api-endpoints) 
    - [Authentication](#authentication)
        - [Welcome view](#welcome-view)
        - [Register](#register)
        - [Login](#login)
        - [User profile](#user-profile)
        - [Update profile](#update-profile)
        - [Change password](#change-password)
        - [Delete user](#delete-user)
    - [Item Search](#item-search)
        - [All items](#all-items)
        - [One_item](#one-item)
3. [Error Handling](#error-handling)
4. [Examples](#examples)
5. [Contributing](#contributing)
6. [License](#license)

## Getting Started

To begin using the API, you can simply make requests to the available API endpoints listed below. User authentication is required for accessing the basic information about fruits and vegetables.

## API Endpoints

## Authentication

### Welcome view
**Endpoint:** `/api/vi/auth`

**Method:** "GET"

**Example Request**
```
GET /api/vi/auth
```
**Response:** This request leads you to the welcome view.

### Register
**Endpoint:** `/api/vi/auth/register`

**Method:** "POST"

**Example Request**
```
/api/vi/auth/register
```
**Response:** This request enables new users to enter their details and thereafter use to get logged in.

### Login
**Endpoint:** `/api/vi/auth/token`

**Method:** "POST"

**Example Request**
```
/api/vi/auth/token
```
**Response:** This request leads old users to the page where they enter their login details and get logged in to utilise and consume the API.

### User profile
**Endpoint:** `/api/vi/user/profile`

**Method:** "GET"

**Example Request**
```
GET /api/vi/user/profile
```
**Response:**  It serves as a representation of a user's identity and contains details that are relevant to the user's interactions, preferences, and personalization within the given context.

## Item search
Search for fruits or vegetables based on a keyword or partial name.

### All items

**Endpoint:** `/api/vi/fruits/all`

**Method:** "GET"

```
GET /api/vi/fruits/all
```
**Example Response**
```
{
  "results": [
    {
      "name": "Banana",
      "botanical name": "Musa spp",
      "Vitamins": "B6 Pyridoxine",
      "ph value": "4.5 - 5.2"
    },
 {
      "name": "Spinach",
      "botanical name": "Spinacia oleracea",
      "Vitamins": "Vitamin K",
      "ph value": "6.0 - 7.0"
    },
  ]
}

```
`This request returns all items in the database, according to their id. `

### One item

**Endpoint:** `/api/vi/fruits/search`

**Method:** "GET"

**Parameters:** 
- query (required): The keyword or partial name to search for. (e.g banana)

**Example Request**

**Query search by name**
```
GET /api/vi/fruits/search?q=banana
```
**Example Response**
```
{
  "results": [
    {
      "name": "Banana",
      "botanical name": "Musa spp",
      "Vitamins": "B6 Pyridoxine",
      "ph value": "4.5 - 5.2"
    },
  ]
}

```

## Examples

Usage samples and code snippets
```
/api/vi/auth/register/
```
![image](https://github.com/Certifieddonnie/GreenBounty/assets/81980032/af3a6c6c-bc4c-404c-82d3-8bd4bc453434)

```
/api/v1/auth/login/
```
![image](https://github.com/Certifieddonnie/GreenBounty/assets/81980032/1ea8e4d5-5543-4a0e-af9f-f36a2b7cfffe)

```
/api/v1/auth/user/
```
![image](https://github.com/Certifieddonnie/GreenBounty/assets/81980032/5a7c3f79-9fae-4640-a2af-0628db7c96b9)


```
/api/v1/fruits
```
![image](https://github.com/Certifieddonnie/GreenBounty/assets/81980032/06e1ebfd-31c4-4a18-a0b0-27e2daa64284)


```
/api/v1/fruits/search?name=Orange
```
