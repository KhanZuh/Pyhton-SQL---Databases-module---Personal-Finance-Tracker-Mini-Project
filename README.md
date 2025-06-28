# Personal Finance Tracker
A Python-based terminal application for tracking personal expenses, built using Test-Driven Development principles and PostgreSQL database integration.

## 📋 Project Overview
This Personal Finance Tracker helps you manage your personal expenses by categorizing them and tracking spending against budget limits. The application demonstrates key software engineering concepts including database design, TDD, and proper separation of concerns using the Repository pattern.

## 🎯 Learning Objectives
This project reinforces these key concepts:

- SQL Practice: Complex SELECT, INSERT, DELETE, and JOIN queries
- Test-Driven Development: Full test coverage for models and repositories
- Database Schema Design: One-to-many relationships and foreign keys
- CRUD Operations: Complete Create, Read, Update, Delete functionality
- Sequence Diagrams: Document application-database communication

## ✨ Core Features

### Database Schema
Two-table design with one-to-many relationship:
- `categories` table: id, name, budget_limit
- `expenses` table: id, description, amount, date, category_id (foreign key)

### Application Features
1. View all categories with total spent vs budget comparison
2. Add new category with budget limit
3. View all expenses (with category names via JOIN queries)
4. Add new expense to an existing category
5. View expenses by category (filtered results)
6. Delete an expense
7. View monthly spending summary with analytics

## 🚀 Getting Started
### Prerequisites
- Python 3.8+
- PostgreSQL
- pytest (for testing)

💡Tip: Running pip freeze
```
pip freeze > requirements.txt
```
when first setting up makes it easier to collab with others

### Installation & Setup
1. Clone this repository
2. Install dependencies: pip install psycopg pytest
3. Set up your database connection (see Project Setup Guide)
4. Create the database: createdb finance_tracker
5. Run the setup: `python -c "from lib.database_connection import DatabaseConnection; db = DatabaseConnection(); db.connect(); db.seed('finance_tracker.sql')"`

### Environment Variables 
```bash
export POSTGRES_USER="your_username"
export POSTGRES_PASSWORD="your_password"
```

## 🏗️ Project Structure
```
finance_tracker/
├── lib/
│   ├── __init__.py
│   ├── database_connection.py    # Database connection utilities
│   ├── category.py              # Category model class
│   ├── expense.py               # Expense model class  
│   ├── category_repository.py   # Category CRUD operations
│   └── expense_repository.py    # Expense CRUD operations
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest configuration
│   ├── test_category.py        # Category model tests
│   ├── test_expense.py         # Expense model tests
│   ├── test_category_repository.py
│   ├── test_expense_repository.py
│   └── test_database_connection.py
├── app.py                      # Main terminal application
├── finance_tracker.sql         # Database schema and seed data
├── pytest.ini                 # Test configuration
└── README.md
```

## 🎨 Example Usage
```bash
$ python app.py

=== Personal Finance Tracker ===
1. View all categories
2. Add new category  
3. View all expenses
4. Add new expense
5. View expenses by category
6. Delete expense
7. Monthly summary
8. Exit

Enter choice: 1

Categories:
- Food (Budget: £300, Spent: £245, Remaining: £55)
- Transport (Budget: £150, Spent: £89, Remaining: £61)
- Entertainment (Budget: £100, Spent: £120, Over budget by: £20)
```


## 📚 Additional Resources
📋 [Project Setup Guide](Project_setup.md) - Detailed setup instructions  
🎯 [Design Recipe Template](design_recipe.md) - Step-by-step development guide

