# HackRice 15 Starter Backend

Welcome to the HackRice 15 Starter Backend! This guide will walk you through setting up and customizing your project. This backend is built with [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python.

## Getting Started: Your First Steps

Follow these steps to get your backend up and running from the project's root directory.

### 1. Install Dependencies

This project uses a few external libraries, and they are listed in the `requirements.txt` file. Open your terminal and run this command to install them:

```bash
pip install -r backend/requirements.txt
```

### 2. Configure Your Environment

Your application needs some secret keys, like an API key for a service you're using. We'll store these in a special file called `.env` to keep them safe and out of your code.

First, copy the example file:

```bash
cp backend/.env.example backend/.env
```

Next, open the new `backend/.env` file and add your secret keys. You'll need to generate a `SECRET_KEY` for encoding your authentication tokens. You can use a command like `openssl rand -hex 32` to generate one.

### 3. Run the Development Server

Now you're ready to start the server! From the project root, run:

```bash
uvicorn backend.main:app --reload
```

This command does a few things:
*   `uvicorn`: The server that runs your application.
*   `backend.main:app`: Tells `uvicorn` to look for an object named `app` in the `backend/main.py` file.
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
│
├── api/                # Your API endpoints (URLs)
│   ├── deps.py         # Handles dependencies (e.g., getting the current user)
│   └── v1/             # Version 1 of your API
│       ├── api.py      # Main router for API v1
│       └── endpoints/  # Your endpoint files (e.g., auth.py)
│
├── core/               # Core application logic
│   ├── config.py       # Manages application settings from .env
│   └── security.py     # Handles password hashing and tokens
│
├── crud/               # Create, Read, Update, Delete (CRUD) database operations
│   ├── base.py         # A generic base class for CRUD operations
│   └── user.py         # CRUD functions for the User model
│
├── db/                 # Database-related code
│   ├── base_class.py   # A base class for your database models
│   └── session.py      # Manages your database connection and session
│
├── models/             # Defines the structure of your database tables
│   └── user.py         # The User table model
│
├── schemas/            # Pydantic schemas for data validation and serialization
│   ├── token.py        # Schemas for authentication tokens
│   └── user.py         # Schemas for the User model
│
├── .env.example        # Example environment variables
│
├── main.py             # The heart of your application, where the FastAPI app is created
│
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

### 4. Designing Your Own Modules

As your application grows, you'll want to add new features. The best way to do this is by creating self-contained **modules**. A module is a collection of related code that handles a specific piece of functionality (e.g., a blog, user profiles, or product inventory).

**The Philosophy:** A modular design keeps your code organized, makes it easier to test, and allows different team members to work on different features at the same time without conflicts. Each module should have a clear responsibility.

**Anatomy of a Feature Module (Example: A "Blog" Module):**

A complete feature module typically includes:

1.  **Models (`models/blog.py`):** Define the database tables for your feature, like `Post` and `Comment`. These models would include relationships (e.g., a `Post` has many `Comments`).
2.  **Schemas (`schemas/blog.py`):** Create Pydantic schemas for data validation. You'd have schemas for creating a post (`PostCreate`), reading a post (`Post`), and creating a comment (`CommentCreate`).
3.  **CRUD (`crud/blog.py`):** Write the database logic. You could create a `CRUDPost` class that inherits from the generic `CRUDBase` to handle posts, and a `CRUDComment` for comments.
4.  **API Endpoints (`api/v1/endpoints/blog.py`):** Expose your feature through a new `APIRouter`. This file would contain endpoints like `POST /blog/posts`, `GET /blog/posts/{id}`, and `POST /blog/posts/{id}/comments`.

**How to Structure Your Code:**

*   **Group by Feature:** For larger applications, you might even create a new directory for each module (e.g., `backend/blog/`) that contains its own `models.py`, `schemas.py`, `crud.py`, and `endpoints.py`.
*   **Keep it Simple:** For a hackathon, keeping models, schemas, and CRUD operations in their respective top-level directories (`models/`, `schemas/`, `crud/`) is perfectly fine. The key is to be consistent.

**Extending the Core:**

Don't be afraid to extend the core modules when needed:

*   **`core/security.py`:** You might add new functions for handling permissions or different authentication methods.
*   **`core/config.py`:** Add new configuration variables from your `.env` file as your application needs them.
*   **`db/`:** If you decide to use a different database or need more complex session management, you can modify the code here.

By following these principles, you can build a clean, scalable, and maintainable backend for your project.

Happy hacking!