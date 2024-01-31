CREATE TABLE User(
    email varchar(50),
    last_name varchar(50) NOT NULL,
    first_name varchar(50) NOT NULL,
    username varchar(50) NOT NULL,
    password varchar(32) NOT NULL,
    primary key(email)
);

CREATE TABLE Tasks(
    task_id int,
    email varchar(50),
    task_name varchar(50) NOT NULL,
    task_desc varchar(255) NOT NULL,
    foreign key(email) references User(email),
    primary key(task_id,email)
);

