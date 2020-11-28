-- =============================================
-- Problem: https://www.hackerrank.com/challenges/weather-observation-station-4
-- Author: Shovra Das
-- =============================================

SELECT COUNT(CITY)-COUNT(DISTINCT CITY) FROM STATION;