-- Create holberton database if it doesn't exist.
-- Creates the table - users if it doesn't exist.
CREATE DATABASE IF NOT EXISTS holberton;
USE holberton;
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
)
