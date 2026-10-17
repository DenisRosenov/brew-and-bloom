# Brew & Bloom ☕

Brew & Bloom is a Django web application created for coffee lovers. It provides a place to explore coffee beans, discover brewing methods, and create and manage coffee recipes.

## Features

- **Coffee Catalog** — browse, add, edit, view, and delete coffee entries.
- **Flavor Tags** — organize coffee recipes by their flavor profiles.
- **Brewing Methods** — explore and manage different coffee preparation methods.
- **Coffee Recipes** — create, view, edit, and delete recipes.
- **Recipe Details** — view ingredients, instructions, preparation time, ratings, and related coffee information.
- **Form Validation** — validate user input and display helpful feedback.
- **Custom Error Page** — a personalized 404 page matching the website design.
- **Responsive Design** — a clean interface built with Bootstrap and custom CSS.

## Technologies

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- SQLite

## Project Structure

The application is organized into three Django apps:

- `catalog` — coffee entries and flavor tags.
- `brewing` — brewing methods.
- `recipes` — coffee recipes and their relationships with coffee entries, brewing methods, and flavor tags.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the example values with your actual GitHub repository URL and project folder name.

### 2. Create and activate a virtual environment

On macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Django

```bash
python -m pip install django
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Database Relationships

- A recipe references a coffee entry.
- A recipe references a brewing method.
- A recipe can have multiple flavor tags, and a flavor tag can be associated with multiple recipes.

These relationships connect the main parts of the application and help keep the data organized.

## Purpose

Brew & Bloom was developed as a Django project to demonstrate model relationships, validated ModelForms, CRUD operations, reusable templates, template inheritance, static styling, and custom error handling.