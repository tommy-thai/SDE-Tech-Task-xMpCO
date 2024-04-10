-- SQL queries to set up schemas in BigQuery

-- SQL queries to set up schemas in BigQuery

CREATE TABLE js_users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    email TEXT,
    street TEXT,
    suite TEXT,
    city TEXT,
    zipcode TEXT,
    lat TEXT,
    lng TEXT,
    phone TEXT,
    website TEXT,
    company_name TEXT,
    catch_phrase TEXT,
    bs TEXT
);

CREATE TABLE js_posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT,
    body TEXT
);



