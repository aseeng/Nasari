import re
import math

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
        value = findContext(word)
        for p in value:
            nasari1[p] = value.get(p)

    for word in sentence:
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

    sentenceWeight = {

        "“Dream the impossible – and go out and make it happen. I walked on the moon. What can’t you do?” These are the final words spoken by Eugene (Gene) Cernan in the documentary film The Last Man on the Moon. They are a challenge, spoken by a man in his 80s, not just to his grandchildren, but to all of us." : ["0.4347022832142779"],
        "The documentary opens with the Cernan of today, complete with cowboy hat and boots, attending a rodeo and wincing as riders are thrown off the back of a real-life bucking bronco. We are led to imagine, as the picture changes to one of an astronaut in a giant centrifuge, that Cernan is remembering his own training and experiences." :["0.4285171324749593"],
        "The opening credits, accompanied by plangent guitar twangs, are superimposed over pictures of a deserted launchpad, grass growing through cracks in the concrete, close-ups of rusting gantries, and, finally, the silhouette of Cernan himself (one assumes) against the skyline above a crumbling blast-pit, arms akimbo." : ["0.4752064975182557"] ,
        "All the clichés of a western – only the tumbleweed is missing. My heart sank. Why did I agree to review this drivel? I am pleased to report, though, that things got a lot better very quickly.":["0.47509132172146673"],
        "The film gives a personal, compelling account of some of the main events in Cernan’s life as an astronaut, especially his involvement in the Apollo programme. Scenes of Cernan today, visiting locations where he lived and trained, are mixed with historical footage of his younger self.":["0.4752378114023714"],
        "After starting his career as a gung-ho navy pilot in the 1950s, he was selected by Nasa in 1963 to become part of its astronaut training corps. But the film is much more than a biography of Cernan; it is his account of one of the most important parts of the history of human spaceflight.":["0.4752407323398737"],
        "Cernan flew in space three times. His first opportunity was marked by grief. The original crew of Gemini 9 were killed in a plane crash, moving Cernan from backup astronaut to flight crew. Part of his mission was to carry out a spacewalk, from the front of the capsule to the rear.":["0.47566580542210196"],
        "Cernan’s spacewalk was a solo effort, with a hugely long “umbilical cord” attaching him to the spacecraft, which kept getting in the way of his manoeuvres. He had no handholds and no tethers to anchor him. His spacesuit did not appear to be cooled, and as he got hotter, his heart rate rose to dangerous levels. Overheating from his exertions, combined with heat from the Sun, made him sweat – causing his helmet to fog upwhen the temperatured fell, which was once every 90 minutes as the capsule orbited Earth.":["0.47542226734063764"],
        "Because of these problems, he could not complete the spacewalk. Cernan regards his part in the mission as a failure. But watching the ISS astronauts carrying out their tasks half a century later, it is clear they owe an enormous debt of gratitude to pathfinders such as Cernan, who took huge risks to identify where improvements had to be made.":["0.47566580542210196"],
        "The Gemini programme gave way to the Apollo programme, which started with a tragedy – a fire, while on the launchpad, on Apollo 1. Cernan speaks with emotion of the accident that took the lives of three of his friends and colleagues, and the effect it had on the remaining astronauts. ":["0.47566580542210196"],
        "His first Apollo flight was as a member of the Apollo 10 crew, which went to the Moon, to simulate landing and docking. He was clearly moved by the experience, speaking evocatively of seeing the Earth rise for the first time.":["0.4752411840360483"],
        "Cernan’s last trip was as commander on Apollo 17. His description of the lunar landscape, his excitement at finding orange soil and travelling in the lunar rover brought out the inner astronaut in me.":["0.4752411840360483"],
        "Cernan’s first wife is an important part of the documentary, describing what it was like living in the “astronaut colony”. Pictures of parties, barbecues and laughter are shown alongside footage of the Apollo 1 disaster, showing how close the astronauts’ wives became to each other. After Apollo, Cernan travelled as a global ambassador for Nasa, and long stretches away from home eventually ruined his marriage.":["0.47542226734063764"],
        "Reflecting on his life, and still travelling as an ambassador, Cernan acknowledges he was selfish, in that he neglected his family for his job. He isn’t the first, and won’t be the last, to make that admission. But he does seem to be a dedicated father in his own way. Footage of his young daughter explaining to a TV reporter her dad had promised to bring her back a moonbeam from his mission certainly shows paternal warmth.":["0.4754844437978828"],
        "As Neil Armstrong, the first man to walk on the moon, took “one small step” to make “a giant leap for mankind”, so Cernan marked his departure from the moon with “man’s last step from the surface”, hoping that “we shall return, with peace and hope for all mankind”. Only 41 months separated the footprints made by the two men, but their achievements have echoed through the 44 years since Cernan closed the hatch on the lunar module.":["0.4752064975182557"],
        "The documentary once again reminds us of the gift the bravery of the Apollo astronauts gave us – a heritage of human spaceflight that has now enabled a much more global and co-operative space programme.":["0.4689601636494808"]
        }


    '''for sentence in preposition:
        w = weight(title,sentence)
        print(sentence)
        print(weight(title,sentence))
        sentenceWeight[sentence] = w'''

    gradeOfReduction = len(preposition)- (len(preposition)/100 *30)
    print(int(gradeOfReduction))

    sorted(sentenceWeight, key=sentenceWeight.get, reverse=False)

    for i in range(0,int(gradeOfReduction)):
        print(sentenceWeight.popitem())
