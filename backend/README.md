# HackRice 15 Starter Backend

Welcome to the HackRice 15 Starter Backend! This guide will walk you through setting up and customizing your project. This backend is built with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python.

## Getting Started: Your First Steps

Follow these steps to get your backend up and running.

### 1. Install Dependencies

This project uses a few external libraries, and they are listed in the `requirements.txt` file. Open your terminal and run this command to install them:

```bash
pip install -r requirements.txt
```

### 2. Configure Your Environment

Your application needs some secret keys, like an API key for a service you're using. We'll store these in a special file called `.env` to keep them safe and out of your code.

First, copy the example file:

```bash
cp .env.example .env
```

Next, open the new `.env` file and add your secret keys. You'll need to generate a `SECRET_KEY` for encoding your authentication tokens. You can use a command like `openssl rand -hex 32` to generate one.

### 3. Run the Development Server

Now you're ready to start the server!

```bash
uvicorn main:app --reload
```

This command does a few things:
*   `uvicorn`: The server that runs your application.
*   `main:app`: Tells `uvicorn` to look for an object named `app` in the `main.py` file.
*   `--reload`: Automatically restarts the server whenever you make changes to the code.

Your API is now live at `http://localhost:8000`.

## Understanding the Project Structure

Here's a breakdown of the folders and files in this project:

*   `main.py`: The heart of your application. This is where your FastAPI app is created and configured.
*   `api/`: This is where you'll define your API endpoints (the URLs that users can visit).
    *   `v1/`: We're versioning our API to make it easy to add new features without breaking old ones.
    *   `deps.py`: Handles dependencies, like getting the current user from an authentication token.
*   `core/`: Contains the core logic of your application.
    *   `config.py`: Manages your application's settings, like reading from the `.env` file.
    *   `security.py`: Handles password hashing and token creation.
*   `crud/`: Stands for Create, Read, Update, Delete. This is where you'll put the functions that interact with your database.
*   `db/`: Everything related to your database.
    *   `session.py`: Manages your database connection.
    *   `base_class.py`: A base class for your database models.
*   `models/`: Defines the structure of your database tables (e.g., a `User` table).
*   `schemas/`: Pydantic schemas define the shape of the data you're sending and receiving.
*   `ai/`: A special folder for integrating with Generative AI models.
    *   `base.py`: A base class for all AI providers.
    *   `openai_client.py`, `anthropic_client.py`, `gemini_client.py`: Clients for specific AI providers.
    *   `factory.py`: A factory for creating the correct AI client.

## Your Customization Roadmap

Now that you're set up, here's how you can start building your own features.

### 1. Create a New Database Model

Let's say you want to add a `Post` model for a blog.

1.  **Create a new model:** In `models/post.py`, define your `Post` table.
2.  **Create a new schema:** In `schemas/post.py`, define what a `Post` looks like when it's sent to or from the API.
3.  **Create new CRUD functions:** In `crud/post.py`, write functions to create, read, update, and delete posts.

### 2. Create New API Endpoints

Now, let's expose your new `Post` model through the API.

1.  **Create a new endpoint file:** In `api/v1/endpoints/posts.py`, create a new router.
2.  **Add your endpoints:** Add routes for creating, reading, updating, and deleting posts.
3.  **Include the router in `main.py`:** Add your new router to the main FastAPI app.

### 3. Add a New AI Provider

Want to use a different AI provider? No problem!

1.  **Create a new client:** In the `ai/` folder, create a new file for your provider (e.g., `my_ai_client.py`).
2.  **Implement the `LLMProvider` interface:** Your new client must have a `get_response` method.
3.  **Add it to the factory:** In `ai/factory.py`, add your new client to the `get_llm_provider` function.

Happy hacking!