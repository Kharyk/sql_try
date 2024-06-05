
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            age INT,
            student_id INT
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS curs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50),
            course_id INT
        )
        ''')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS many_to_many (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INT,
            course_id INT,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES curs (id)
        )
        ''')
        self.conn.commit()

    def students_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def curs_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def fetchall_courses(self):
        self.cursor.execute("SELECT * FROM curs")
        return self.cursor.fetchall()

    def fetch_students_in_course(self, course_name):
        self.cursor.execute('''
        SELECT students.id, students.name, students.age
        FROM students
        JOIN many_to_many ON students.id = many_to_many.student_id
        JOIN curs ON many_to_many.course_id = curs.id
        WHERE curs.name = ?
        ''', (course_name,))
        return self.cursor.fetchall()

    def register_student(self, student_id, course_id):
        self.cursor.execute('''
        INSERT INTO many_to_many (student_id, course_id) VALUES (?, ?)
        ''', (student_id, course_id))
        self.conn.commit()
