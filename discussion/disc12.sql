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
  and a.division != b.division;

/* 4.1 Write a query that outputs each supervisor and the sum of salaries of all the employees
   they supervise.
 */
with supervisor(name) as (select distinct supervisor from record)
select a.name, sum(b.salary)
from supervisor as a,
     record as b
where b.supervisor = a.name
group by b.supervisor;

/* 4.2 Write a query that outputs the days of the week for which fewer than 5 employees
have a meeting. You may assume no department has more than one meeting on a
given day. */
with days(name) as (select 'Sunday'
                    union
                    select 'Monday'
                    union
                    select 'Tuesday'
                    union
                    select 'Wednesday'
                    union
                    select 'Thursday'
                    union
                    select 'Friday'
                    union
                    select 'Saturday'),
     meetings_info(name, day) as (select a.name, b.day
                                  from record as a,
                                       meetings as b
                                  where a.division = b.division)
select a.name
from days as a,
     meetings_info as b
group by b.day
having count(distinct b.name) < 5;

create table meeting_info as
select a.name, b.day
from record as a,
     meetings as b
where a.division = b.division;