/* Run the script to intialize diary database

Usage
-----
$ mysql -u youruser -p < setup.sql

*/

CREATE DATABASE IF NOT EXISTS diarydatabase;

USE diarydatabase;

CREATE TABLE IF NOT EXISTS diary (
    id INT UNSIGNED AUTO_INCREMENT,
    date DATE NOT NULL,
    content LONGTEXT NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS tag (
    id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS diary_tag (
    diary_id INT UNSIGNED NOT NULL,
    tag_id INT UNSIGNED NOT NULL
);