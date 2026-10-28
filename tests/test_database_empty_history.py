import database
def test_history_starts_empty(tmp_path,monkeypatch):
    monkeypatch.setattr(database,"DATABASE_PATH",tmp_path/"lab.db")
    database.initialize_database()
    assert database.get_history()==[]