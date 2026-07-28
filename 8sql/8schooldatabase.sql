-- ============================================
-- SCHOOL DATABASE PROJECT
-- ============================================

-- Drop database if it already exists
DROP DATABASE IF EXISTS SchoolDB;

-- Create Database
CREATE DATABASE SchoolDB;

USE SchoolDB;

-- ============================================
-- TABLE: Teachers
-- ============================================

CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    subject_specialization VARCHAR(50),
    phone VARCHAR(15),
    email VARCHAR(100)
);

-- ============================================
-- TABLE: Students
-- ============================================

CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender ENUM('Male','Female','Other'),
    date_of_birth DATE,
    phone VARCHAR(15),
    email VARCHAR(100),
    address VARCHAR(200)
);

-- ============================================
-- TABLE: Classes
-- ============================================

CREATE TABLE Classes (
    class_id INT PRIMARY KEY AUTO_INCREMENT,
    class_name VARCHAR(20),
    section CHAR(1),
    class_teacher INT,
    FOREIGN KEY (class_teacher)
    REFERENCES Teachers(teacher_id)
);

-- ============================================
-- TABLE: Subjects
-- ============================================

CREATE TABLE Subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(50),
    teacher_id INT,
    FOREIGN KEY (teacher_id)
    REFERENCES Teachers(teacher_id)
);

-- ============================================
-- TABLE: Enrollments
-- ============================================

CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    class_id INT,
    admission_date DATE,
    FOREIGN KEY (student_id)
    REFERENCES Students(student_id),
    FOREIGN KEY (class_id)
    REFERENCES Classes(class_id)
);

-- ============================================
-- TABLE: Marks
-- ============================================

CREATE TABLE Marks (
    mark_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject_id INT,
    exam_type VARCHAR(30),
    marks INT CHECK (marks BETWEEN 0 AND 100),
    FOREIGN KEY (student_id)
    REFERENCES Students(student_id),
    FOREIGN KEY (subject_id)
    REFERENCES Subjects(subject_id)
);

-- ============================================
-- INSERT DATA INTO TEACHERS
-- ============================================

INSERT INTO Teachers
(first_name,last_name,subject_specialization,phone,email)
VALUES
('John','Smith','Mathematics','9876543210','john@school.com'),
('Mary','Joseph','Science','9876543211','mary@school.com'),
('David','Wilson','English','9876543212','david@school.com');

-- ============================================
-- INSERT DATA INTO STUDENTS
-- ============================================

INSERT INTO Students
(first_name,last_name,gender,date_of_birth,phone,email,address)
VALUES
('Rahul','Kumar','Male','2008-05-15','9000000001','rahul@gmail.com','Chennai'),
('Priya','Sharma','Female','2009-01-20','9000000002','priya@gmail.com','Coimbatore'),
('Arun','Raj','Male','2008-11-30','9000000003','arun@gmail.com','Madurai'),
('Sneha','Reddy','Female','2008-09-18','9000000004','sneha@gmail.com','Salem'),
('Kiran','Das','Male','2009-03-12','9000000005','kiran@gmail.com','Trichy');

-- ============================================
-- INSERT DATA INTO CLASSES
-- ============================================

INSERT INTO Classes
(class_name,section,class_teacher)
VALUES
('10','A',1),
('10','B',2);

-- ============================================
-- INSERT DATA INTO SUBJECTS
-- ============================================

INSERT INTO Subjects
(subject_name,teacher_id)
VALUES
('Mathematics',1),
('Science',2),
('English',3);

-- ============================================
-- INSERT DATA INTO ENROLLMENTS
-- ============================================

INSERT INTO Enrollments
(student_id,class_id,admission_date)
VALUES
(1,1,'2023-06-01'),
(2,1,'2023-06-01'),
(3,2,'2023-06-01'),
(4,2,'2023-06-01'),
(5,1,'2023-06-01');

-- ============================================
-- INSERT DATA INTO MARKS
-- ============================================

INSERT INTO Marks
(student_id,subject_id,exam_type,marks)
VALUES
(1,1,'Midterm',92),
(1,2,'Midterm',88),
(1,3,'Midterm',85),

