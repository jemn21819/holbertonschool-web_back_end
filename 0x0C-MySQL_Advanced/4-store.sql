--
--
CREATE TRIGGER after_new_order
AFTER
INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - new.number
where items.name = new.item_name;