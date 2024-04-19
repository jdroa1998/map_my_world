CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE location_category_reviewed (
    id SERIAL PRIMARY KEY,
    location_id INT REFERENCES locations(id),
    category_id INT REFERENCES categories(id),
    last_reviewed TIMESTAMP NULL
);