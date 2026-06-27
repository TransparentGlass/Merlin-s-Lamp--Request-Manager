# Merlin's Lamp

A desktop request manager application (built with PyQt6) that allows users to submit requests to a public board, and allows administrators to manage them by setting priority and status.

## Main features

- **Public request board** — users submit requests with a title, content, and request type
- **Priority and status sorting** — requests can be filtered and sorted by priority, status, and request type simultaneously, with combinable filters
- **Upvoting** — users can upvote (and undo their vote on) existing requests
- **Separate user and admin views** — admins see an extended view of each request (`adminQFrame`) with controls regular users don't have, while regular users get a simpler view (`userQFrame`)
- **Full CRUD groundwork** — create, read, and update operations are implemented (submit, fetch with filters, update priority/status); delete is scaffolded but not yet implemented
- **Authentication** — user registration and login, with passwords hashed using `bcrypt` before being stored, never saved in plain text
- **Custom styling** — interface styled via an external `.qss` stylesheet, loaded at runtime

## Architecture

- **Frontend:** PyQt6, with UI defined in a `.ui` file (`merlins_lamp.ui`) and loaded dynamically at runtime
- **Backend:** A `databaseManager` class centralizes all database access through a small set of reusable methods (`execute_query`, `fetch_data`, `fetch_one`) so every read/write goes through the same error handling and connection management, rather than scattering raw queries throughout the app
- **Database:** MySQL, with the schema defined in a `create_tables.sql` file that's run automatically on startup if the tables don't already exist

## Setup

1. Create a MySQL database. [XAMPP](https://www.apachefriends.org/) works well for quickly spinning up a local MySQL service.
2. Open `src/backend/database.py` and update the `config` dictionary (`host`, `user`, `password`, `database`) to match your local database setup.
3. Run the program:
   ```bash
   python main.py
   ```
4. Create an account to start using the app.

## Known limitations

- `deleteRequest` is scaffolded in the database layer but not yet implemented
- Database credentials are currently hardcoded in `database.py` rather than loaded from environment variables — fine for local development, but worth moving to a `.env` file before sharing credentials or deploying anywhere shared

## Tech stack

- Python
- PyQt6
- MySQL
- bcrypt (password hashing)

## Codebase

[github.com/TransparentGlass/Merlin-s-Lamp--Request-Manager](https://github.com/TransparentGlass/Merlin-s-Lamp--Request-Manager)
