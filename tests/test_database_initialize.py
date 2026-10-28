import database
def test_initialize_creates_database(tmp_path,monkeypatch):
    monkeypatch.setattr(database,"DATABASE_PATH",tmp_path/"nested"/"lab.db")
    database.initialize_database()
    assert database.DATABASE_PATH.exists()