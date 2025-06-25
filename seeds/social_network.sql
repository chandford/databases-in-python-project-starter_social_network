DROP TABLE IF EXISTS accounts CASCADE;
DROP SEQUENCE IF EXISTS accounts_id_seq;

DROP TABLE IF EXISTS posts CASCADE;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS accounts_id_seq;
CREATE TABLE accounts (
  id SERIAL PRIMARY KEY,
  username VARCHAR(255),
  email_address VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  content TEXT,
  views INTEGER,
  account_id INT,
  CONSTRAINT fk_account FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

INSERT INTO accounts (username, email_address) VALUES 
('user1', 'user1@example.com'),
('user2', 'user2@example.com'),
('user3', 'user3@example.com'),
('user4', 'user4@example.com'),
('user5', 'user5@example.com'); 

INSERT INTO posts (title, content, views, account_id) VALUES 
('Post Title 1', 'Content for post 1.', 150, 1),
('Post Title 2', 'Content for post 2.', 200, 1),
('Post Title 3', 'Content for post 3.', 300, 2),
('Post Title 4', 'Content for post 4.', 250, 2),
('Post Title 5', 'Content for post 5.', 100, 3),
('Post Title 6', 'Content for post 6.', 180, 3),
('Post Title 7', 'Content for post 7.', 270, 4),
('Post Title 8', 'Content for post 8.', 450, 4),
('Post Title 9', 'Content for post 9.', 360, 5),
('Post Title 10', 'Content for post 10.', 220, 5);