def _3nf_db(cur):
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
        CREATE TABLE IF NOT EXISTS Items (
            item_id INTEGER PRIMARY KEY,
            name TEXT,
            type TEXT,
            power INTEGER
        );
    """)

    cur.execute("""
        CREATE TABLE Inventory (
            character_id INTEGER,
            item_id INTEGER,
            FOREIGN KEY (character_id) REFERENCES Characters(character_id),
            FOREIGN KEY (item_id) REFERENCES Items(item_id)
        );
    """)

    cur.execute("""
        INSERT INTO Players
        VALUES (1, 'Python', 'python@mail.com'),
        (2, 'Gamer', 'gamer@mail.com');
    """)

    cur.execute("""
        INSERT INTO Characters
        VALUES (1, 1, 'Thorin', 'Warrior'),
        (2, 2, 'Elandra', 'Mage');
    """)

    cur.execute("""
        INSERT INTO Items VALUES
            (1, 'Sword of Dawn', 'Weapon', 150),
            (2, 'Steel Shield', 'Armor', 50),
            (3, 'Staff of Wisdom', 'Weapon', 120);
    """)

    cur.execute("""
        INSERT INTO Inventory VALUES
            (1, 1),
            (1, 2),
            (2, 3);
    """)