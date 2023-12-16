-- SQL script that creates a trigger that decreases the quantity 
-- of an item after adding a new order

DELIMITER $$
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON `orders` 
FOR EACH ROW
BEGIN 
	-- Decr quantity in items table for corresponding item_name
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
END;

$$
DELIMITER ;
