
from SpellChecker import *
from enchant_and_levenshtein import *
def main():

	#get sentence
	#parse sentence by words
	#find misspelled words and put into list
	#run LCSrec on each misspelled word
	#check Levenshtein score on each suggested word
	#output top 3
	theDict = English().dictionary

	while True:
		#get input
		print(": ")
		textBlock = raw_input()

		#tokenize sentence and put in list
		#find misspelled words and put into list
		misspelledList = getMisspelledWords(theDict, textBlock)


		#run LCsrec on each misspelled word
		misspelledDict = {}
		for eachMisspelled in misspelledList:
			recommendedList = returnLCSrecs(mispelled):
			recommendedDict = {}
			for eachRecommended in recommendedList:
				recommendDict[eachRecommended] = levenshteinCheck(eachRecommended, eachMisspelled)

			misspelledDict[eachMisspelled] = sorted(recommendDict, key=recommendDict.get, reverse = true)[0:2]
			

		for eachKey in misspelledDict.keys():
			print(eachKey),
			print(": "),
			print(misspelledDict[eachKey])
		#check Levenshtein score on each suggest word

		#output top 3 for each word








if __name__ == "__main__":
	main()