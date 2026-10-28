import database
def test_clear_history_removes_rows(tmp_path,monkeypatch):
    monkeypatch.setattr(database,"DATABASE_PATH",tmp_path/"lab.db")
    database.initialize_database(); database.log_operation("encrypt","HELLO",3,"KHOOR")
    database.clear_history()
    assert database.get_history()==[]