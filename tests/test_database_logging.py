import database
def test_log_operation_and_read_history(tmp_path,monkeypatch):
    monkeypatch.setattr(database,"DATABASE_PATH",tmp_path/"lab.db")
    database.initialize_database(); database.log_operation("encrypt","HELLO",3,"KHOOR")
    rows=database.get_history()
    assert len(rows)==1 and rows[0][1]=="encrypt" and rows[0][2]==3