# Flask Superheroes API

A Flask-based REST API for tracking heroes and their superpowers. This project allows you to manage heroes, powers, and the associations between them through hero powers.

## Features

- **Heroes Management**: Create, read, and manage superhero profiles
- **Powers Management**: Handle various superpowers with descriptions
- **Hero-Powers Associations**: Link heroes to their powers with strength ratings
- **RESTful API**: Full CRUD operations with proper HTTP status codes
- **Data Validation**: Ensures data integrity with model validations
- **Database Migrations**: Uses Flask-Migrate for schema management

## Setup Instructions

1. **Clone the repository** (if not already done):

   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   Superheroes API — quick and chill

   Simple Flask API for heroes and powers. Run it and try the endpoints.

   Setup

   1. Make a venv and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   2. Install:

   ```bash
   pip install -r requirements.txt
   ```

   3. Migrate DB:

   ```bash
   export FLASK_APP=app.py
   flask db upgrade
   ```

   4. (Optional) Seed sample data:

   ```bash
   python seed.py
   ```

   5. Run the app:

   ```bash
   python app.py
   ```

   Main endpoints

   - GET /heroes
   - GET /heroes/:id
   - GET /powers
   - GET /powers/:id
   - PATCH /powers/:id
   - POST /hero_powers

   Quick notes

   - `Power.description` needs 20+ chars.
   - `HeroPower.strength` must be `Strong`, `Average`, or `Weak`.

   Use the Postman collection provided to test everything.

## Technologies Used
