CREATE TABLE cats (
    id SERIAL PRIMARY KEY,
    api_id VARCHAR(100) UNIQUE NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    name VARCHAR(100),
    description VARCHAR(255),
    breed VARCHAR(255)
);

CREATE TABLE favorite_cats (
    cat_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY (cat_id) REFERENCES cats(id) ON DELETE CASCADE
);