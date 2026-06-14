CREATE TABLE lost_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    location TEXT,
    description TEXT
);

CREATE TABLE found_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT,
    location TEXT,
    description TEXT
);
