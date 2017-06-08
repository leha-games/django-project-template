CREATE DATABASE {{ project_name }} ENCODING 'UTF-8' LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8' TEMPLATE template0;
CREATE USER {{ project_name }} WITH PASSWORD 'password';
ALTER ROLE {{ project_name }} SET client_encoding TO 'utf8';
ALTER ROLE {{ project_name }} SET default_transaction_isolation TO 'read committed';
ALTER ROLE {{ project_name }} SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE {{ project_name }} TO {{ project_name }};
