import landerdb

relay = 0
brokers = [{"ip":"zcoin.zapto.org", "port":9595, "192.111.130.31":9595}]#[{"ip":"zcoin.zapto.org", "port":6564}, {"ip":"192.111.130.31", "port":6565}]
version = "0.2.2"
host = "0.0.0.0"
port = 9595
nodes = landerdb.Connect("nodes.db")
wallet = landerdb.Connect("wallet.db")
db = landerdb.Connect("db.db")
