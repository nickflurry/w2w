from mwapi import Session
from revscoring.extractors import api
from revscoring.features import temporal, wikitext
from revscoring import Feature
import mwparserfromhell as mwp

from wordlist import WordList
from phraselist import PhraseList
from w2w_feature import W2WFeature

session = Session("https://en.wikipedia.org/w/api.php", user_agent="joe")
extractor = api.Extractor(session)

def puffery(segmentsAdded):
	wordList = WordList()
	wordList.parse("pufferyOutput.txt")
	segmentsAdded = mwp.parse(segmentsAdded)
	retScore = 0.0;
	for key in wordList:
		count = segmentsAdded.count(key)
		count += segmentsAdded.count(key.title())				
		if count > 0:
			retScore += count * wordList[key]
	return retScore

puffery = Feature(
    "puffery", 
    puffery, 
    depends_on=[wikitext.revision.diff.datasources.segments_added],
    returns=float)

print(extractor.extract(867964616, puffery))







