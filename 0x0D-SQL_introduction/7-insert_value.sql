USE hbtn_0c_0;

-- Create the first_table if it doesn't exist
CREATE TABLE IF NOT EXISTS first_table (
  id INT,
  name VARCHAR(255)
);

-- Check if the new row already exists
SELECT * FROM first_table WHERE id = 89 AND name = 'Best School';

-- Insert the new row if it doesn't exist
INSERT INTO first_table (id, name)
SELECT * FROM (SELECT 89, 'Best School') AS tmp
WHERE NOT EXISTS (
  SELECT id, name FROM first_table WHERE id = 89 AND name = 'Best School'
);
