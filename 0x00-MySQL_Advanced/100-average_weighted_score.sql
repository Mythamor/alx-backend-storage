-- Create the stored procedure ComputeAverageWeightedScoreForUser

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN w_user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_weighted_score FLOAT;

    -- Compute total score and weight for user
    SELECT SUM(c.score * p.weight), SUM(p.weight)
    INTO total_score, total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = w_user_id;

    -- Compute average weighted score
    IF total_weight > 0 THEN
        SET avg_weighted_score = total_score / total_weight;
    ELSE
        SET avg_weighted_score = 0;
    END IF;

    -- Update the average_score for the user
    UPDATE users
    SET average_score = avg_weighted_score
    WHERE id = w_user_id;
END $$

DELIMITER ;

