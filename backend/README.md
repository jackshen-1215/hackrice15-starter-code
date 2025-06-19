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

Here's a visual breakdown of the backend directory. This tree structure helps you see how the different parts of the application are organized.

```
backend/
├── ai/                 # For integrating with Generative AI models
│   ├── base.py         # A base class for all AI providers
│   ├── factory.py      # A factory for creating the correct AI client
│   └── ..._client.py   # Clients for specific AI providers
├── api/                # Your API endpoints (URLs)
│   ├── deps.py         # Handles dependencies (e.g., getting current user)
│   └── v1/             # Version 1 of your API
│       └── ... .py     # Your endpoint files
├── core/               # Core application logic
│   ├── config.py       # Manages application settings from .env
│   └── security.py     # Handles password hashing and tokens
├── crud/               # Create, Read, Update, Delete (CRUD) database operations
│   └── user.py         # CRUD functions for the User model
├── db/                 # Database-related code
│   ├── __init__.py     # Initializes the database
│   ├── base_class.py   # A base class for your database models
│   └── session.py      # Manages your database connection
├── models/             # Defines the structure of your database tables
│   └── user.py         # The User table model
├── schemas/            # Pydantic schemas for data validation and serialization
│   ├── token.py        # Schemas for authentication tokens
│   └── user.py         # Schemas for the User model
├── .env.example        # Example environment variables
├── main.py             # The heart of your application, where the FastAPI app is created
└── requirements.txt    # Project dependencies
```

## Your Customization Roadmap

Now that you're set up, here's how you can start building your own features. Each section explains a core concept and then gives you actionable steps.

### 1. Create a New Database Model

**The Concept:** Your application needs a way to store and manage data, like users, posts, or products. We use **SQLAlchemy**, a powerful tool that lets you define your database tables using Python classes called "models." These models live in the `models/` directory. To ensure your data has the correct format when it comes in and out of your API, we use **Pydantic** schemas, which live in the `schemas/` directory. Finally, the actual database logic (creating, reading, updating, deleting) is handled by functions in the `crud/` directory.

*   **Learn more:**
    *   SQLAlchemy ORM: [https://docs.sqlalchemy.org/en/20/orm/](https://docs.sqlalchemy.org/en/20/orm/)
    *   Pydantic Models: [https://docs.pydantic.dev/latest/](https://docs.pydantic.dev/latest/)

**Actionable Steps (Example: Adding a `Post` model):**

1.  **Define the Model:** Create a new file `models/post.py` and define your `Post` table structure using SQLAlchemy.
2.  **Define the Schemas:** Create `schemas/post.py` and define Pydantic schemas for creating and reading posts. This ensures data validation.
3.  **Write CRUD Functions:** Create `crud/post.py` with functions like `create_post`, `get_post`, etc., to interact with the database.

### 2. Create New API Endpoints

**The Concept:** An API endpoint is a specific URL where your application listens for requests. We use **FastAPI's `APIRouter`** to group related endpoints together. This keeps your code organized. For example, all user-related endpoints (`/users/`, `/users/{id}`) would go into a user router. These routers are defined in the `api/v1/endpoints/` directory and then included in the main `FastAPI` app in `main.py`.

*   **Learn more:**
    *   FastAPI Tutorial - Bigger Applications: [https://fastapi.tiangolo.com/tutorial/bigger-applications/](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

**Actionable Steps (Example: Exposing the `Post` model):**

1.  **Create an Endpoint File:** Create `api/v1/endpoints/posts.py` and set up a new `APIRouter`.
2.  **Add Endpoint Functions:** Write functions for `POST /posts`, `GET /posts/{id}`, etc., using your CRUD functions to handle the logic.
3.  **Include the Router:** In `main.py`, import and include your new posts router in the main FastAPI app.

### 3. Add a New AI Provider

**The Concept:** To make it easy to switch between different Large Language Models (LLMs), we use a design pattern called a **Factory**. The `ai/` directory contains a base `LLMProvider` class that defines a common interface (a `get_response` method). Each specific provider (like OpenAI or Anthropic) has its own client class that implements this interface. The `factory.py` file has a function that returns the correct client based on a name. This makes your code flexible and easy to extend.

**Actionable Steps (Example: Adding a new provider `MyAI`):**

1.  **Create a New Client:** In the `ai/` folder, create `my_ai_client.py`.
2.  **Implement the Interface:** Inside the new file, create a `MyAIClient` class that inherits from `LLMProvider` and implements the `get_response` method.
3.  **Update the Factory:** In `ai/factory.py`, import your new `MyAIClient` and add it as an option in the `get_llm_provider` function.

Happy hacking!