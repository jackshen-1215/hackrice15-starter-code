# Social Impact Track

This track focuses on leveraging technology to address pressing social and environmental problems.

## Sample Module: Resource Locator

To help you get started, we've built a sample module for a **Resource Locator**. This tool allows you to create and list essential resources like food banks, shelters, or legal aid services.

### Module Structure

The code for this module is organized as follows:

*   `models/resource.py`: Defines the `Resource` database table using SQLAlchemy.
*   `schemas/resource.py`: Defines the Pydantic schemas for data validation and serialization.
*   `crud/resource.py`: Contains the functions for creating, reading, updating, and deleting resources from the database.
*   `api/endpoints/resources.py`: Defines the API endpoints for interacting with resources.
*   `api/api.py`: The main router for this track, which groups all related endpoints.

### Integration and Usage

This module has already been integrated into the main application. Here's how it works and how you can test it:

1.  **Database Setup:** The `Resource` model is a standard SQLAlchemy model. When you first run the application, the database tables will be created automatically. If you make changes to the model, you will need to manage database migrations.

2.  **API Endpoints:** The following endpoints are available:

    *   `POST /api/v1/track_specific/social_impact/resources/`: Create a new resource.
    *   `GET /api/v1/track_specific/social_impact/resources/`: Get a list of all resources.

3.  **Testing with cURL:**

    *   **Create a resource:**

        ```bash
        curl -X 'POST' \
          'http://127.0.0.1:8000/api/v1/track_specific/social_impact/resources/' \
          -H 'accept: application/json' \
          -H 'Content-Type: application/json' \
          -d '{
          "name": "City Food Bank",
          "category": "Food",
          "address": "123 Main St, Anytown, USA",
          "phone_number": "555-1234",
          "website": "http://foodbank.example.com",
          "description": "Provides free meals and groceries."
        }'
        ```

    *   **Get all resources:**

        ```bash
        curl -X 'GET' \
          'http://127.0.0.1:8000/api/v1/track_specific/social_impact/resources/' \
          -H 'accept: application/json'
        ```

## Your Turn: Potential Modules

Now it's your turn to build something amazing! Here are some other ideas for this track:

*   **Community Platform:** A platform to connect volunteers with local organizations and initiatives.
*   **Donation and Fundraising Tracker:** A system for non-profits to manage donations and run fundraising campaigns transparently.
*   **Advocacy and Awareness Tool:** A platform to launch and manage campaigns, petitions, and educational content about specific social issues.