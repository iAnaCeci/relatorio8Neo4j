from neo4j import GraphDatabase
from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.192.56.92:7687", user="neo4j", password="subprograms-benches-harness")

db.drop_all()

# Criando uma instância da classe GameDatabase para interagir com o banco de dados
game_database = GameDatabase(db)

# Criando um jogador
game_database.create_player(player_id=1, player_name="Ana")

# Obtendo a lista de jogadores
players = game_database.get_players()
print(players)

# Registrando informações sobre uma partida
game_database.create_match(match_id=1, player_ids=[1, 2, 3], scores=[10, 20, 30])

# Obtendo informações sobre uma partida específica
match_info = game_database.get_match(match_id=1)
print(match_info)

# Obtendo o histórico de partidas de um jogador
player_history = game_database.get_player_history(player_id=1)
print(player_history)

# Atualizando informações de um jogador
game_database.update_player(player_id=1, player_name="Ana Cecilia")

# Excluindo um jogador
game_database.delete_player(player_id=1)
