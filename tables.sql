CREATE TABLE user(
    email varchar(50),
    last_name varchar(50)NOT NULL,
    first_name varchar(50)NOT NULL,
    username varchar(50)NOT NULL,
    password varchar(32) NOT NULL,
    primary key (email)
);

CREATE TABLE tasks(
    task_name varchar(255),
    task_desc varchar(255)
);