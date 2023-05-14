class GameDatabase:
    def __init__(self, db):
        self.db = db


    def create_player(self, player_id, player_name):
        query = "CREATE (:Player {player_id: $player_id, player_name: $player_name})"
        self.db.execute_query(query, {"player_id": player_id, "player_name": player_name})


    def update_player(self, player_id, player_name):
        query = "MATCH (p:Player {player_id: $player_id}) SET p.player_name = $player_name"
        self.db.execute_query(query, {"player_id": player_id, "player_name": player_name})


    def delete_player(self, player_id):
        query = "MATCH (p:Player {player_id: $player_id}) DETACH DELETE p"
        self.db.execute_query(query, {"player_id": player_id})


    def get_players(self):
        query = "MATCH (p:Player) RETURN p.player_id, p.player_name"
        return self.db.execute_query(query)


    def create_match(self, match_id, player_ids, scores):
        query = "CREATE (:Match {match_id: $match_id})"
        self.db.execute_query(query, {"match_id": match_id})

        for i in range(len(player_ids)):
            query = "MATCH (p:Player {player_id: $player_id}) MATCH (m:Match {match_id: $match_id}) CREATE (p)-[:PARTICIPATED_IN {score: $score}]->(m)"
            self.db.execute_query(query, {"player_id": player_ids[i], "match_id": match_id, "score": scores[i]})


    def get_match(self, match_id):
        query = "MATCH (m:Match {match_id: $match_id})<-[:PARTICIPATED_IN]-(p:Player) RETURN m.match_id, COLLECT(p.player_id) as player_ids, COLLECT(p.player_name) as player_names, COLLECT(p.score) as scores"
        return self.db.execute_query(query, {"match_id": match_id})[0]


    def get_player_history(self, player_id):
        query = "MATCH (p:Player {player_id: $player_id})-[r:PARTICIPATED_IN]->(m:Match) RETURN m.match_id, COLLECT(p.player_name) as player_names, COLLECT(p.score) as scores"
        return self.db.execute_query(query, {"player_id": player_id})



