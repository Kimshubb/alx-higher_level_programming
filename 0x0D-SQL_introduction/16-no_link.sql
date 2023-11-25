-- lists all recordds of second table in desc order
USE hbtn_0c_0;

SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL
ORDER BY `score` DESC;
