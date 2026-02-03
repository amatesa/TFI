# Inventory Management System (Python + SQLite)

This project is a console-based inventory management system developed in Python using SQLite for data persistence.

It allows users to manage products through basic CRUD operations and monitor stock levels via a simple menu-driven interface.

## Features

- Create and manage a local SQLite database.
- Add, update, delete and list products.
- Check available stock.
- Identify products with low stock.
- Modular structure separating database logic, business logic and user interface.

## Project structure

- `db.py` – Database connection and initialization.
- `funciones_crud.py` – CRUD operations and inventory logic.
- `menu.py` – Console menu and user interaction.

## How to run

1. Make sure you have Python 3 installed.
2. Clone the repository or download the source code.
3. Run the main menu:

```bash
python menu.py
