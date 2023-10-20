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
    - [Item Search](#item-search)
        - [All items](#all-items)
        - [One_item](#one-item)
3. [Examples](#examples)
4. [SDK-Integration](sdk-integration)

## Getting Started

To begin using the API, you can simply make requests to the available API endpoints listed below. User authentication is required for accessing the basic information about fruits and vegetables.

## API Endpoints

### Authentication

### Welcome view
**Endpoint:** `/api/v1/auth`

**Method:** "GET"

**Example Request**
```
GET /api/v1/auth
```
**Response:** This request leads you to the welcome view.

### Register
**Endpoint:** `/api/v1/auth/register`

**Method:** "POST"

**Example Request**
```
/api/vi/auth/register
```
**Response:** This request enables new users to enter their details and thereafter use them to get logged in.

### Login
**Endpoint:** `/api/v1/auth/token`

**Method:** "POST"

**Example Request**
```
/api/v1/auth/token
```
**Response:** This request leads old users to the page where they enter their login details and get logged in to utilize and consume the API.

### User profile
**Endpoint:** `/api/v1/user/profile`

**Method:** "GET"

**Example Request**
```
GET /api/v1/user/profile
```
**Response:**  It represents a user's identity and contains details relevant to the user's interactions, preferences, and personalization within the given context.

## Item search
Search for fruits or vegetables based on a keyword or partial name.

### All items

**Endpoint:** `/api/v1/fruits/all`

**Method:** "GET"

```
GET /api/v1/fruits/all
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

**Endpoint:** `/api/v1/fruits/search`

**Method:** "GET"

**Parameters:** 
- query (required): The keyword or partial name to search for. (e.g banana)

**Example Request**

**Query search by name**
```
GET /api/v1/fruits/search?q=banana
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

## SDK-Integration
To successfully integrate the Treblle-Dynasty SDK in your app, follow the steps highlighted [here](https://github.com/Certifieddonnie/treblle-dynasty/blob/develop/README.md)

