from enchant_and_levenshtein import *
from SpellChecker import *

def main():

	print("initliazing English dictionary")
	englishDict = English().dictionary
	levenshteinTest()
	return 0
if __name__ == "__main__":
	main()