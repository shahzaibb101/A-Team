CREATE TABLE user(
    id int PRIMARY KEY,
    LastName varchar(255),
    FirstName varchar(255),
    username varchar(255),
    password varchar(255)
);

CREATE TABLE tasks(
    task_name varchar(255),
    task_desc varchar(255)
);