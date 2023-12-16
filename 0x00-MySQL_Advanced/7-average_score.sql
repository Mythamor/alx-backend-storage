-- SQL script that creates a stored procedure that computes and stores
-- the average score for a student. Note: An average score can be a decimal

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN

    DECLARE p_total_score INT;
    DECLARE p_total_projects INT;
    DECLARE p_avg_score FLOAT;

    -- Compute total score and projects for user
    SELECT SUM(score),  COUNT(DISTINCT project_id)
    INTO p_total_score, p_total_projects
    FROM corrections
    WHERE user_id = p_user_id;


    -- Compute average score
    IF p_total_projects > 0 THEN
        SET p_avg_score = p_total_score / p_total_projects;
    ELSE
        SET p_avg_score = 0;
    END IF;

    -- Update the average_score for the user
    UPDATE users
    SET average_score = p_avg_score
    WHERE id = p_user_id;

END $$

DELIMITER ;

