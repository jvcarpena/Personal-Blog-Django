# Django Personal Blog Project

## Overview
This is a personal blog project built using Django, where users can browse blog posts, view details of each post, and explore various topics. The project uses Django's templating system to render pages dynamically.

## Features
- **Homepage**: Displays the latest three blog posts.
- **All Posts Page**: Lists all available blog posts.
- **Post Detail Page**: Shows the full content of a selected blog post.
- **Simple URL Routing**: Uses Django's path routing to navigate between pages.

## Technologies Used
- **Python** (Django Framework)
- **HTML & CSS** (for templates and styling)
- **Bootstrap** (for responsive UI, if applicable)
- **SQLite** (or any Django-supported database, if configured)

## Installation & Setup
1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   cd personal-blog
   ```
2. **Set up a virtual environment**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install django
   ```
4. **Run the Django development server**:
   ```sh
   python manage.py runserver
   ```
5. Open your browser and go to: `http://127.0.0.1:8000/`

## URLs and Views
- **Home Page (`/`)**: Displays the latest blog posts.
- **All Posts (`/posts`)**: Lists all blog posts.
- **Post Detail (`/posts/<slug>`)**: Displays a specific blog post.

## Future Enhancements
- Add a database model for dynamic post storage.
- Implement user authentication for blog authors.
- Add categories and tags for better content organization.
- Enable commenting and likes on posts.

## Author
**JV Carpena**

