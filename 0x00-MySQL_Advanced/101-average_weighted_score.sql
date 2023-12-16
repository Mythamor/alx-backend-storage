-- Create the stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE avg_weighted_score FLOAT;

    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN cur;

    -- Loop through each user
    user_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE user_loop;
        END IF;

        -- Compute total score and weight for user
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_score, total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Compute average weighted score
        IF total_weight > 0 THEN
            SET avg_weighted_score = total_score / total_weight;
        ELSE
            SET avg_weighted_score = 0;
        END IF;

        -- Update the average_score for the user
        UPDATE users
        SET average_score = avg_weighted_score
        WHERE id = user_id;
    END LOOP;

    CLOSE cur;
END $$

DELIMITER ;
