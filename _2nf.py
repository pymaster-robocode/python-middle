def _2nf_db(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Players (
        player_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Characters (
            character_id INTEGER PRIMARY KEY,
            player_id INTEGER,
            name TEXT,
            class TEXT,
            FOREIGN KEY (player_id) REFERENCES Players(player_id)
            );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Inventory (
            character_id INTEGER,
            item_name TEXT,
            item_type TEXT,
            item_power INTEGER,
            FOREIGN KEY (character_id) REFERENCES Characters(character_id)
        );
    """)

    cur.execute("""
        INSERT INTO Players
        VALUES (1, 'Python', 'python@mail.com'),
        (2, 'Gamer', 'gamer@mail.com');
    """)

    cur.execute("""
        INSERT INTO Characters VALUES
        (1, 1, 'Thorin', 'Warrior'),
        (2, 2, 'Elandra', 'Mage');
    """)

    cur.execute("""
        INSERT INTO Inventory VALUES
        (1, 'Sword of Dawn', 'Weapon', 150),
        (1, 'Steel Shield', 'Armor', 50),
        (2, 'Staff of Wisdom', 'Weapon', 120);
    """)
