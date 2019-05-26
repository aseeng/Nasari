import re
import math
from nltk.corpus import stopwords as sw

stop_words = sw.words('english')
nasari = []

with open("asset/dd-small-nasari-15.txt", encoding="utf8") as file:
    for line in file:
        current = line[:-1]
        nasari.append(current)


def findContext(word):

    vector = dict()
    synset = []

    for line in nasari:
        if re.search("\D;(\w+)\W", line).group(1).lower() == word.lower():
            synset = re.findall("(\w+_\d+.\d+)", line)

    for w in synset:
        vector[re.search("(\w+)_", w).group(1)] = re.search("_(\d+.\d+)", w).group(1)

    return vector


def weight(title, sentence):
    overlapping = set()
    nasari1 = dict()
    nasari2 = dict()

    for word in title:
        if word not in stop_words:
            value = findContext(word)
            for p in value:
                nasari1[p] = value.get(p)

    for word in sentence:
        if word not in stop_words:
            value = findContext(word)
            for p in value:
                nasari2[p] = value.get(p)

    for word in nasari1:
        if word in nasari2:
            overlapping.add(word)

    sum = 0

    for word in overlapping:
        if word in nasari1:
            sum += float(nasari1.get(word))

        if word in nasari2:
            sum += float(nasari2.get(word))

    cardinality = 0
    for i in range(len(overlapping)):
        cardinality += 2 * i

    return math.sqrt(cardinality/sum)


def printSentences(sentences, gradeOfReduction):
    print(str(gradeOfReduction) + " %")
    numSentences = len(sentences) - (len(sentences) / 100 * gradeOfReduction)
    count = 0
    for sentence in sentences:
        if count < numSentences:
            print(sentence[0])
            count += 1

    print()
