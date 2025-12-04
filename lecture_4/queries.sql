-- Remove tables if they already exist (clean reset)
DROP TABLE IF EXISTS grades;
DROP TABLE IF EXISTS students;

-- Create table for students
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Unique student ID
    full_name TEXT UNIQUE NOT NULL,         -- Full name (must be unique)
    birth_year INTEGER NOT NULL             -- Year of birth
);

-- Create table for grades
CREATE TABLE IF NOT EXISTS grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,   -- Unique grade ID
    student_id INTEGER,                     -- Foreign key: student ID
    subject TEXT NOT NULL,                  -- Subject name
    grade INTEGER CHECK(grade BETWEEN 1 AND 100), -- Grade (1–100)
    FOREIGN KEY(student_id) REFERENCES students(id)
);

-- Insert students; ignore duplicates
INSERT OR IGNORE INTO students (full_name, birth_year) 
VALUES 
    ('Alice Johnson', 2005),
    ('Brian Smith', 2004),
    ('Carla Reyes', 2006),
    ('Daniel Kim', 2005),
    ('Eva Thompson', 2003),
    ('Felix Nguyen', 2007),
    ('Grace Patel', 2005),
    ('Henry Lopez', 2004),
    ('Isabella Martinez', 2006);

-- Insert grades for each student
INSERT INTO grades (student_id, subject, grade) 
VALUES 
    (1, 'Math', 88),
    (1, 'English', 92),
    (1, 'Science', 85),
    (2, 'Math', 75),
    (2, 'History', 83),
    (2, 'English', 79),
    (3, 'Science', 95),
    (3, 'Math', 91),
    (3, 'Art', 89),
    (4, 'Math', 84),
    (4, 'Science', 88),
    (4, 'Physical Education', 93),
    (5, 'English', 90),
    (5, 'History', 85),
    (5, 'Math', 88),
    (6, 'Science', 72),
    (6, 'Math', 78),
    (6, 'English', 81),
    (7, 'Art', 94),
    (7, 'Science', 87),
    (7, 'Math', 90),
    (8, 'History', 77),
    (8, 'Math', 83),
    (8, 'Science', 80),
    (9, 'English', 96),
    (9, 'Math', 89),
    (9, 'Art', 92);

-- Index to speed up queries filtering by birth year
CREATE INDEX IF NOT EXISTS idx_students_birth_year
ON students(birth_year);

-- Get all grades for Alice Johnson
SELECT students.full_name, grades.subject, grades.grade
FROM grades
JOIN students ON students.id = grades.student_id
WHERE students.full_name = 'Alice Johnson';

-- Average grade for each student
SELECT students.full_name, AVG(grades.grade) AS average_grade
FROM grades
JOIN students ON students.id = grades.student_id
GROUP BY students.id;

-- Get students born after 2004
SELECT * FROM students
WHERE birth_year > 2004;

-- Average grade for each subject
SELECT subject, AVG(grade) AS average_grade
FROM grades
GROUP BY subject;

-- Top 3 students by average grades
SELECT students.full_name, AVG(grades.grade) AS avg_grade
FROM grades
JOIN students ON students.id = grades.student_id
GROUP BY students.id
ORDER BY avg_grade DESC
LIMIT 3;

-- All grades below 80
SELECT DISTINCT students.full_name, grades.subject, grades.grade
FROM grades
JOIN students ON students.id = grades.student_id
WHERE grades.grade < 80;