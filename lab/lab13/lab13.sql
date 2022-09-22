.read data.sql


CREATE TABLE average_prices AS
SELECT category, avg(MSRP) as average_price
from products
group by category;


CREATE TABLE lowest_prices AS
SELECT store, item, min(price) as lowest_price
from inventory
group by item;


CREATE TABLE overall_rating AS
SELECT name, min(MSRP / products.rating) as rating
from products
group by category;


CREATE TABLE shopping_list AS
SELECT a.name, b.store
from overall_rating as a,
     lowest_prices as b
where a.name = b.item
order by a.name;


CREATE TABLE total_bandwidth AS
SELECT sum(Mbs)
from stores as a,
     shopping_list as b
where a.store = b.store;

