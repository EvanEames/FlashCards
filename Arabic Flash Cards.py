import random

print("-- Arabic Flash Cards")
print("--Evan Eames")
print("--2013")
print("-------------------------")

score = 0
run = 1
while run == 1:
    letters = ["ض","ص","ث","ق","ف","غ","ع","ه","خ","ح","ج","د","ذ","ش","س","ي","ب","ل","ا","ت","ن","م","ك","ط","ئ","ء","ؤ","ر","ل","ا","ى","ة","و","ز","ظ","أ","إ"]
    numbers = ["واحِد","إثنان","ثلاثة","أرْبَعَة","خَمْسة","سِتَّة","سَبْعَة","ثَمانِيَة","تِسْعَة","عَشْرَة","أحَد عَشَر","اِثنا عَشَر","ثَلاثة عشر","أربَة عشر","خَمسَة عَشَر","سِتّة عشر","سَبعة عشر","ثَمانِية عشر","تِسعة عشر","عِشرونَ","ثَلاثونَ","أربَعونَ","جَمسونَ","سِتّونَ","سَبعونَ","ثَمانونَ","تِسعونَ","مِئة"]
    numbermeaning = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventee","eighteen","nineteen","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety","one hundred"]
    pronunciation = ["ض","ص","ث","ق","ف","غ","ع","ه","خ","ح","ج","د","ذ","ش","س","ي","ب","ل","ا","ت","ن","م","ك","ط","ئ","ء","ؤ","ر","ل","ا","ى","ة","و","ز","ظ","أ","إ"]

    words = ["طِوال","بِفَضل","أَلْتَحِق بِ","مِثلَ","أَنجَح في","اُمّ","أَدخُل","اُذاكِر","رَأي","أَرفُض","يوقِظني","يَنْزِل من","قليلاً","يَفطُر","الغَداء","حَوالَيْ","خاصّ","يُدَخِّن","بَعدَ الظُّهْر","يَعود الى","آخّر","يَبدَأ","بعض","جَريدة","يَجلِس","يُقيم","أَكثَر","لَيلة","اللَّيلة","مَوعِد","يَسْهَر","يُصْبِع","يَصحو","الصَّلاة","يَفْهَم","مُتَأَخِّر","مُبَاراة","جامِع","يَجيء إلى","بِسُرعة","عِندما","فُندُق","يَنْقَطِع","مَرّة","مَعًا","مُهَنْدِس","صَيْدَلِيّة","عِدة","يَتَعَرَّف على","عاطِفيّ","عَلاقة","يَتَبادَل","تَجْرِبة","الخَجَل","خُطِبَت لِ","السِّياحة","عُيِّنْتُ","يَتَغَيَّب عن","يُقَرَّر","يَقْضي","هُنا","وَفاة","مِنْحة","يَزور","بِالإضافة إلى","طَبْعًا","عُطلة","يَعْلَم","الحَياة","جَميعًا","يَبْقى","آخِر","يَأخُذ","وَظيفة","مَقالة","كَذالِك","مُناسِب","ينتَهي من","يَجِد","الغُربة","فُرْصة","يَفْشَل","يَفصِل","يَسْتَقِرّ","يَرغَب في","ما زِلتُ","يُشَجِّع على","يَظُنّ أنّ","يَعني","أمامَ","مَجَلّة","حَضَرَ إلى","يَحضُر","يَرجِع","كانَت","ماتَت","أكْبَرهم","أكبر","الاِقتِصاد","تَعيش","عامّ","حادِث","جَدّ","الثّانَوِيّة العامّة","ثانَوِيّ","أُولى","اليَوم","يَوم","مُنذُ","لِذ’لِك","لِماذا","سَنة","أُسْبوع","أذهَب إلى","تَخَرَّجْمِن","مُحاضَرة","الحُسول على","أحسُل على","التِّجارة","بِالنسبة","كَثيراً","فَقَط","فَصل دراسيّ","عالِية","الصَّيف","أشعُر","الشِّتاء","الرَّبيع","دَرَجة الحَرارة","دَرَجة","الخَريف","كُلَ","كانَ","كُنتُ","أحْيانًا","صَديقة","الطُّفولة","فَرد","قَبْلَ","رابِع","زَميل","السَّفَر","أتَذَكَّر","أوَّل","اِبتِدائيّ","أحفَظ","مَدرَسة","كلية","قريب","عائلة","عم","علم","أعرف","ضابط","صورة","زوجة","زوجها","زوج","رسالة","يدرس","في الحقيقة","جيش","إبن عم","أبناء","إبن","الآن","أُسرتُهُ","مُوظّف","وحيد","النهار","المساء","لُغة","لي","القُبول","فِعلاً","العمل","مشغول","الشُغل","أِسمُها","دائِمًا","خالة","مُتخصّص","حتثُ","مُترجِم","الترجمة","أيضًا","أُسرة","الأدب","الأمم التّحدة","أدرس","أسكن","تعمل","يعمل","مصريّ","منطقة","نفس","والد","والدة"]
    meaning = ["throughout","thanks to","I join","like","I succeed in","mother","I enter","I study","opinion","I refuse","he wakes me up","he leaves from","a little","he eats breakfast","lunch","approximately","special","he smokes","afternoon","he returns to","other","he begins","some of","newspaper","he sits","he resides","more","night","tonight","appointment","he stays up late","he becomes","he wakes up","prayer","he understands","late","match","mosque","he comes to","quickly","when (non-interrogative)","hotel","he is cut off","once","together","engineer","pharmacy","several","he gets to know","romantic","relationship","he exchanges","experience","shyness","she got engaged to","tourism","I was appointed","he was absent from","he decides","to spend","scholarship","here","death","he visits","in addition to","of course","day off","he learns","life","all together","he stays","the last","he takes","job","article","likewise","appropriate","he finishes","he finds","homesickness","opportunity","he fails","he fires","he settles down","he desires","I continue to","he encourages","he thinks that","it means","in front of","magazine","come to","he attends","he returns","she was","she died","the oldest","oldest","economics","she lives","general","accident","grandfather","baccalaureate","secondary","first","today","day","since","so","why","year","week","I go to","graduated","lecture","to get","I get","trade","as far as","a lot","only","semester","high","summer","I feel","winter","spring","temperature","degree","autumn","all","he was","I was","sometimes","friend","childhood","individual","before","fourth","classmate","traveling","remember","first","primary","memorize","school","college","relative","extended family","paternal uncle","science","I know","officer","picture","wife","her husband","husband","letter","he teaches","actually","army","male paternal cousin","sons","son","now","his family","employee","only","daytime","evening","language","I have","admission","really!","work","busy","work","her name","always","maternal aunt","specializing","where","translator","translation","also","family","literature","United Nations","I study","I live","she works","he works","Egyptian","area","same","father","mother"]
    meaning2 = ["during","thanks to","I enter","like","I pass in","mother","to enter","to study","opinion","to refuse","he wakes me up","to leave from","a bit","to eat breakfast","lunch","around","private","to smoke","afternoon","to return to","other","to begin","some","newspaper","to sit","he lives","more","night","tonight","fixed time","to stay up late","to become","to wake up","praying","to understand","late","game","mosque","ome to","quick","when","hotel","to be cut off","one time","together","engineer","pharmacy","several","he meets","emotional","relationship","exchange","an experience","embarassment","engaged to","tourism","appointed","he missed","decide","spend time","grant","here","dying","visit","furthermore","naturally","holiday","learn","life","all together","he remains","last","take","position","article","also","suitable","to finish","find","feeling of being a stranger","chance","to fail","to fire","become stable","he wishes to","still","encourage","think","like","before","journal","come","attend","return","it was","died","oldest","biggest","economy","lives","public","accident","grandfather","bachelors","secondary","first","today","day","ago","thus","why","year","week","I go to","I graduated","lecture","getting","obtain","commerce","as far as","a lot","only","semester","high","summer","I feel","winter","spring","temperature","degree","fall","every","he was","I was","sometimes","friend","childhood","person","before","fourth","classmate","traveling","I remember","first","elementary","I memorize","school","college","relative","family","uncle","science","know","officer","picture","wife","her husband","husband","letter","he teaches","actually","army","cousin","sons","son","now","his family","employee","lonely","daytime","evening","language","have","admission","really","work","busy","work","her name","always","aunt","specializing","where","translator","translation","also","family","literature","united nations","I study","I live","she works","he works","egyptian","area","same","father","mother"]

    singular = []
    plural = []
    plural2 = []
    
    adjectives = ["قريب من","بعيد عن","تعبان","بردان","حران","عطشان","زعلان","سعيد","مريض"]
    adjmeaning = ["close to","far from","tired","cold","hot","thirsty","hungry","happy","sick"]
    adjmeaning2 = ["close","far","tired","cold","hot","thirsty","hungry","happy","sick"]
    
    prompt1 = "Please input meaning \n"
    prompt2 = "Please input characters \n"

    mode = input("What would you like to study? Letters, Numbers, Vocab, or Plurals? \n")
    if mode == "Letters" or mode == "letters":
        print('Type "end" at any point to try something else \nType "quit" at any point to quit\n-----')
        n=1
    elif mode == "Vocab" or mode == "vocab":
        mode2 = input("Would you like to study Adjectives, Verbs or General Vocab? \n")
        if mode2 == "General Vocab" or mode2 == "general vocab":
            print('Type "reverse" at any point to reverse input mode\nType "end" at any point to try something else\nType "quit" at any point to quit\n-----')
            n=2
        elif mode2 == "Adjectives" or mode2 == "adjectives":
            print('Type "reverse" at any point to reverse input mode\nType "end" at any point to try something else\nType "quit" at any point to quit\n-----')
            n=3
            adj2 = adjmeaning2
        elif mode2 == "Plurals" or mode2 == "plurals":
            print('Type "reverse" at any point to reverse input mode\nType "end" at any point to try something else\nType "quit" at any point to quit\n-----')
            n=4
    elif mode == "Numbers" or mode == "numbers":
        print('Type "end" at any point to try something else \nType "quit" at any point to quit\n-----')
        n=5
    elif mode == "Test" or mode == "test":
        n = 6

    while n == 1:
        symbol = random.choice(letters)
        print(symbol)
        g = letters.index(symbol)
        answer = input("Please input letter \n")
        if answer == pronunciation[g]:
            print("Correct! \n-----")
        elif answer == "end" or answer == "End":
            n = 0
        elif answer == "quit" or answer == "Quit":
            n = 0
            run = 0
        elif answer == "Go West" or answer == "go west":
            print("You go West, you come to a river, possible directions are north, east, and egypt")
        else:
            print("Incorrect, the correct letter is " + str(pronunciation[g]) + ". \n-----")

    while n == 2:
        symbol = random.choice(words)
        print(symbol)
        g = words.index(symbol)
        answer = input(prompt1)
        if answer == meaning[g] or answer == meaning2[g]:
            score = score + 1
            print("Correct!\nCombo: " + str(score)+"\n-----")
        elif answer == "end" or answer == "End":
            n = 0
        elif answer == "quit" or answer == "Quit":
            n = 0
            run = 0
        elif answer == "reverse" or answer == "Reverse":
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
        elif answer == "end" or answer == "End":
            n = 0
        elif answer == "quit" or answer == "Quit":
            n = 0
            run = 0
        elif answer == "reverse" or answer == "Reverse":
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
        symbol = random.choice(singular)
        print(symbol)
        g = verbs.index(symbol)
        answer = input(prompt1)
        if answer == plural[g] or answer == plural2[g]:
            print("Correct! \n-----")
        elif answer == "end" or answer == "End":
            n = 0
        elif answer == "quit" or answer == "Quit":
            n = 0
            run = 0
        elif answer == "reverse" or answer == "Reverse":
            temp = plural
            plural = singular
            singular = temp
            temp = prompt1
            prompt1 = prompt2
            prompt2 = temp
            print("Input mode reversed. \n-----")
        else:
            print("Incorrect, the correct answer is " + str(verbmeaning[g]) + ". \n-----")

    while n == 5:
        symbol = random.choice(numbers)
        print(symbol)
        g = numbers.index(symbol)
        answer = input("Please input value \n")
        if answer == numbermeaning[g]:
            print("Correct! \n-----")
        elif answer == "end" or answer == "End":
            n = 0
        elif answer == "quit" or answer == "Quit":
            n = 0
            run = 0
        else:
            print("Incorrect, the correct answer is " + str(numbermeaning[g]) + ". \n-----")
