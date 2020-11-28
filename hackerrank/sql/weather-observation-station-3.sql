-- =============================================
-- Problem: https://www.hackerrank.com/challenges/weather-observation-station-3
-- Author: Shovra Das
-- =============================================

SELECT DISTINCT CITY FROM STATION WHERE BITAND(ID,1)=0;