-- Create table if it does not exist
CREATE TABLE IF NOT EXISTS `force_name` (
  `id` INT,
  `name` VARCHAR(256) NOT NULL
);

-- Insert data into the table
INSERT INTO `force_name` (`id`, `name`) VALUES (89, 'Best School');

-- Select data from the table
SELECT * FROM `force_name`;

