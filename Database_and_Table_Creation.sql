-- Create database
CREATE DATABASE IF NOT EXISTS bookstoscrape;
USE bookstoscrape; -- Set the current database context to 'bookstoscrape'

-- Create categories table
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique ID for each category (auto-incremented)
    category_name VARCHAR(255) UNIQUE NOT NULL   -- Name of the category (must be unique and not null)
);

-- Create books table
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each book (auto-incremented)
    book_name VARCHAR(255) NOT NULL,          
    category_id INT,                          -- Foreign key reference to categories table
    price DECIMAL(10, 2),                     -- decimal format to handle currency
    stock INT,
    rating INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)   -- Defining foreign key constraint to enforce referential integrity
);

SELECT * from categories;
SELECT * from books;