from wordlist import WordList
from phraselist import PhraseList
from w2w_feature import W2WFeature

wordList = WordList()
wordList.parse("pufferyOutput.txt")

w2wFeature = W2WFeature(wordList)
print("output below should be 1, 2, 0")
print(w2wFeature.generateFeatureValue(["joe", "is", "legendary"]))
print(w2wFeature.generateFeatureValue(["joe", "is", "legendary", "and", "adept"]))
print(w2wFeature.generateFeatureValue(["joe", "is", "cat", "dog", "dolphin"]))

phraseList = PhraseList()
phraseList.parse("phrase.csv")
w2wFeature = W2WFeature(phraseList)
print("ouput below should be 1, 1, 2, 0")
print(w2wFeature.generateFeatureValue(["the", "dog", "sleep"])) #should print 1
print(w2wFeature.generateFeatureValue(["the", "dog", "sleep", "happy", "dreams"]))#should print 1
print(w2wFeature.generateFeatureValue(["the", "dog", "sleep", "happy", "dreams","the", "dog", "sleep"]))#should print 0
print(w2wFeature.generateFeatureValue(["the", "dog", "not", "sleep"]))#should print 0