-- create db hbtn_0d_2 if not exists
-- create user user_0d_2 if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'USER_0d_pass';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
