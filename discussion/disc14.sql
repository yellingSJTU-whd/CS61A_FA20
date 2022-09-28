CREATE TABLE scoring AS
SELECT 'Donald Stewart' AS player, 7 AS points, 1 AS quarter
UNION
SELECT 'Christopher Brown Jr.', 7, 1
UNION
SELECT 'Ryan Sanborn', 3, 2
UNION
SELECT 'Greg Thomas', 3, 2
UNION
SELECT 'Cameron Scarlett', 7, 3
UNION
SELECT 'Nikko Remigio', 7, 4
UNION
SELECT 'Ryan Sanborn', 3, 4
UNION
SELECT 'Chase Garbers', 7, 4;

CREATE TABLE players AS
SELECT 'Ryan Sanborn' AS name, 'Stanford' AS team
UNION
SELECT 'Donald Stewart', 'Stanford'
UNION
SELECT 'Cameron Scarlett', 'Stanford'
UNION
SELECT 'Christopher Brown Jr.', 'Cal'
UNION
SELECT 'Greg Thomas', 'Cal'
UNION
SELECT 'Nikko Remigio', 'Cal'
UNION
SELECT 'Chase Garbers', 'Cal';

/* 8.1 Write a SQL statement to select a one-column table of quarters in which more than
10 total points were scored. */
select quarter
from scoring
group by quarter
having sum(points) > 10;

/* 8.2 Write a SQL statement to select a two-column table of the points scored by each
team. Assume that no two players have the same name. */
select team, sum(points)
from players,
     scoring
where players.name = scoring.player
group by team;