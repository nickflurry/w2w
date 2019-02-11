from wordlist import WordList
from phraselist import PhraseList

class W2WFeature():

    def __init__(self, referenceList):
        self.referenceList = referenceList
        super().__init__()

    def generateFeatureValue(self, tokens):
        tokens  = [x.lower() for x in tokens]
        retScore = 0
        if type(self.referenceList) is WordList:
           for token in tokens:
               if self.referenceList.has_key(token):
                   retScore += self.referenceList[token]
        elif type(self.referenceList) is PhraseList:
            for i in range (0, len(tokens)):
                for key in self.referenceList:
                    if key[0] == tokens[i]:
                        found = True
                        for j in range(1, len(key)):
                            if i+j < len(tokens) and tokens[i+j] != key[j]:
                                found = False
                                break
                        if found:
                            retScore += self.referenceList[key]
        else:
            raise Exception("referenceList was not of the correct type")

        return retScore