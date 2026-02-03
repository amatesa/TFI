# Inventory Management System (Python + SQLite)

This project is a console-based inventory management system developed in Python using SQLite for data persistence.

It was created as a **final academic project** to practice Python fundamentals, database interaction and modular code organization.

## Purpose

The goal of this project is to simulate a simple inventory management tool for small businesses.  
It allows users to register products, update stock and detect low inventory levels using a menu-driven console interface.

## Features

- Create and manage a local SQLite database.
- Add, update, delete and list products.
- Search products by ID.
- Check available stock.
- Generate a report of products with low stock.

## Project structure

- `db.py` – Database connection and initialization (creates the `productos` table).
- `funciones_crud.py` – CRUD operations and inventory logic.
- `menu.py` – Console menu and user interaction.

## Technologies used

- Python 3.x  
- SQLite3  
- colorama (for better visual output in the terminal)

## How to run

1. Make sure you have Python 3 installed.
2. Install the dependency:

```bash
pip install colorama

python menu.py
