-- displays all records with the same score in second table IN DESC
USE hbtn_0c_0;
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
