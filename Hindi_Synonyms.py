import random

mode = input("Do you want to study synonyms or antonyms?\n")

if mode.lower() == "synonyms":
	a = ["आँख", "भूमि","पानी","मित्र","बादल","सूर्य","चाँद","रात","दिन","फूल","पेड़","पक्षी","शाम","सुबह","हवा","पत्र","दुनिया","आसमान","बारिश"]
	b = [["नैन","नयन","चक्षु","लोचन"], ["पृथ्वी","भू","धरा","धरती"], ["नीर","तोय","अंबु","जल"], ["दोस्त","सखा","सहचर","साथी"], ["मेघ","जलधर","पयोद","घन"], ["सूरज","दिनेश","दिवाकर","दिनकर"], ["शशि","मयंक","राकेश","चन्द्रमा"], ["रात्रि","निशा","यामिनी","रजनी"], ["दिवस","वासर","दिवा","वार"], ["पुष्प","सुमन","प्रसून","कुसुम"],["वृक्ष","तरु","बिरवा","विटप"], ["खग","विहग","पंछी","पखेरु"],["सायं","संध्या","साँझ"],["प्रात:","सवेरा","भोर","प्रभात"],["पवन","वायु","अनिल","समीर"],["चिट्ठी","खत"],["संसार","जग","जगत"],["नभ","व्योम","आकाश","गगन"],["बरसात","बरखा","वृष्टि","वर्षा"]]

	Flawless = True
	while len(a) != 0:
		word = random.choice(a)
		print(word)
		g = a.index(word)
		while len(b[g]) != 0:
			answer = input("Please input synonyms \n")
			if answer in b[g]:
				if len(b[g]) == 1:
					print("Correct! \n-----")
					del b[g][0]
					del a[g]
				else:
					del b[g][b[g].index(answer)]
					print("Yes. "+str(len(b[g]))+" more to go.")
			else:
				print("Incorrect. Try again.")
				Flawless = False
		del b[g]

	if Flawless:
		print("Flawless success!!!")
	else:
		print("Success!")	

elif mode.lower() == "antonyms":
	a = ["Outside","Inside","Friend", "Enemy", "Fearful", "Fearless", "Foreign", "Local", "Absent", "Present", "False", "True", "Grief", "Happiness", "Unhealthy", "Healthy", "Healthy Person", "Sick Person", "Light", "Heavy", "Heroic", "Coward", "Outsider", "Insider", "Straight", "Inverted", "Evil", "Noble", "Good", "Bad", "Weak", "Strong", "Poor", "Rich", "Laugh", "Cry", "More", "Less", "Difficult", "Simple", "Answer", "Question", "Win", "Loss", "Close", "Far"]
	b = ["भीतर","बाहर","शत्रु", "मित्र", "निडर", "डरपोक", "देशी", "विदेशी", "उपस्थित", "अनुपस्थित", "सच्चा", "झूठा", "सुख", "दुःख", "स्वस्थ", "अस्वस्थ", "रोगी", "निरोगी", "भारी", "हलका", "कायर", "वीर", "अपना", "पराया", "उलटा", "सीधा", "नेक", "दुष्ट", "बुरा", "भला", "पक्का", "कच्चा", "अमीर", "गरीब", "रोना", "हँसना", "कम", "अधिक", "सरल", "कठिन", "प्रश्न", "उत्तर", "हार", "जीत", "दूर", "निकट"]

	Flawless = True
	while len(a) != 0:
		word = random.choice(a)
		g = a.index(word)
		answer = input("Please give the antonym of '" + word +"'.\n")
		if answer == b[g]:
			print("Correct! \n-----")
			del a[g]
			del b[g]
		else:
			print("Incorrect. Try again.")
			Flawless = False

	if Flawless:
		print("Flawless success!!!")
	else:
		print("Success!")

else:
	print("Selection not recognized; must be 'synonyms' or 'antonyms'. Exiting...")
