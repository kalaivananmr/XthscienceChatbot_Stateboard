CREATE CONSTRAINT chapter_name IF NOT EXISTS
FOR (c:Chapter) REQUIRE c.name IS UNIQUE;

CREATE CONSTRAINT concept_name IF NOT EXISTS
FOR (c:Concept) REQUIRE c.name IS UNIQUE;

CREATE CONSTRAINT equation_formula IF NOT EXISTS
FOR (e:ChemicalEquation) REQUIRE e.formula IS UNIQUE;

CREATE CONSTRAINT element_symbol IF NOT EXISTS
FOR (e:Element) REQUIRE e.symbol IS UNIQUE;
