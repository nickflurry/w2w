from referencelist import ReferenceList

class WordList(ReferenceList):

    def __init__(self):
        super().__init__()

    def parse(self, filePath):
        with open(filePath) as f:
            for line in f.readlines():
                tokens = [x.strip() for x in line.split(',')]
                super(WordList, self).__setitem__(tokens[0].lower(), float(tokens[1]))