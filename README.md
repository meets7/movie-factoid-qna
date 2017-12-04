A factoid Question and Answer system which understands the question given in natural language and outputs answer to it using Wikipidea (Dbpedia) as the backend database. Dbpedia has a SPARQL endpoint which would be used to extract information. The domain of the system would be restricted to movies and books. 

With more and more exposure to the field of Natural Language Processing and conversational agents, this application will help as a backend for chat bots or other communication system. Given a natural language query string, the system should be able to process and output the answer.

Examples of questions:
When was the movie released?
What was the movie gross collection?
Who is the director of the movie?
What is the genre of the movie?

---------------------

When What Who How questions supported
POS tag of WH-word - wh-determiner, wh-pronoun, wh-adverb
POS tag of word at 2nd position in bigram of WH-word

