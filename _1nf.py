def _1nf_db(cur):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS MMORPG1NF (
        player_id INTEGER,
        player_name TEXT,
        player_email TEXT,
        character_name TEXT,
        character_class TEXT,
        item_name TEXT,
        item_type TEXT,
        item_power INTEGER
        );
    """)

    cur.execute("""
    INSERT INTO MMORPG1NF VALUES
        (1, 'Python', 'python@mail.com', 'Thorin', 'Warrior', 'Sword of Dawn', 'Weapon', 150),
        (1, 'Python', 'python@mail.com', 'Thorin', 'Warrior', 'Steel Shield', 'Armor', 50),
        (2, 'Gamer', 'Gamer@mail.com', 'Elandra', 'Mage', 'Staff of Wisdom', 'Weapon', 120);
    """)