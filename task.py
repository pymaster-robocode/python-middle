def _3nf_db_with_guilds(cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Guilds (
            guild_id INTEGER PRIMARY KEY,
            name TEXT
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Players (
            player_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            guild_id INTEGER,
            FOREIGN KEY (guild_id) REFERENCES Guilds(guild_id)
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
        CREATE TABLE IF NOT EXISTS Inventory (
            character_id INTEGER,
            item_id INTEGER,
            FOREIGN KEY (character_id) REFERENCES Characters(character_id),
            FOREIGN KEY (item_id) REFERENCES Items(item_id)
        );
    """)

    # Вставка даних для кланів
    cur.execute("""
        INSERT INTO Guilds (guild_id, name) VALUES
        (1, 'Dragon Slayers'),
        (2, 'Mage Circle');
    """)

    # Вставка даних для гравців з прив'язкою до кланів
    cur.execute("""
        INSERT INTO Players (player_id, name, email, guild_id) VALUES
        (1, 'Python', 'python@mail.com', 1),
        (2, 'Gamer', 'gamer@mail.com', 2);
    """)

    cur.execute("""
        INSERT INTO Characters (character_id, player_id, name, class) VALUES
        (1, 1, 'Thorin', 'Warrior'),
        (2, 2, 'Elandra', 'Mage');
    """)

    cur.execute("""
        INSERT INTO Items (item_id, name, type, power) VALUES
            (1, 'Sword of Dawn', 'Weapon', 150),
            (2, 'Steel Shield', 'Armor', 50),
            (3, 'Staff of Wisdom', 'Weapon', 120);
    """)

    cur.execute("""
        INSERT INTO Inventory (character_id, item_id) VALUES
            (1, 1),
            (1, 2),
            (2, 3);
    """)
