import random

print("--Russian Flash Cards")
print("--Evan Eames")
print("--2014")
print("-------------------------")

score = 0
run = True
while run:
	majuscules = ["А","Б","В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"]
	miniscules = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
	pronunciation = ["a","b","v","g","d","ye","yo","zhe","z","ee","y","k","l","m","n","o","p","r","s","t","u","f","h","ts","ch","sh","shch","hard","ouei","soft","e","yu","ya"]

	words =    ["дом", "кот", "самолёт", "хлеб", "яблоко", "здравствуйте", "меня", "зовут", "очень приятно", "как", "до свидания", "вы", "ты" ,"а вас?" ,"студент", "он", "она", "оно", "мы", "они", "утро", "день", "вечер", "ночь", "добрый", "спасибо", "хорошо", "тоже", "собака", "книга", "город", "страна", "кто", "что", "семья", "деньги", "брат","улица", "выходные", "класс", "но", "здорово", "откуда", "жена", "дочь", "ещё", "немного", "сейчас", "здесь", "очень", "много", "только", "конечно", "не", "всё", "только", "всегда", "каждый", "как обычно", "комнате", "юге", "сайте", "обеде", "когда", "жизнь", "неплохо", "потом", "извините", "пожалуйста", "прямо", "справа", "не за что", "конкретно", "слева", "сегодня", "завтракал", "или", "раньше", "рыбы", "люди", "лесу", "уже", "сегодня", "раз", "там"]

	meaning =  ["home", "cat", "plane", "bread", "apple", "hello", "my", "name", "pleasure to meet you", "what", "goodbye", "you(formal)", "you(informal)", "and you?", "student", "he", "she", "it", "we", "they", "morning", "day", "evening", "night", "good", "thanks", "well", "also", "dog", "book", "city", "country", "who", "that", "family", "money", "brother", "street", "weekend", "good!", "but", "excellent", "whence", "wife", "daughter", "still", "a little", "now", "here", "very", "many", "only", "of course", "not", "every", "only", "always", "each", "as usual" ,"room", "south", "online", "dinner", "when?", "life", "not bad", "and then", "sorry", "please", "foreward", "on the right", "it's nothing", "specifically", "on the left", "today", "breakfast", "or", "before", "fish", "people", "forest", "already", "today", "instance", "there (position)"]

	meaning2 = ["house", "cat", "flight", "bread", "apple", "hello", "my", "name", "nice to meet you", "what", "goodbye", "you", "you", "and you", "student", "he", "she", "it", "we", "they", "morning", "day", "evening", "night", "good", "thank you", "good", "also", "dog", "book", "city", "country", "who", "that", "family", "money", "brother", "road", "weekend", "good", "but", "excellent", "location", "wife", "daughter", "yet", "a bit", "currently", "here", "very", "much", "only", "sure", "not", "all", "only", "always", "each", "as usual", "room", "south", "online", "dinner", "when", "life", "pretty good", "then", "sorry", "please", "straight", "right", "you're welcome", "exactly", "left" "today", "breakfast", "or", "previously", "fish", "people", "forest", "already", "today", "time", "there"]

	#Use this if there is a word/meaning missmatch:
	#for i in range(0,len(words)):
	#	print(words[i]+" "+meaning[i]+" "+meaning2[i]+"\n")

	verbs = ["говорить", "работать", "слушать", "читать", "понимать", "думать", "знать", "быть", "курить", "видеть", "есть"]
	dicform = []
	verbmeaning = ["speak", "work", "listen", "read", "understand", "think", "know", "be", "smoke", "see", "eat"]
	verbmeaning2 = ["speak", "work", "listen", "read", "understand", "think", "know", "have", "smoke", "see", "eat"]

	adjectives = ["большая", "маленький", "занят", "вкусный", "устал", "отлично", "дорого"]
	adjmeaning = ["large", "little", "busy", "tasty", "tired", "very well", "expensive"]
	adjmeaning2 = ["big", "small", "busy", "yummy", "tired", "very good", "expensive"]

	prompt1 = "Please input meaning \n"
	prompt2 = "Please input characters \n"
	disclaimer = 'Type "reverse" at any point to reverse input mode\nType "end" at any point to try something else\nType "quit" at any point to quit\n-----'
	reverse = False

	mode = input("What would you like to study? Majuscules, Miniscules, or Vocab? \n")
	print(mode)
	if mode.lower() == "majuscules":
		print('Type "end" at any point to try something else \nType "quit" at any point to quit\n-----')
		n=1
	elif mode.lower() == "vocab":
		mode2 = input("Would you like to study Adjectives, Verbs or General Vocab? \n")
		if mode2.lower() == "general vocab":
			print(disclaimer)
			n=2
		elif mode2.lower() == "adjectives":
			print(disclaimer)
			n=3
			adj2 = adjmeaning2
		elif mode2.lower() == "verbs":
			mode3 = input("Would you like to study Polite or Dictionary forms? \n")
			if mode3.lower() == "polite":
				print(disclaimer)
				n=4
			elif mode3.lower() == "dictionary":
				print(disclaimer)
				verbs = dicform
				n=4
	elif mode.lower() == "miniscules":
		print('Type "end" at any point to try something else \nType "quit" at any point to quit\n-----')
		n=5
	elif mode == "Test" or mode == "test":
		n = 6
	else:
		print("Input not understood.\n")
		continue

	#MAJUSCULES
	while n == 1:
		symbol = random.choice(majuscules)
		print(symbol)
		g = majuscules.index(symbol)
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
			pronunciation = majuscules
			majuscules = temp
			temp = prompt1
			prompt1 = prompt2
			prompt2 = temp
			print("Input mode reversed. \n-----")
		else:
			print("Incorrect, the correct pronunciation is " + str(pronunciation[g]) + ". \n-----")
	
	while n == 2:
		symbol = random.choice(words)
		print(symbol)
		g = words.index(symbol)
		answer = input(prompt1)
		if answer == meaning[g] or answer == meaning2[g]:
			score = score + 1
			print("Correct!\nCombo: " + str(score)+"\n-----")
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
	
	
	#MINISCULES
	while n == 5:
		symbol = random.choice(miniscules)
		print(symbol)
		g = miniscules.index(symbol)
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
		elif answer.lower() == "reverse":
			reverse = not reverse
			temp = pronunciation
			pronunciation = miniscules
			miniscules = temp
			temp = prompt1
			prompt1 = prompt2
			prompt2 = temp
		
		else:
			print("Incorrect, the correct pronunciation is " + str(pronunciation[g]) + ". \n-----")	
