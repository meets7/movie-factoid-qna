import wptools
import re


def getAnswerContent(entity):
    answerContent = wptools.page(entity).get_parse()
    return answerContent.data['infobox'], answerContent.data['wikidata_url']


def extractAnswer(content, type, subtype):

    if type == 'person':
        if subtype == 'director':
            if content.get('director'):
                directorRegex = re.compile(r'\[\[(.*)\]\]', re.I)
                answer = directorRegex.search(content['director']).groups()[0]
                # answer = re.search(
                #     r'\[\[([a-zA-Z\s]+)\]\]', content['director'])
            else:
                answer = 'No director specified on Wikipedia.'
        elif subtype == 'cast' and content.get('starring'):
            answer = re.findall(
                r'\[\[([a-zA-Z\s]+)\]\]', content['starring'])
        elif subtype == 'music' and content.get('starring'):
            answer = re.findall(
                r'\[\[([a-zA-Z\s]+)\]\]', content['starring'])
    elif type == 'date':
        if content.get('released'):
            answer = content['released']
        else:
            answer = 'Release date not available.'
    elif type == 'info':
        answer = ''
    elif type == 'money':
        if content.get('gross'):
            answer = content['gross']
        else:
            answer = 'No gross collection specified in wikipedia article.'

    return answer


if __name__ == '__main__':
    entity = 'How I met your mother'
    content = getAnswerContent(entity)
    finalAnswer = extractAnswer(content, 'person', 'cast')
    print(finalAnswer)
