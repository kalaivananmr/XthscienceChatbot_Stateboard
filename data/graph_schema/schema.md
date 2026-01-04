# Class 10 Science Knowledge Graph Schema

## Nodes
- Chapter
  - name
  - number
- Concept
  - name
- Definition
  - text
- ChemicalEquation
  - formula
- Element
  - symbol
  - name
- Question
  - text
  - type (MCQ, FillBlank, Short)
- Answer
  - text

## Relationships
- (Chapter)-[:HAS_CONCEPT]->(Concept)
- (Concept)-[:DEFINED_AS]->(Definition)
- (ChemicalEquation)-[:USES]->(Element)
- (Question)-[:ANSWER]->(Answer)
- (Chapter)-[:NEXT]->(Chapter)