(2,1,'Midterm',78),
(2,2,'Midterm',90),
(2,3,'Midterm',81),

(3,1,'Midterm',70),
(3,2,'Midterm',74),
(3,3,'Midterm',82),

(4,1,'Midterm',95),
(4,2,'Midterm',91),
(4,3,'Midterm',89),

(5,1,'Midterm',84),
(5,2,'Midterm',79),
(5,3,'Midterm',86);

-- ============================================
-- DISPLAY TABLES
-- ============================================

SHOW TABLES;

-- ============================================
-- VIEW ALL STUDENTS
-- ============================================

SELECT * FROM Students;

-- ============================================
-- VIEW ALL TEACHERS
-- ============================================

SELECT * FROM Teachers;

-- ============================================
-- VIEW ALL SUBJECTS
-- ============================================

SELECT * FROM Subjects;

-- ============================================
-- VIEW ALL CLASSES
-- ============================================

SELECT * FROM Classes;

-- ============================================
-- VIEW ALL ENROLLMENTS
-- ============================================

SELECT * FROM Enrollments;

-- ============================================
-- VIEW ALL MARKS
-- ============================================

SELECT * FROM Marks;

-- ============================================
-- STUDENTS WITH THEIR CLASS
-- ============================================

SELECT
s.student_id,
s.first_name,
s.last_name,
c.class_name,
c.section
FROM Students s
JOIN Enrollments e
ON s.student_id=e.student_id
JOIN Classes c
ON e.class_id=c.class_id;

-- ============================================
-- STUDENTS WITH THEIR MARKS
-- ============================================

SELECT
s.first_name,
sub.subject_name,
m.exam_type,
m.marks
FROM Marks m
JOIN Students s
ON s.student_id=m.student_id
JOIN Subjects sub
ON sub.subject_id=m.subject_id;

-- ============================================
-- AVERAGE MARKS OF EACH STUDENT
-- ============================================

SELECT
s.student_id,
s.first_name,
AVG(m.marks) AS Average_Marks
FROM Students s
JOIN Marks m
ON s.student_id=m.student_id
GROUP BY s.student_id,s.first_name;

-- ============================================
-- TEACHERS WITH SUBJECTS
-- ============================================

SELECT
sub.subject_name,
t.first_name,
t.last_name
FROM Subjects sub
JOIN Teachers t
ON sub.teacher_id=t.teacher_id;

-- ============================================
-- HIGHEST MARKS
-- ============================================

SELECT
s.first_name,
MAX(m.marks) AS Highest_Marks
FROM Students s
JOIN Marks m
ON s.student_id=m.student_id
GROUP BY s.student_id,s.first_name;

-- ============================================
-- LOWEST MARKS
-- ============================================

SELECT
s.first_name,
MIN(m.marks) AS Lowest_Marks
FROM Students s
JOIN Marks m
ON s.student_id=m.student_id
GROUP BY s.student_id,s.first_name;

-- ============================================
-- STUDENTS SCORING ABOVE 85
-- ============================================

SELECT
s.first_name,
sub.subject_name,
m.marks
FROM Students s
JOIN Marks m
ON s.student_id=m.student_id
JOIN Subjects sub
ON sub.subject_id=m.subject_id
WHERE m.marks>85;

-- ============================================
-- TOTAL STUDENTS
-- ============================================

SELECT COUNT(*) AS Total_Students
FROM Students;

-- ============================================
-- TOTAL TEACHERS
-- ============================================

SELECT COUNT(*) AS Total_Teachers
FROM Teachers;

-- ============================================
-- STUDENTS ORDERED BY NAME
-- ============================================

SELECT *
FROM Students
ORDER BY first_name;

-- ============================================
-- MARKS ORDERED DESCENDING
-- ============================================

SELECT
s.first_name,
sub.subject_name,
m.marks
FROM Students s
JOIN Marks m
ON s.student_id=m.student_id
JOIN Subjects sub
ON sub.subject_id=m.subject_id
ORDER BY m.marks DESC;

-- ============================================
-- END OF PROJECT
-- ============================================
