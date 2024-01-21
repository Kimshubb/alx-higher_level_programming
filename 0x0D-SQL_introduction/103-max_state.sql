-- displays the max temperatures of each city ORDERED BY STATE NAME
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
