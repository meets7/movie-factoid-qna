import nltk
import csv


def readTrainingData():
    with open('../trainingData/train_5500.label.txt') as f:
        data = f.readlines()
    return data


def createfeatures():
    data = readTrainingData()
    with open('features.csv', 'w') as f:
        for datapoint in data:
            line = datapoint.split()
            question = line[1]
            label = line[0]
            taggedtokens = nltk.pos_tag(nltk.word_tokenize(question))
            chunks = nltk.ne_chunk(taggedtokens)
            for token in taggedtokens:
                word = token[0]
                pos = token[1]
                if pos == 'WRB' or pos == 'WP' or pos == 'WDT' or pos == 'WP$':
                    wh_token = word
                    wh_pos = pos


            csvwriter = csv.writer(f, delimiter=',')
            csvwriter.writerow([question, label])


if __name__ == '__main__':
    createfeatures()
