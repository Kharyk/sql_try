
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    age INT,
    student_id INT
);

CREATE TABLE curs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    course_id INT
);

CREATE TABLE many_to_many(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES curs (id)
);
