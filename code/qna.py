import questionProcessor
import answerProcessor


def getAnswer(inputstring):

    questionType, subtype = questionProcessor.getQType(inputstring)
    entity = questionProcessor.getMovieName(inputstring)
    if not entity:
        return 'No data found. Please try another movie.', '#'
    answerContent, link = answerProcessor.getAnswerContent(entity)
    answer = answerProcessor.extractAnswer(
        answerContent, questionType, subtype)
    return answer, link


if __name__ == '__main__':

    inputstring = "Who is the director of Cast Away?"
    result = getAnswer(inputstring)
    print(result)
