# queries

getMovies = 'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\
SELECT DISTINCT ?film_title ?film_abstract\
WHERE {\
?film_title rdf:type <http://dbpedia.org/ontology/Film> .\
?film_title rdfs:comment ?film_abstract \
} LIMIT 5 OFFSET 0'\

getmovieDetails = 'SELECT ?film_title ?star_name ?nameDirector ?link WHERE {\
  {  \
    SELECT DISTINCT ?movies ?film_title\
    WHERE {\
       ?movies rdf:type <http://dbpedia.org/ontology/Film>; \
       rdfs:label ?film_title.\
    } \
  }. \
  ?movies dbpedia-owl:starring ?star;\
  foaf:isPrimaryTopicOf ?link;\
  dbpedia-owl:director ?director.\
  ?director foaf:name ?nameDirector.\
  ?star foaf:name ?star_name.\
}'