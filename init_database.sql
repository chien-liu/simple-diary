/* Run the script to intialize diary database

Usage
-----
$ mysql -u youruser -p < setup.sql

*/

CREATE DATABASE IF NOT EXISTS diarydatabase;

USE diarydatabase;

CREATE TABLE diary (
    id INT UNSIGNED AUTO_INCREMENT,
    date DATE NOT NULL,
    content LONGTEXT NOT NULL,
    PRIMARY KEY(id),
    UNIQUE (date)
);

CREATE TABLE tag (
    id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(40) NOT NULL,
    PRIMARY KEY(id),
    UNIQUE (name)
);

CREATE TABLE diary_tag (
    diary_id INT UNSIGNED NOT NULL,
    tag_id INT UNSIGNED NOT NULL,
    UNIQUE (diary_id, tag_id)
);