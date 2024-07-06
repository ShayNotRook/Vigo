# Vigo

Vigo is a web application designed to offer a wide range of gaming products, including games, gift cards, keys, and more. This project is currently in the local development phase.

## Table of Contents

- [About](#about)
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About

Vigo is an e-commerce platform dedicated to providing a diverse selection of gaming products. Whether you're looking for the latest game releases, gift cards, or game keys, Vigo has you covered.

## Features

- Browse a wide range of gaming products
- Search for specific games or products
- Add products to your cart
- Manage user profiles
- Secure checkout process (upcoming feature)

## Technologies

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (development), PostgreSQL (planned for production)
- **Other**: Font Awesome for icons

## Setup

To set up the project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/vigo.git
    cd vigo
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the application:**
    Open your web browser and go to `http://localhost:8000`

## Usage

### Running the Server

To start the development server, run:
```bash
python manage.py runserver
