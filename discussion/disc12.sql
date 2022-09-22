CREATE TABLE record AS
SELECT 'Ben Bitdiddle'   AS name,
       'Computer'        AS division,
       'Wizard'          AS title,
       60000             AS salary,
       'Oliver Warbucks' AS supervisor
UNION
SELECT 'Alyssa P Hacker', 'Computer', 'Programmer', 40000, 'Ben Bitdiddle'
UNION
SELECT 'Cy D Fect', 'Computer', 'Programmer', 35000, 'Ben Bitdiddle'
UNION
SELECT 'Lem E Tweakit', 'Computer', 'Technician', 25000, 'Ben Bitdiddle'
UNION
SELECT 'Louis Reasoner', 'Computer', 'Programmer Trainee', 30000, 'Alyssa P Hacker'
UNION
SELECT 'Oliver Warbucks', 'Administration', 'Big Wheel', 150000, 'Oliver Warbucks'
UNION
SELECT 'Eben Scrooge', 'Accounting', 'Chief Accountant', 75000, 'Oliver Warbucks'
UNION
SELECT 'Robert Cratchet', 'Accounting', 'Scrivener', 18000, 'Eben Scrooge';

/* 2.1 Write a query that outputs the names of employees that Oliver Warbucks directly
supervises.*/
SELECT name
from record
where supervisor = 'Oliver Warbucks'
  and name != 'Oliver Warbucks';

/* 2.2 Write a query that outputs all information about employees that supervise
themselves. */
select *
from record
where name = supervisor;

/* 2.3 Write a query that outputs the names of all employees with salary greater than
50,000 in alphabetical order. */
select name
from record
where salary > 50000
order by name;

create table meetings as
select 'Accounting' as division, 'Monday' as day, '9am' as time
union
select 'Computer', 'Wednesday', '4pm'
union
select 'Administration', 'Monday', '11am'
union
select 'Administration', 'Wednesday', '4pm';

/* 3.1 Write a query that outputs the meeting days and times of all employees directly
supervised by Oliver Warbucks. */

select b.division, b.day
from record as a,
     meetings as b
where a.division = b.division
  and a.supervisor = 'Oliver Warbucks'
  and a.name != 'Oliver Warbucks';

/* 3.2 Write a query that outputs the names of all pairs of employees that have a meeting
at the same time. Make sure that if A|B appears in your output, B|A does not
appear as well (A|A and B|B should additionally not appear). */
with full_info(name, meeting_day, meeting_time) as (select a.name,
                                                           b.day,
                                                           b.time
                                                    from record as a,
                                                         meetings as b
                                                    where a.division = b.division)
select a.name, b.name
from full_info as a,
     full_info as b
where a.name < b.name
  and a.meeting_day = b.meeting_day
  and a.meeting_time = a.meeting_time;

/* 3.4  Write a query that outputs the names of employees whose supervisor is in a different
   division.
*/
select a.name
from record as a,
     record as b
where a.supervisor = b.name
  and a.division <> b.division;

/* 4.1 Write a query that outputs each supervisor and the sum of salaries of all the employees
   they supervise.
 */
select supervisor, sum(salary)
from record
group by supervisor;

/* 4.2 Write a query that outputs the days of the week for which fewer than 5 employees
have a meeting. You may assume no department has more than one meeting on a
given day. */
select day
from meetings as m,
     record as r
where r.division = m.division
group by day
having count(*) < 5;

/* 4.3 Write a query that outputs all divisions for which there is more than one employee,
and all pairs of employees within that division that have a combined salary less
than 100,000. */
with pairs(name0, salary0, name1, salary1, division) as
         (select a.name, a.salary, b.name, b.salary, a.division
          from record as a,
               record as b
          where a.division = b.division
            and a.name < b.name)
select division, name0 || ', ' || name1
from pairs
where salary0 + salary1 < 100000;

create table courses as
select 'John DeNero' as Professor, 'CS 61C' as Course, 'Sp20' as Semester
union
select 'John DeNero', 'CS 61A', 'Fa19'
union
select 'Dan Garcia', 'CS 61C', 'Sp19'
union
select 'John DeNero', 'CS 61A', 'Fa18'
union
select 'Dan Garcia', 'CS 10', 'Fa18'
union
select 'Josh Hug', 'CS 61B', 'Sp18'
union
select 'John DeNero', 'CS 61A', 'Sp18'
union
select 'John DeNero', 'CS 61A', 'Fa17'
union
select 'Paul Hilfinger', 'CS 61A', 'Fa17'
union
select 'Paul Hilfinger', 'CS 61A', 'Sp17'
union
select 'John DeNero', 'Data 8', 'Sp17'
union
select 'Josh Hug', 'CS 61B', 'Sp17'
union
select 'Satish Rao', 'CS 70', 'Sp17'
union
select 'Nicholas Weaver', 'CS 61C', 'Sp17'
union
select 'Gerald Friedland', 'CS 61C', 'Sp17';

/* 5.1 Create a table called num_taught that contains three columns: professor, the
course they taught, and the number of times they taught each course. */
create table num_taught as
select professor, course, count(*) as count
from courses
group by professor, course;

/* 5.2 Write a query that outputs two professors and a course if they have taught that
course the same number of times. You may use the num taught table you created
in the previous question. */
select a.professor as prof0, b.professor as prof1, a.course
from num_taught as a,
     num_taught as b
where a.professor < b.professor
  and a.course = b.course
  and a.count = b.count;

/* 5.3 Write a query that outputs two professors if they co-taught (taught the same course
at the same time) the same course more than once. */
select a.Professor as prof0, b.Professor as pro1
from courses as a,
     courses as b
where a.Professor < b.Professor
  and a.Course = b.Course
  and a.Semester = b.Semester
group by prof0, pro1, a.Course
having count(*) > 1;
