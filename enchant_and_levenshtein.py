import enchant
import Levenshtein
import re
import nltk

class English():

	def __init__(self):
		self.dictionary = enchant.Dict("en_US")


def getMisspelledWords(theDict, textBlock):

	#create missSpelled list
	misspelledList = []
	#token the block of text and store into list
	tokenizedList = re.findall("[A-Z]{2,}(?![a-z])|[A-Z][a-z]+(?=[A-Z])|[\'\w\-]+",textBlock)
	print("tokenized list: "),
	print(tokenizedList)
	#check list for misspelled words
	for word_tokenize in tokenizedList:
		token = re.split("-", word_tokenize)
		print("token: ", token)

		#type checking
		if type(token) == type(list()):
			for eachWord in token:

				#check if english word
				if not ifEnglishWord(theDict, eachWord):
					misspelledList.append(eachWord)

		elif type(token) == type(str()):
			if not ifEnglishWord(theDict, token):
				misspelledList.append(token)
		else:
			print("ERROR type")

	return misspelledList

						

	return 0
def ifEnglishWord(theDict, word):
	try:
		if theDict.check(word) is True:
			return True
		else:
			return False
	except:
		print("theDict not the same type as enchant.Dict")

	return -1


#get score of 2 words
def levenshteinCheck(word1, word2):
	return Levenshtein.ratio(word1,word2)

#description below
def wordSuggestion(theDict, word1):

	'''
	param: dictionary <- {}
		   word <- str

	ouput -> 1-3 length suggestionList of words


	pseudo:

	suggestionList <- list()
	check words that contain that word (ex. good -> goode, have -> shave)

	'''


#just a test for levenshtein
def levenshteinTest():
	print("Test")

	listOfWords = ["good",
				  "goode",
				  "geode",
				  "moody"]

	wordTest = "good"

	for each in listOfWords:
		print(str(each) + ": "),
		print(levenshteinCheck(each,wordTest))

def getMisspelledWords_test():

	theDict = English().dictionary
	textBlock = "Don't ki-yourself this is just an example. This life is too good to us. We're too young too fail"

	print("misspelled list: ")
	print(getMisspelledWords(theDict, textBlock))

	print("checking Don't")
	print(ifEnglishWord(theDict, "hadn't"))
	print(ifEnglishWord(theDict, "Ishmael"))
		
		





	return 0