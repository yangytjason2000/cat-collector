# Cat Collector Setup Guide

This guide will help you set up the website by configuring the environment, setting up the database, and running the backend and frontend servers.

## Prerequisites

- **Python** installed on your system.
- **Node.js** and **npm** installed on your system.

## Setting Up the Environment

1. **Create the `.env` File:**

   - Copy the `.env_example` file to create a new file named `.env` in the root directory.
   - Replace the placeholders in the `.env` file with your actual database credentials and API key:

     \`\`\`plaintext
    THE_CAT_API_URL = "https://api.thecatapi.com/v1/images/search"
    THE_CAT_API_KEY = <your_cat_api_key>
    DB_USERNAME = <your_database_username>
    DB_PASSWORD = <your_database_password>
    DB_PORT = <your_database_port>
     \`\`\`

2. **Create and Activate a Virtual Environment:**

   Open your terminal and navigate to the project root directory, then run the following commands:

   \`\`\`bash
   python -m venv .venv
   \`\`\`

   - **Activate the virtual environment:**

     - On **Windows**:

       \`\`\`bash
       .venv\\Scripts\\activate
       \`\`\`

     - On **macOS/Linux**:

       \`\`\`bash
       source .venv/bin/activate
       \`\`\`

## Setting Up the Backend

1. **Navigate to the Backend Directory:**

   \`\`\`bash
   cd backend
   \`\`\`

2. **Install Backend Dependencies:**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Create and Populate the Database:**

   \`\`\`bash
   python .\\create_database.py
   \`\`\`

   This script will create the database using the schema and populate it with 100 random cats' information from the Cat API.

4. **Start the Backend Server:**

   \`\`\`bash
   flask run
   \`\`\`

## Setting Up the Frontend

1. **Open a New Terminal and Navigate to the Frontend Directory:**

   \`\`\`bash
   cd frontend
   \`\`\`

2. **Install Frontend Dependencies:**

   \`\`\`bash
   npm install
   \`\`\`

3. **Start the Frontend Server:**

   \`\`\`bash
   npm start
   \`\`\`

After following these steps, your website should be up and running. You can access the frontend and backend servers through their respective URLs.