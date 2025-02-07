# Photography Web Application

## Overview
This is a Flask-based web application designed to showcase photography portfolios. It allows photographers to display their work, organize photos into galleries, and provide information about themselves and their services.

## Key Features
- **Home Page:** A welcoming landing page with a brief introduction and a showcase of featured photographs.
- **Gallery Page:** A page to display photo galleries, each containing a collection of related photographs.
- **Individual Photo Pages:** Detailed pages for individual photos, providing more information about each shot.
- **About Page:** A page where photographers can introduce themselves and share their background, experience, and contact information.
- **Contact Page:** A form for visitors to reach out to the photographer for inquiries or booking services.

## Technologies Used
- **Flask:** A lightweight WSGI web application framework for Python.
- **HTML/CSS:** For structuring and styling the web pages.
- **JavaScript:** For interactivity and dynamic content.
- **SQLAlchemy:** An ORM for database management.

## File Structure
- `app.py:` The main Flask application script.
- `templates/:` Directory containing HTML templates.
- `static/:` Directory for static files such as CSS, JavaScript, and images.
- `requirements.txt:` A file listing the Python packages required for the application.
- `README.md:` Documentation with setup instructions and project details.

## Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/NagaSravyaMadduri/Photography-webapp.git

2. Navigate to the Project Directory
   ```sh
   cd Photography-weapplication

4. Create a Virtual Environment (optional but recommended)
   ```sh
   For Windows:
   python -m venv myenv
   myenv\Scripts\Activate
   For MacOS/Linux:
   python3 -m venv myenv
   source myenv/bin/activate

7. Install Dependencies Make sure you have pip installed, then install the required packages:
   ```sh
   pip install -r requirements.txt

9. Run the Application
    ```sh
   python app.py


