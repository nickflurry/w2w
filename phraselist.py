from referencelist import ReferenceList

class PhraseList(ReferenceList):

    def __init__(self):
        super().__init__()

    def parse(self, filePath):
        with open(filePath) as f:
            for line in f.readlines():
                tokens = [x.strip() for x in line.split(',')]
                key = list()
                value = 1 #default value
                for token in tokens:
                    try:
                        value = float(token)
                    except ValueError:
                        key.append(token)
                super(PhraseList, self).__setitem__(tuple(key), value)