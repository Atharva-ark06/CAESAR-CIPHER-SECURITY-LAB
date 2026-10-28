import database
def test_history_is_limited_to_latest_fifty(tmp_path,monkeypatch):
    monkeypatch.setattr(database,"DATABASE_PATH",tmp_path/"lab.db")
    database.initialize_database()
    for i in range(55): database.log_operation("encrypt",f"message-{i}",i,f"result-{i}")
    rows=database.get_history()
    assert len(rows)==50 and rows[0][3]=="message-54"