import re
import math
import operator
import nltk
from nltk.corpus import stopwords as sw


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
        if word not in stopwords:
            value = findContext(word)
            for p in value:
                nasari1[p] = value.get(p)

    for word in sentence:
        if word not in stopwords:
            value = findContext(word)
            for p in value:
                nasari2[p] = value.get(p)

    for word1 in nasari1:
        for word2 in nasari2:
            if word1 == word2:
                overlapping.add(word1)

    sum = 0
    for w in overlapping:

        for word in nasari1:
            if w == word:
                sum += float(nasari1.get(word))

        for word in nasari2:
            if w == word:
                sum += float(nasari2.get(word))

    cardinality = 0
    for i in range(0,len(overlapping)):
        cardinality += 2 * i

    return math.sqrt(cardinality/sum)

if __name__=="__main__":

    stopwords = sw.words('english')

    preposition = []
    nasari = []

    with open("asset/dd-small-nasari-15.txt", encoding="utf8") as filehandle:
        file = filehandle. readlines()

        for line in file:
            current = line[:-1]
            nasari.append(current)


    with open("asset/The-Last-Man-on-the-Moon--Eugene-Cernan-gives-a-compelling-account.txt", encoding="utf8" ) as filehandle:
        filecontents = filehandle.readlines()

        for line in filecontents:

            current_place = line[:-1]

            if not current_place.startswith("#"):
                if not len(current_place) == 0:
                    preposition.append(current_place)

    sentenceWeight = dict()
    title = preposition.pop(0)

    for sentence in preposition:
        sentenceWeight[sentence] = weight(title, sentence)

    gradeOfReduction = len(preposition) - (len(preposition)/100 *30)

    sorted = sorted(sentenceWeight.items(), key=operator.itemgetter(1), reverse=True)

    count = 0
    for i in sorted:
        if count < gradeOfReduction:
            print(i[0])
            count+=1