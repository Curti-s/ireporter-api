CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY NOT NULL,
    firstname VARCHAR(60) NOT NULL,
    lastname VARCHAR(60) NOT NULL,
    username VARCHAR(60) NOT NULL,
    email VARCHAR(60) NOT NULL,
    othernames VARCHAR(60),
    phone_number VARCHAR(60),
    registered TIMESTAMP DEFAULT now() NOT NULL,
    is_admin BOOL NOT NULL 
);

CREATE TYPE incident_type AS ENUM ('redflag','incident');

CREATE TYPE current_status AS ENUM('draft', 'under investigation','resolved', 'rejected');

CREATE TABLE IF NOT EXISTS incidents (
    incident_id SERIAL PRIMARY KEY NOT NULL,
    created_on TIMESTAMP DEFAULT now() NOT NULL,
    created_by INT NOT NULL,
    record_type incident_type,
    location VARCHAR(50),
    status current_status,
    image BYTEA,
    video BYTEA,
    comment VARCHAR(255),
    FOREIGN KEY (created_by)
        REFERENCES users(user_id)
        ON UPDATE CASCADE ON DELETE CASCADE
)