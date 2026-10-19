# Brew & Bloom ☕

Brew & Bloom is a Django web application created for coffee lovers. It provides a place to explore coffee beans, discover brewing methods, and create and manage coffee recipes.

## Features

- **Coffee Catalog** — browse, add, view, edit, and delete coffee entries.
- **Flavor Tags** — organize recipes by their flavor profiles.
- **Brewing Methods** — explore and manage different coffee preparation methods.
- **Coffee Recipes** — create, view, edit, and delete coffee recipes.
- **Recipe Details** — view ingredients, instructions, preparation time, ratings, and related coffee information.
- **Form Validation** — validate user input and display helpful feedback.
- **Delete Confirmation** — confirm deletion before removing records.
- **Custom Error Page** — a personalized 404 page matching the website design.
- **Responsive Design** — a clean interface built with Bootstrap 5 and custom CSS.

## Technologies

- Python
- Django
- HTML5
- CSS3
- Bootstrap 5
- SQLite

## Project Structure

The project is organized into three Django apps:

- `catalog` — manages coffee entries and flavor tags.
- `brewing` — manages brewing methods.
- `recipes` — manages recipes and their relationships with coffees, brewing methods, and flavor tags.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/DenisRosenov/brew-and-bloom.git
cd brew-and-bloom
```

### 2. Create and activate a virtual environment

On macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
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

- Each recipe references a coffee entry.
- Each recipe references a brewing method.
- A recipe can have multiple flavor tags, and each flavor tag can be associated with multiple recipes.

These relationships demonstrate the use of Django foreign keys and many-to-many relationships.

## Purpose

Brew & Bloom was developed as a Django project to demonstrate model relationships, validated forms, CRUD operations, reusable templates, template inheritance, static styling, and custom error handling.

## Repository

GitHub: https://github.com/DenisRosenov/brew-and-bloom
