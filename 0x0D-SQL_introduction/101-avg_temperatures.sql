-- Script to display average temperature (Fahrenheit) by city
USE hbtn_0c_0;

-- Display the result
SELECT city, AVG(temp_f) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
