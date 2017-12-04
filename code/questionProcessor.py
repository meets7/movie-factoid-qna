import re
import nltk
import spacy


def getMovieName(inputstring):
    tokens = nltk.word_tokenize(inputstring)
    tagging = nltk.pos_tag(tokens)

    regex0 = re.compile(r'did([A-Za-z0-9\s]+)earn', re.I)
    try:
        nounphrase = regex0.search(inputstring).groups()
        return nounphrase[0].strip()
    except:
        pass

    regex1 = re.compile(r'(?<=in|of)([\w\d\s]+)', re.I)
    try:
        nounphrase = regex1.search(inputstring).groups()
        return nounphrase[0].strip()
    except:
        pass

    grammar1 = "INSTHING: {<IN><DT>?<NN>}"
    cp = nltk.RegexpParser(grammar1)
    result = cp.parse(tagging)


    phrase = ''
    for r in result:
        if isinstance(r, nltk.tree.Tree) and r.label() == 'INSTHING':
            for tup in r:
                phrase = phrase + tup[0] + ' '
            break

    if phrase:
        phrase = phrase.strip()
        regex2 = re.compile(r'(?<={})([\w\d\s]+)'.format(phrase), re.I)
        nounphrase = regex2.search(inputstring).groups()
        return nounphrase[0].strip()

    # whenregex = re.compile(r'(?<=when)([\w\d\s]+)', re.I)
    chunks = nltk.ne_chunk(tagging)
    whenregex = "WHENTHING: {<WRB><VBD><NNP>}"
    cp = nltk.RegexpParser(whenregex)
    result = cp.parse(tagging)
    phrase = ''
    for r in result:
        if isinstance(r, nltk.tree.Tree) and r.label() == 'WHENTHING':
            for tup in r:
                phrase = phrase + tup[0] + ' '
            break

    if phrase:
        phrase = phrase.strip()
        regex2 = re.compile(r'(?<={0})([\w\d\s]+)'.format(phrase), re.I)
        nounphrase = regex2.search(inputstring).groups()
        return nounphrase[0].strip()

def getQType(inputstring):
    qtypemapping = {
        'who': 'person',
        'when': 'date',
        'what': 'money',
        'how': 'money',
        'gross': 'money',
        'box': 'money'
    }
    tokens = nltk.word_tokenize(inputstring)

    qtype = ''
    for token in tokens:
        qtype = qtypemapping.get(token.lower())
        if qtype:
            break

    nlpspacy = spacy.load('en')
    doc1 = nlpspacy(inputstring)
    docs = [nlpspacy('Who is the director'),
            nlpspacy('Who directed the movie'),
            nlpspacy('Who directed'),
            nlpspacy('What is the name of the director of'),
            nlpspacy('Who is the actor'),
            nlpspacy("What is the actor's name"),
            ]

    scores = []
    for doc in docs:
        scores.append(doc1.similarity(doc))

    maxSimilarityIndex = scores.index(max(scores))
    if maxSimilarityIndex <= 3:
        subtype = 'director'
    else:
        subtype = 'cast'
    return qtype, subtype


if __name__ == '__main__':
    inputstring = 'Who is the music director of Avatar?'
    print(getMovieName(inputstring))
    print(getQType(inputstring))
