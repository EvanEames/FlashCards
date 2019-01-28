import random

print("--Hindi Flash Cards")
print("--Evan Eames")
print("--2015")
print("-------------------------")

score = 0
run = True
while run:
	compete = False
	letters = ["अ","आ","इ","ई","उ","ऊ","ऋ","ए","ऐ","ओ","औ","अं","अः","क","ख","ग","घ","ङ","च","छ","ज","झ","ट","ठ","ड","ढ","ण","त","थ","द","ध","न","प","फ","ब","भ","म","य","र","ल","श","ष","स","ह"]#,‌"‌‌‌‌‍‌व"]
	pronunciation = ["a","aa","e","ee","o","oo","rr","eh","ehh","oh","ow","an","ah","k","kh","g","gh","rdh","ch","chh","j","jh","tt","tth","d","dh","rdn","t","th","the","thh","n","p","f","b","bh","m","y","r","l","sh","sh","c","h"]#,"v"]

	words =    ["नाराज़ होना","चाल","राज़","बदलना","सुझा‌‌व‍‌","जल्दी करना","कसूर‌‌वार ठहराना","सूर्य की रोशनी","बहुसख्यक","दोहराना","स्तानपायी","राजस्व","बन्द करना","स्कूल वर्ष","लघुकथएं","घोषणा करना", "विजेता", "रही", "कंघी करना", "गलती से", "जरुरी", "आगे","मीठा","बेचना","पिछला","छुटृटियों","गले लगाना","सुनाना","पुराना","कवीता","प्रश्न","ईमान्दारी","चित्र बनाना","कलाकार","नुकसान पहुंचाना","बाटना","बराबर","चलो","हिस्सों","कितना","लाना","कैसे","आग","ऐनक","पैसा","हँसना","मुँह","भौं","शादी","बहन","रोशनी","शक करना","बिस्तर","परिवार ","ऊपर","समझाना","बार","विदेशी","समाधान","ग्रराहक","सारा","जानना","सैर","कोई","चुनाव करना","उदाहरण","गलत","मामला","पहचान","अपवाद","नियम","होते हैं","कहा जाता है","पुराना","बजे","लम्बा","अगला","अन्दर","बाहर","सब","जगह","परेशान मत करो","झक्कास","तथा","लिखना","तैरना","डरावना","अन्य","अघिक","लेना","उपयोग करना","आजकल","के बारे मेँ","दफ्तर","रखना","जहाँ","तब","कारा","दरवाज़े","बिलकुल पास","पहुँचना","मदद","साड़े","दोपहर","शाम","पूरे","महिला","तस्वीर","कौनसि","लगातार","खोदना","जीवाश्म","दुर्लभ","पक्षी","फोटो खीचना","तालाब","पूरी तरह","सर्दी","गला","दुखना","स्नातक होना","घास का मैदान","चोटी","फैला हुआ","इतिहास","विश्वविद्यालयट","विश्व","घड़ी","बिजली","पहले","गिरना","किस तरफ","नज़रअन्दाज करना","का अर्थ होना","भाषण","कर","पकना","ज़रा देख लें","यह बाले","बेहतर बनाना","अभिनेता","सजा हुआ","नाव","मित्र","धैर्य","सदगुण","बगीचा","पहली बार","बैंगन","शबाश","कहीं","उगना","खाली","टोकरी","ध्यान से","पीछे-पीछे","खोज़ना","दौड़ना","भरना","तोड़ना","खराब करना","तेल","मिलना","भुगतान करना","न भूलें","अंगुठा","अत्यधिक","थुलथुल","समय","झूलना","बस करो","चिड़ियाघर","हाथी","हिरन","उछल-कूद","मसखरी करना","लुका-छिपी","दरियायी घोड़ा","बाघ","स्वागत","पूँछ","आसपास","फल","मज़े लेना", "सभी","कुछ और","निकालना","दोनों","जोखिम उठाना","बिना कुछ","हासिल करना","तब से","आज तक","सही","परीक्षा","समद्र-तट","एकदम","फरड़ना"]

	meaning =  ["to be angry","trick","secret","to change","idea","to hurry","to blame","sunshine","majority","to repeat","mammal","revenue","to close","school year","anecdote","to announce", "winner", "lives", "to brush", "by mistake", "needs", "front","sweet","sell","previous","vacation","to hug","to recite","old","poem","question","honesty","to draw","artist","to damage","to divide","equal","let's","parts","how much","to induce","how","fire","glasses","money","to laugh","mouth","eyebrow","wedding","sister","light","to doubt","bed","family","upstairs","to explain","time","alien","solution","custom","all","to know","walk (noun)","any","to choose","example","mistaken","matter","identity","exception","rule","there are","they say","old","hour","tall","next","inside","outside","every","place","don't bother me","perfect","as well","to write","to swim","scary","other","more","to take","to use","nowadays","about","office","to put","where (noun)","then","alas","doorway","very close","to arrive","help (noun)","half hour","afternoon","evening","all (duration)","lady","picture","which","continuous","to dig","fossil","rare","bird","take a photo","pond","enough","winter","throat","to hurt","to graduate","meadow","peak","spread out","history","university","universe","clock","electricity","ago","to fall","which way","to ignore","to imply","speech","tax","to cook","let's see","these ones","to improvise","actor","decorated","boat","mate","patience","virtue","garden","first time","eggplant","well done","somewhere","to grow","empty","basket","carefully","following","to search","to run","to fill","to break","to destroy","oil","to find","to pay","don't forget","thumb","highly","pudgy","period","to swing","stop","zoo","elephant","deer","prance","to clown around","hide and seek","hippo","tiger","welcome","tail","nearby","fruit","to enjoy","everything","something else","to remove","both","to venture","nothing","to acheive","since then","until today","correct","exam","beach","immediately","to tear apart"]

	meaning2 = ["angry","move","secret","change","idea","hurry","blame","sunlight","majority","repeat","mammal","revenue","close","school year","story","announce", "winner", "lives", "brush", "by mistake", "important", "forward","sweet","to sell","last","vacation","hug","recite","old","poem","question","honesty","draw","artist","damage","divide","equal","might as well","parts","how","bring about","like what","fire","glasses","money","augh","face","eyebrows","wedding","sister","light","doubt","bed","family","up","explain","instance","foreign","solution","custom","all","know","walk","any","choose","example","wrong","case","identity","exception","rules","there are","they say that","old","time","long","next","inside","outside","all","space","don't bother me","perfect","also","write","swim","scary","other","more","take","use","these days","regarding","office","put","where","then","alas","door","close","to reach","help","thirty","afternoon","evening","all","woman","photo","which","continuous","dig","fossil","rare","bird","to take a photo","pool","sufficient","winter","throat","hurt","graduate","field","top","extended","history","university","universe","clock","lightning","ago","to drop","which way?","ignore","imply","remark","tax","cook","let's see","these few","improvise","actor","decorated","boat","friend","patience","virtue","garden","first time","eggplant","good job","somewhere","grow","empty","basket","cautiously","in the wake of","search","to scramble","fill","break","destroy","oil","to meet","pay","don't forget","thumb","extremely","tubby","time","swing","stop","zoo","elephant","deer","friskiness","clown around","hide-and-seek","hippopotamus","tiger","welcome","tail","neighbourhood","fruit","enjoy","all","something else","remove","both","venture","nothing","to gain","since then","until now","right","exam","beach","absolutely","to open wide"]

	#Use this if there is a word/meaning missmatch:
	if False:
		for i in range(0,len(words)):
			print(words[i]+" "+meaning[i]+"\n")

	verbs = []
	dicform = []
	verbmeaning = []
	verbmeaning2 = []

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
			mode3 = input("Would you like to study Polite or Dictionary forms? \n")
			if mode3.lower() == "polite":
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
	
