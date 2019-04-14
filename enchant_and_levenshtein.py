import enchant
import Levenshtein

#initialize english word library
#access by English.dictionary
class English():

	def __init__(self):
		dictionary = enchant.Dict("en_US")

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
def levenshteinTest()
	print("Test")

	listOfWords = ["good",
				  "goode",
				  "geode",
				  "moody"]

	wordTest = "good"

	for each in listOfWords:
		print(str(each) + ": "),
		print(levenshteinCheck(each,wordTest))	

	return 0