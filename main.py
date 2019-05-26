
import operator
import utils

propositions = []
with open("asset/The-Last-Man-on-the-Moon--Eugene-Cernan-gives-a-compelling-account.txt", encoding="utf8") as file:
    for line in file:
        current = line[:-1]
        if not current.startswith("#"):
            if len(current) != 0:
                propositions.append(current)

sentenceWeights = dict()
title = propositions.pop(0)

for sentence in propositions:
    sentenceWeights[sentence] = utils.weight(title, sentence)

sentences = sorted(sentenceWeights.items(), key=operator.itemgetter(1), reverse=True)

utils.printSentences(sentences,10)
utils.printSentences(sentences,20)
utils.printSentences(sentences,30)
