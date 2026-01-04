class GraphBuilder:
    def __init__(self, neo4j_client):
        self.db = neo4j_client

    def add_chapter(self, name, number):
        self.db.run("""
        MERGE (c:Chapter {name:$name})
        SET c.number = $number
        """, {"name": name, "number": number})

    def add_concept(self, chapter, concept):
        self.db.run("""
        MATCH (c:Chapter {name:$chapter})
        MERGE (co:Concept {name:$concept})
        MERGE (c)-[:HAS_CONCEPT]->(co)
        """, {"chapter": chapter, "concept": concept})

    def add_definition(self, concept, definition):
        self.db.run("""
        MATCH (c:Concept {name:$concept})
        MERGE (d:Definition {text:$definition})
        MERGE (c)-[:DEFINED_AS]->(d)
        """, {"concept": concept, "definition": definition})

    def add_equation(self, formula, elements):
        self.db.run("""
        MERGE (e:ChemicalEquation {formula:$formula})
        """, {"formula": formula})

        for el in elements:
            self.db.run("""
            MATCH (eq:ChemicalEquation {formula:$formula})
            MERGE (el:Element {symbol:$symbol})
            MERGE (eq)-[:USES]->(el)
            """, {"formula": formula, "symbol": el})

    def link_chapters(self, current, next_chapter):
        self.db.run("""
        MATCH (c1:Chapter {name:$c1})
        MATCH (c2:Chapter {name:$c2})
        MERGE (c1)-[:NEXT]->(c2)
        """, {"c1": current, "c2": next_chapter})
