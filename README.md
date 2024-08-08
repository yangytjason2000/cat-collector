# Cat Collector Setup Guide

This guide will help you set up the website by configuring the environment, setting up the database, and running the backend and frontend servers.

## Prerequisites

- **Python** installed on your system.
- **Node.js** and **npm** installed on your system.

## Setting Up the Environment

1. **Create the `.env` File:**

   - Copy the `.env_example` file to create a new file named `.env` in the root directory.
   - Replace the placeholders in the `.env` file with your actual database credentials and API key:

     ```plaintext
        THE_CAT_API_URL = "https://api.thecatapi.com/v1/images/search"
        THE_CAT_API_KEY = <your_cat_api_key>
        DB_USERNAME = <your_database_username>
        DB_PASSWORD = <your_database_password>
        DB_PORT = <your_database_port>
    ```

2. **Create and Activate a Virtual Environment:**

   Open your terminal and navigate to the project root directory, then run the following commands:

   ```bash
   python -m venv .venv
   ```

   - **Activate the virtual environment:**

     - On **Windows**:

       ```bash
       .venv\Scripts\activate
       ```

     - On **macOS/Linux**:

       ```bash
       source .venv/bin/activate
       ```

## Setting Up the Backend

1. **Navigate to the Backend Directory:**

   ```bash
   cd backend
   ```

2. **Install Backend Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create and Populate the Database:**

   ```bash
   python .\create_database.py
   ```

   This script will create the database using the schema and populate it with 100 random cats' information from the Cat API.

4. **Start the Backend Server:**

   ```bash
   flask run
   ```

## Setting Up the Frontend

1. **Open a New Terminal and Navigate to the Frontend Directory:**

   ```bash
   cd frontend
   ```

2. **Install Frontend Dependencies:**

   ```bash
   npm install
   ```

3. **Start the Frontend Server:**

   ```bash
   npm start
   ```

After following these steps, your website should be up and running. You can access the frontend and backend servers through their respective URLs.

# Testing

1. **Navigate to the Backend Directory in your virtual environment:**

   ```bash
   cd backend
   ```

2. **Simply run pytest**

   ```bash
   pytest
   ```

# API Documentation

This section provides detailed information about the available API endpoints, including parameters, expected behavior, and example responses.

## 1. `GET /cats`

- **Description:** Retrieve a paginated list of all cats in the database.
- **Parameters:**
  - `page` (optional, default: 1): The page number for pagination.
  - `limit` (optional, default: 10): The number of cats to retrieve per page.
- **Response:**
  - Returns a list of cat objects with the following fields: `id`, `api_id`, `image_url`, `name`, `description`, and `is_favorite`.
- **Example Request:**
  ```http
  GET /cats?page=1&limit=10
  ```
- **Example Response:**
  ```json
  [
    {
      "id": 1,
      "api_id": "abc123",
      "image_url": "https://example.com/cat1.jpg",
      "name": "cat1",
      "description": "A good cat.",
      "is_favorite": false
    },
    {
      "id": 2,
      "api_id": "def456",
      "image_url": "https://example.com/cat2.jpg",
      "name": "cat2",
      "description": "A cool cat.",
      "is_favorite": true
    }
  ]
  ```

## 2. `POST /cats`

- **Description:** Add a new cat to the favorites list.
- **Request Body:**
  - `cat_id` (required): The ID of the cat to be added to the favorites list.
- **Response:**
  - Returns a success message and the ID of the cat added to favorites.
- **Example Request:**
  ```http
  POST /cats
  Content-Type: application/json

  {
    "cat_id": 1
  }
  ```
- **Example Response:**
  ```json
  {
    "message": "Cat added to favorites",
    "cat": 1
  }
  ```

## 3. `GET /cats/<int:cat_id>`

- **Description:** Retrieve detailed information about a specific cat by its ID.
- **Parameters:**
  - `cat_id` (required): The ID of the cat to retrieve.
- **Response:**
  - Returns a cat object with the fields: `id`, `api_id`, `image_url`, `name`, `description`, and `is_favorite`.
- **Example Request:**
  ```http
  GET /cats/1
  ```
- **Example Response:**
  ```json
  {
    "id": 1,
    "api_id": "abc123",
    "image_url": "https://example.com/cat1.jpg",
    "name": "cat1",
    "description": "A good cat.",
    "is_favorite": false
  }
  ```

## 4. `PUT /cats/<int:cat_id>`

- **Description:** Update the name or description of a specific cat by its ID.
- **Parameters:**
  - `cat_id` (required): The ID of the cat to update.
- **Request Body:**
  - `name` (optional): The new name of the cat.
  - `description` (optional): The new description of the cat.
- **Response:**
  - Returns a success message and the ID of the updated cat.
- **Example Request:**
  ```http
  PUT /cats/1
  Content-Type: application/json

  {
    "name": "Mr. Whiskers",
    "description": "A very friendly cat."
  }
  ```
- **Example Response:**
  ```json
  {
    "message": "Cat updated",
    "cat": 1
  }
  ```

## 5. `DELETE /cats/<int:cat_id>`

- **Description:** Remove a cat from the favorites list by its ID.
- **Parameters:**
  - `cat_id` (required): The ID of the cat to remove from favorites.
- **Response:**
  - Returns a success message and the ID of the cat removed from favorites.
- **Example Request:**
  ```http
  DELETE /cats/1
  ```
- **Example Response:**
  ```json
  {
    "message": "Cat removed from favorites",
    "cat": 1
  }
  ```