import random

print("--Korean Flash Cards")
print("--Evan Eames")
print("--2016")
print("-------------------------")

score = 0
run = True
while run:
	compete = False
	letters = ["ㅂ","ㅃ","ㅈ","ㅉ","ㄷ","ㄸ","ㄱ","ㄲ","ㅅ","ㅆ","ㅁ","ㄴ","ㅇ","ㄹ","ㅎ","ㅋ","ㅌ","ㅊ","ㅍ","ㅣ","ㅡ","ㅏ","ㅑ","ㅓ","ㅕ","ㅜ","ㅠ","ㅗ","ㅛ","ㅐ","ㅒ","ㅔ","ㅖ"]
	pronunciation = ["b","bb","j","jj","d","dd","g","gg","s","ss","m","n","ng","r","h","k","t","ch","p","ee","e","a","ya","aw","ya","oo","yoo","o","yo","ey","yey","eh","yeh"]

	words = ['책','잘자','안녕','감사합니다','고마워','제발','미안','죄송합니다','나','너','그','그녀','우리','그들','그녀들','것']

	meaning = ['book','good night','hello','thank you','thanks','please','sorry (informal)','sorry (formal)','I','you','he','she','we','they (male)','they (female)','thing']

	meaning2 = ['book','good night','hello','thanks','thank you','please','sorry','sorry','I','you','that','she','we','they','they','thing']

	#Use this if there is a word/meaning missmatch:
	if False:
		for i in range(0,len(words)):
			print(words[i]+" "+meaning[i]+"\n")

	verbs = ['한다','하는중이다','했다','하는중이었다','할것이다','하는중일것이다','마신다','마시는중이다','마셨다','마시는중이었다','마실것이다','마시는중일것이다','간다','가는중이다','갔다','가는중이었다','갈것이다','가는중일것이다']
	dicform = ['하다','마시다','가다']
	verbmeaning = ['do','doing','did','was doing','will do','will be doing','drink','drinking','drank','was drinking','will drink','will be drinking','go','going','went','was going','will go','will be going']
	verbmeaning2 = ['do','is doing','did','was doing','will do','will be doing','drink','is drinking','drank','was drinking','will drink','will be drinking','go','is going','went','was going','will go','will be going']
	dicformmeaning = ['do','drink','go']

	adjectives = []
	adjmeaning = []
	adjmeaning2 = []

	prompt1 = "Please input meaning \n"
	prompt2 = "Please input characters \n"
	disclaimer = 'Type "reverse" at any point to reverse input mode\nType "end" at any point to try something else\nType "quit" at any point to quit\n-----'
	reverse = False

	mode = input("What would you like to study? Letters, or Vocab? \n")
	print(mode)
	if mode.lower() == "letters":
		print('Type "end" at any point to try something else \nType "quit" at any point to quit\n-----')
		n=1
	elif mode.lower() == "vocab":
		mode2 = input("Would you like to study Adjectives, Verbs, or All? \n")
		if mode2.lower() == "all":
			print(disclaimer)
			n=2
		elif mode2.lower() == "adjectives":
			print(disclaimer)
			n=3
			adj2 = adjmeaning2
		elif mode2.lower() == "verbs":
			mode3 = input("Would you like to study Full or Dictionary forms? \n")
			if mode3.lower() == "full":
				print(disclaimer)
				n=4
			elif mode3.lower() == "dictionary":
				print(disclaimer)
				verbs = dicform
				n=4
	elif mode == "Test" or mode == "test":
		n = 6
	else:
		print("Input not understood.\n")
		continue

	#LETTERS
	while n == 1:
		symbol = random.choice(letters)
		print(symbol)
		g = letters.index(symbol)
		if reverse:
			answer = input("Please input characters \n")
		else:
			answer = input("Please input pronunciation \n")
		if answer == pronunciation[g]:
			print("Correct! \n-----")
		elif answer.lower() == "end":
			n = 0
		elif answer.lower() == "quit":
			n = 0
			run = False
		elif answer.lower() == "go west":
			print("You go West, you come to a river, possible directions are north, east and japan")
		elif answer.lower() == "reverse":
			reverse = not reverse
			temp = pronunciation
			pronunciation = letters
			letters = temp
			temp = prompt1
			prompt1 = prompt2
			prompt2 = temp
			print("Input mode reversed. \n-----")
		else:
			print("Incorrect, the correct pronunciation is " + str(pronunciation[g]) + ". \n-----")
	
	#Vocab
	while n == 2:
		symbol = random.choice(words)
		print(symbol)
		g = words.index(symbol)
		answer = input(prompt1)
		if answer == meaning[g] or answer == meaning2[g]:
			score = score + 1
			print("Correct!\nCombo: " + str(score)+"\n-----")
			if compete:
				if len(words) == 1:
					print("A winner is you!!!\n")
					again = input("Would you like to play again? Y/N\n")
					if again.lower() == "y":
						n = 0
					else:
						n = 0
						run = False
				else:
					del words[g]
					del meaning[g]
					del meaning2[g]
		elif answer.lower() == "end":
			n = 0
		elif answer.lower() == "quit":
			n = 0
			run = False
		elif answer.lower() == "reverse":
			reverse = not reverse
			temp = meaning
			meaning = words
			words = temp
			temp = prompt1
			prompt1 = prompt2
			prompt2 = temp
			print("Input mode reversed. \n-----")
		elif answer.lower() == "compete":
			compete = True
		else:
			score = 0
			print("Incorrect, the correct answer is " + str(meaning[g]) + ". \n-----")
	
	while n == 3:
		symbol = random.choice(adjectives)
		print(symbol)
		g = adjectives.index(symbol)
		answer = input(prompt1)
		if answer == adjmeaning[g] or answer == adjmeaning2[g]:
			print("Correct! \n-----")
		elif answer.lower() == "end":
			n = 0
		elif answer.lower() == "quit":
			n = 0
			run = False
		elif answer.lower() == "reverse":
			temp = adjmeaning
			adjmeaning = adjectives
			adjectives = temp
			temp = prompt1
			prompt1 = prompt2
			prompt2 = temp
			if prompt1 == "Please input meaning \n":
				adj2 = adjmeaning2
			else:
				adj2 = adjmeaning
			print("Input mode reversed. \n-----")
		else:
			if adjmeaning[g] == adj2[g]:
				print("Incorrect, the correct answer is " + str(adjmeaning[g]) + ". \n-----")
			else:
				print("Incorrect, the correct answer is " + str(adjmeaning[g]) + " or " + str(adj2[g]) + ". \n-----")
	
	while n == 4:
		symbol = random.choice(verbs)
		print(symbol)
		g = verbs.index(symbol)
		answer = input(prompt1)
		if answer == verbmeaning[g] or answer == verbmeaning2[g]:
			print("Correct! \n-----")
		elif answer.lower() == "end":
			n = 0
		elif answer.lower() == "quit":
			n = 0
			run = False
		elif answer.lower() == "reverse":
			temp = verbmeaning
			verbmeaning = verbs
			verbs = temp
			temp = prompt1
			prompt1 = prompt2
			prompt2 = temp
			print("Input mode reversed. \n-----")
		else:
			print("Incorrect, the correct answer is " + str(verbmeaning[g]) + ". \n-----")
	
