import PloudosAPI
session = PloudosAPI.login("Altorru", "Nieunieu85") #replace with your PloudOS username / password
server = session.get_server("0")
server.start()
