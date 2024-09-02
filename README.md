# s3-flask_resume_generator
 
Resume Generator:

The Resume Generator is a web application built using Flask, a Python web framework, that allows users to create and download their resumes easily. The application collects user input such as personal details, education history, work experience, and skills through a user-friendly interface. Once the user submits their information, the application generates a resume in plain text format and uploads it to an AWS S3 bucket.

Features:
1)User-friendly Interface: The application provides a simple and intuitive interface for users to input their resume information.
Resume Generation: It dynamically generates a resume in plain text format based on the user's input.
2)AWS S3 Integration: Utilizes the AWS S3 service to securely store and manage uploaded resumes.
3)Download Resume: Allows users to download their generated resume directly from the application.

Technologies Used:
* Flask: Python web framework used for building the backend server and handling HTTP requests.
* HTML/CSS: Frontend components and styling for the user interface.
* Boto3: Python library used to interact with AWS services, specifically S3 for file storage.
* Git: Version control system for tracking changes to the project codebase.
* GitHub: Hosting platform for storing and sharing the project's Git repository.
  
Usage:
-   Users input their personal details, education history, work experience, and skills into the provided form.
-   Upon submission, the application generates a resume in plain text format based on the provided information.
-   The generated resume is uploaded to an AWS S3 bucket for secure storage.
-   Users can then download their resume directly from the application for further use.
  
Deployment:
- Clone the repository from GitHub.
- Install the necessary dependencies using pip.
- Configure AWS credentials and create an S3 bucket.
- Run the Flask application locally or deploy it to a cloud platform.
