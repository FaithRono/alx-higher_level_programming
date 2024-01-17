-- Create table if it does not exist
CREATE TABLE IF NOT EXISTS `id_not_null` (
  `id` INT DEFAULT 1,
  `name` VARCHAR(256)
);

-- Insert data into the table
INSERT INTO `id_not_null` (`id`, `name`) VALUES (89, 'Best School');

-- Select data from the table
SELECT * FROM `id_not_null`;
