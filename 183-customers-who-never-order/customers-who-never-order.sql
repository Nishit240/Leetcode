# Write your MySQL query statement below
SELECT c.name Customers
FROM Customers c 
left JOIN Orders o
ON c.id = o.customerId
WHERE o.id iS null;