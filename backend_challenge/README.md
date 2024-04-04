# Backend Developer Challenge

Thank you for your interest in the Backend Developer position at AAK Tele-Science. This coding challenge is designed to assess your skills in developing a Django and Django Rest Framework (DRF) backend. Please follow the instructions below and deliver your work on a GitHub repository.

## Project Description

You are tasked with building a backend for a simple task management system. The application should include at least `Task` and `Label` models, and you need to expose API endpoints for CRUD operations on these models.

## Instructions

1. Fork this repository to your GitHub account.

2. Create a new Django project within your forked repository.

3. Implement a Django app for managing tasks called `tasks`.

4. Create at least two models:
   - `Task`:  This model should have a title, description, completion status, owner, and a many-to-many relationship to `Label`. 
   - `Label`: This model should have a name and owner. Add the necessary constraints to avoid duplicate values.

5. Implement API endpoints for CRUD operations on both `Task` and `Label` models. Use Django Rest Framework for creating these APIs.

6. Implement user authentication and authorization for the API. Users should only be able to perform CRUD operations on their tasks and labels.

> [!TIP]
> Create 2 users with the `python manage.py shell` command with the `is_staff` flag set to `True` so you can use the built-in admin site to log in. Detail the user's credentials on the `challenge.md` file. 

7. Include clear instructions on how to set up and run your project locally in a file called `challenge.md`.

8. Commit your changes regularly and provide meaningful commit messages.

9. Push your code to your GitHub repository.

## Bonus Points

- Write custom filters for the list view of the `Task` and `Label` models to only show your resources (the ones related to the user that's making the request).

- Write tests for your models and API endpoints.

## Review Criteria

- **Code Quality:**
  - Readability: Ensure the code is well-organized and follows the PEP 8 style guide.
  - Modularity: Divide code into modular components for easy understanding and maintenance.
  - Best Practices: Adhere to Django best practices and guidelines.

- **Functionality:**
  - Correctness: Ensure the application meets specified requirements and functions as expected.
  - Completeness: Implement all specified features and API endpoints.
  - Performance: Considerations for optimizing performance, especially in API endpoints.

- **Documentation:**
  - Setup Instructions: Document how to set up and run the project locally.
  - Code Comments: Add comments where necessary to explain complex logic.

- **Bonus Points:**
  - Creativity: Showcase creativity in bonus features or enhancements.
  
## Submission

Once you have completed the challenge, please send us the link to your GitHub repository. Make sure to include any relevant instructions for running the application and any additional notes you'd like to share on the `challenge.md` file.

> [!IMPORTANT]
> You will have 72 hours to complete this challenge.

Thank you, and good luck!

