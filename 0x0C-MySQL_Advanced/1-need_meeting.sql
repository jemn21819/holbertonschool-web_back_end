--
--
CREATE VIEW need_meeting 
AS SELECT name FROM students
WHERE (score < 80) AND
(last_meeting < DATE_SUB(now(), INTERVAL 1 MONTH)
OR ISNULL(last_meeting));
