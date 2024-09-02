
dataBaseName="practicabd"
userName="root"
userPassaword=""
connectionPort=3306
server="localhost"


dataBaseConnection=f"mysql+mysqlconnector://{userName}:{userPassaword}@{server}:{connectionPort}/{dataBaseName}"

print(dataBaseConnection)

