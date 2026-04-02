# Write your MySQL query statement below
SELECT customer_number 
from Orders 
GROUP BY customer_number
Order by count(*) Desc
Limit 1;