# Personal Finance Tracker - Project Setup Structure
## Overview
This project follows the Makers Academy standard project structure for database-backed Python applications. The setup is based on their proven starter template that separates concerns between data models, database operations, and application logic.

## Project Architecture
### 📁 Directory Structure
```
personal_finance_tracker/
├── lib/                     # Main application code
│   ├── __init__.py         # Makes lib a Python package
│   ├── database_connection.py  # Database connection layer
│   ├── category.py         # Category model class
│   ├── expense.py          # Expense model class
│   ├── category_repository.py  # Category database operations
│   └── expense_repository.py   # Expense database operations
├── tests/                   # All test files
│   ├── __init__.py         # Makes tests a Python package
│   ├── conftest.py         # Pytest configuration & fixtures
│   └── test_*.py files     # Individual test files
├── app.py                  # Main application entry point
├── pytest.ini             # Pytest configuration
├── database_connection.sql # Test database setup
└── finance_tracker.sql    # Main database schema
```
## Core Components Explained
### 🔌 DatabaseConnection Class (lib/database_connection.py)
This is a thin wrapper layer around the psycopg PostgreSQL library that provides:

- Connection Management: Handles connecting to PostgreSQL with error handling
- Environment Variables: Uses `POSTGRES_USER` and `POSTGRES_PASSWORD` for security
- SQL Execution: `execute()` method for running queries with parameters
- Database Seeding: `seed()` method for loading SQL files (useful for tests)

Key Methods:
- `connect()` - Establishes database connection
- `execute(query, params)` - Runs SQL queries safely with parameterization
- `seed(sql_filename)` - Loads and executes SQL from files

### 🧪 Testing Setup
`conftest.py` - Pytest Configuration
Contains a pytest fixture that automatically provides database connections to tests:

```python
@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    return conn
```
What this means: Any test function that accepts `db_connection` as a parameter will automatically receive a connected database instance.

`pytest.ini` - Test Configuration
Configures how pytest runs tests (specific settings depend on your project needs).

### 🏗️ Architecture Pattern: Repository Pattern
This project uses the Repository Pattern which separates:

Model Classes (`category.py`, `expense.py`)
- Represent data structures (like Category, Expense objects)
- Contain `__eq__` and `__repr__` methods for testing and debugging

Repository Classes (`category_repository.py`, `expense_repository.py`)
- Handle all database operations (CRUD: Create, Read, Update, Delete)
- Convert between database rows and model objects
- Keep SQL queries organized and reusable

Benefits:
1. Separation of Concerns: Data logic separate from business logic
2. Testability: Easy to test database operations in isolation
3. Maintainability: All SQL for a table in one place

### 📊 Database Files
- `finance_tracker.sql` - Your main database schema (tables, relationships)
- `database_connection.sql` - Test database setup (currently has example test_table)
