# PS C:\Lab uni studies\ICT SEMESTER 2\Oops Python> mysqladmin -u root -p status
# Enter password: *******
# Uptime: 9063  Threads: 4  Questions: 108  Slow queries: 0  Opens: 174  Flush tables: 3  Open tables: 93  Queries per second avg: 0.011
# PS C:\Lab uni studies\ICT SEMESTER 2\Oops Python> mysql -u root -p
# Enter password: *******
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 14
# Server version: 8.0.45 MySQL Community Server - GPL

# Copyright (c) 2000, 2026, Oracle and/or its affiliates.

# Oracle is a registered trademark of Oracle Corporation and/or its
# affiliates. Other names may be trademarks of their respective
# owners.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

# mysql> create database classtasks11-3-26
#     -> \>
# ERROR: 
# Unknown command '\>'.
#     ->
#     -> \.
# ERROR: 
# Usage: \. <filename> | source <filename>
#     -> >\
#     -> <\
#     -> \<
# ERROR: 
# Unknown command '\<'.
#     -> \>
# ERROR: 
# Unknown command '\>'.
#     -> |>
#     -> \c 
# mysql>  create database classtasks11-3-26;
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '-3-26' at line 1
# mysql>  create database classtask1;      
# Query OK, 1 row affected (0.02 sec)

# mysql> create table Task (id INT AUTO_INCREMENT Primary key, name VARCHAR(50) NOT NULL, description VARCHAR(150
# ) );
# ERROR 1046 (3D000): No database selected
# mysql> use classtask1;
# Database changed
# mysql> create table Task (id INT AUTO_INCREMENT Primary key, name VARCHAR(50) NOT NULL, description VARCHAR(150) );
# Query OK, 0 rows affected (0.03 sec)

# mysql> create table student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, birthday DATE, major
#  VARCHAR(50) );
# Query OK, 0 rows affected (0.02 sec)

# mysql> create table credits (id INT AUTO-INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL , date DATE, grade INT, credits INT)
#     -> ;
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'AUTO-INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL , da' at line 1
# mysql> create table credits (id INT AUTO-INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL , date DATE, grade INT, credits INT);
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'AUTO-INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL , da' at line 1
# mysql> create table credits (id INT AUTO-INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL , course_date DATE, grade INT, credits INT);
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'AUTO-INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL , co' at line 1
# mysql> create table credits (id INT AUTO_INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL
#  , date DATE, grade INT, credits INT);       
# Query OK, 0 rows affected (0.03 sec)

# mysql> create table course (id INT AUTO_INCREMENT Primary key, name VARCHAR(50) NOT NULL, description VARCHAR(150) );
# Query OK, 0 rows affected (0.02 sec)

# mysql> create table CourseAssignment (id INT AUTO_INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL
#     ->  \c
# mysql> id INT AUTO_INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL
#     -> id INT AUTO_INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL
#     ->  id INT AUTO_INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL
#     ->  vid INT AUTO_INCREMENT PRIMARY KEY, id_course INT NOT NULL, id_student INT NOT NULL
#     ->  \c
# mysql> create table CourseAssignment (id INT AUTO_INCREMENT PRIMARY KEY, id_task INT NOT NULL, id_course INT NO
# T NULL); 
# Query OK, 0 rows affected (0.02 sec)

# mysql> create table TaskCompletion (id INT AUTO_INCREMENT PRIMARY KEY, id_courseAssignment INT NOT NULL, id_student  INT NOT NULL, time TIME)
#     -> \c
# mysql> create table TaskCompletion (id INT AUTO_INCREMENT PRIMARY KEY, id_courseAssignment INT NOT NULL, id_student  INT NOT NULL, time TIME);
# Query OK, 0 rows affected (0.02 sec)

# mysql> .schema classtask1
#     -> \c
# mysql> .schema classtask1;
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '.schema classtask1' at line 1
# mysql> USE classtasks1;
# ERROR 1049 (42000): Unknown database 'classtasks1'
# mysql> SHOW TABLES;
# +----------------------+
# | Tables_in_classtask1 |
# +----------------------+
# | course               |
# | courseassignment     |
# | credits              |
# | student              |
# | task                 |
# | taskcompletion       |
# +----------------------+
# 6 rows in set (0.01 sec)

# mysql> select * from course;
# ERROR 2013 (HY000): Lost connection to MySQL server during query
# No connection. Trying to reconnect...
# Connection id:    15
# Current database: classtask1

# Empty set (0.15 sec)

# mysql> select * from course;
# Empty set (0.00 sec)

# mysql> select * from student;
# Empty set (0.00 sec)

# mysql> Insert into student (name, birthday, major) Values ("Alex", 28-02-2005, "Computer Science");
# ERROR 1292 (22007): Incorrect date value: '-1979' for column 'birthday' at row 1
# mysql> INSERT INTO student (name, birthday, major) VALUES ('Alex', '2005-02-28', 'Computer Science'),('Emma', '2004-06-15', 'Mathematics'),('John', '2003-11-20', 'Physics'),('Sophia', '2005-01-10', 'Engineering');         
# Query OK, 4 rows affected (0.02 sec)
# Records: 4  Duplicates: 0  Warnings: 0

# mysql> select * from student
#     -> \c
# mysql> select * from student;
# +----+--------+------------+------------------+
# | id | name   | birthday   | major            |
# +----+--------+------------+------------------+
# |  1 | Alex   | 2005-02-28 | Computer Science |
# |  2 | Emma   | 2004-06-15 | Mathematics      |
# |  3 | John   | 2003-11-20 | Physics          |
# |  4 | Sophia | 2005-01-10 | Engineering      |
# +----+--------+------------+------------------+
# 4 rows in set (0.00 sec)

# mysql> select * from student where name = alex
#     -> \c
# mysql> select * from student where name = alex
#     -> \c
# mysql> select * from student where name = alex;
# ERROR 1054 (42S22): Unknown column 'alex' in 'where clause'
# mysql> select * from student where name = Alex;
# ERROR 1054 (42S22): Unknown column 'Alex' in 'where clause'
# mysql> select * from student where name="Alex"'
#     '> \c
#     '> \;
#     '> \'
#     '> \c
#     '> \c
#     '> ');
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')' at line 7
# mysql> select from student where name='Alex';
# ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'from student where name='Alex'' at line 1
# mysql> select * from student where name='Alex';
# +----+------+------------+------------------+
# | id | name | birthday   | major            |
# +----+------+------------+------------------+
# |  1 | Alex | 2005-02-28 | Computer Science |
# +----+------+------------+------------------+
# 1 row in set (0.01 sec)
