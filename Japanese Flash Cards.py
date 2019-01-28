import random

print("--Japanese Flash Cards")
print("--Evan Eames")
print("--2012")
print("-------------------------")

score = 0
run = 1
while run == 1:
    hirigana =      ["あ","い","う","え","お","か", "き", "く", "け", "こ", "さ", "し", "す", "せ","そ", "た","ち", "つ", "て", "と","な","に","ぬ","ね", "の","は", "ひ","ふ","へ", "ほ","ま","み","む","め","も", "や","ゆ","よ","ら", "り","る","れ","ろ", "わ","を","ん","が","ぎ","ぐ","げ","ご", "ざ","じ","ず", "ぜ","ぞ","だ","ぢ","づ", "で","ど","ば", "び","ぶ","べ","ぼ", "ぱ","ぴ","ぷ","ぺ","ぽ","きゃ","きゅ","きょ","しゃ","しゅ","しょ","ちゃ","ちゅ","ちょ","にゃ","にゅ","にょ","ひゃ","ひゅ","ひょ","みゃ","みゅ","みょ","りゃ","りゅ","りょ","ぎゃ","ぎゅ","ぎょ","じゃ","じゅ","じょ","びゃ","びゅ","びょ","ぴゃ","ぴゅ","ぴょ"]
    katakana =      ["ア","イ","ウ","エ","オ","カ", "キ", "ク", "ケ", "コ", "サ", "シ", "ス", "セ","ソ", "タ","チ", "ツ", "テ", "ト","ナ","ニ","ヌ","ネ", "ノ","ハ", "ヒ","フ","ヘ", "ホ","マ","ミ","ム","メ","モ", "ヤ","ユ","ヨ","ラ", "リ","ル","レ","ロ", "ワ","ヲ","ン","ガ","ギ","グ","ゲ","ゴ","ザ","ジ","ズ", "ゼ", "ゾ","ダ","ヂ","ヅ","デ","ド","バ", "ビ","ブ","ベ","ボ", "パ","ピ","プ","ペ","ポ","キャ","キュ","キョ","シャ","シュ","ショ","チャ","チュ","チョ","ニャ","ニャ","ニョ","ヒャ","ヒュ","ヒョ","ミャ","ミュ","ミョ","リャ","リュ","リョ","ギャ","ギュ","ギョ","ジャ","ジュ","ジョ","ビャ","ビュ","ビョ","ピャ","ピュ","ピョ"]
    pronunciation = ["a", "i", "u","e", "o", "ka", "ki", "ku","ke", "ko", "sa","shi","su", "se","so","ta","chi","tsu","te","to","na","ni","nu","ne","no","ha","hi","fu","he","ho","ma","mi","mu","me","mo","ya","yu","yo","ra","ri","ru","re","ro","wa","wo","n","ga","gi","gu","ge","go","za","ji","zu","ze","zo","da","ji","zu","de","do","ba","bi","bu","be","bo","pa","pi","pu","pe","po","kya","kyu","kyo", "sha","shu", "sho","cha", "chu","cho","nya", "nyu", "nyo","hya","hyu", "hyo","mya", "myu", "myo","rya", "ryu", "ryo", "gya","gyu","gyo", "ja",  "ju", "jo","bya", "byu", "byo","pya","pyu", "pyo"]

    words = ["かお","あし","せかい","あさ","あかい","あおい","えき","そこ","しお","かさ","きいて","みて","かいて","よんで","いって","ください","すみません","どういたしまして","もの","べっど","いす","つくえ","ほんだな","でんわ","テレピ","ステレオ","ふとん","たんす","おしいれ","まど","ドア","いぬ","ねこ","ほん","ソファ","テーブル","スタンド","しゃしん","とけい","とだな","え","えいご","おとこ","おんな","がくせい","せんこう","だいがく","ともだち","なまえ","どこから　きましたか","あなた","いま","から","ぶつりがく","なん","どこ","だれ","へや","あした","アルバイト","うんどう","おんがく","かいもの","きのう","くるま","ごりょうしん","ざっし","しけん","しごと","じてんしゃ","しゅうまつ","しんぶん","てがみ","ひとりで","あるいて","くに","あたま","あめ","いしゃ","うで","うま","おかあさん","おかし","おじいさん","おとうさん","おとうと","おなか","おにいさん","おねえさん","おばあさん","かぎ","がっこう","かぜ","からだ","かわ","き","きっぷ","ぎゅうにゅう","きょう","くすり","くち","くも","こうこう","こおり","さとう","しゃしん","しゃっくり","しゅっぷつ","しょうがつ","つき","て","でんしゃ","とうり","とり","はな","ひげ","ひざ","ふうせん","ほし","みみ","みょうじ","むすめ","め","やま","ゆき","ゆび","よる","りょこう","きぶんがわるい","かおいろがわるい","のどがいたい","はがいたい","ねつがある","おなか","こし","つまる","かゆい","せきがでる","けんこう","けがをする","びょうきはなる","ゆびをきる","かぜをひく","からだがよわい","くすり","つける","いしゃ","ねつ","はかる","やすむ","にゅういんする","むりをする","あるく","びょうき","かるい","おもい","だいじょうぶ","こまる","どうしたんですか","おだいじに","どうしたらいいですか","しょうじょう","たふん","天気よほう","はれ","くもり","あめ","ゆき","のさ","ときどき","くもる","はれる","ふる","きこう","おおい","すくない","つよい","よわい","かぜ","つめたい","ふく","さがる","あがる","きおん","おしあつい","このは","なる","さく","そら","ので","いがく","じんるいがく","すうがく","せんたくき","たいぞうこ","いろ","デーパック","どころ","まち","むらさき","かていきょうし","たまご","にく","やさい","りんご", "いちご", "えび", "ぎゅうにく", "とりにく", "ぶたにく", "すいえい", "くつ", "くつした", "ふく", "たくさん", "いくつ", "いくら", "たんじょうび", "おしょく", "みず", "いっしょに", "ちょっと", "いいえ、けっこうです。" ,"あたま", "あたまがいい", "かぞく", "かない", "かみ", "からだ", "きょうだい", "しゅじん", "せ", "せいかく", "ぼうし", "めがね", "けっこんする", "つとめている", "やせている", "ふとっている", "いくつ", "さい", "にん" ,"きょういん", "おしり", "ひげ", "ゆび", "あき", "うみ", "おととし", "おかね", "きせつ", "きょうかい", "きょねん", "ことし", "せんげつ", "つり", "どうぶつえん", "なつ", "なつやすみ", "はくぶつかん", "はる", "はるやすみ", "ひこうき", "ふゆ", "ふゆやすみ", "らいげつ", "へんな", "はじめて", "ばんとし", "ひにさ", "あと", "おみやげ", "かいがい", "がいこく", "かんこうりょこう", "くうこう", "けいかく", "ことぼ", "しつもん", "ちず", "つもり", "ばしょ", "まえ", "みずうみ", "みせ", "みんしゅく", "よてい", "りょかん", "りょこう", "りょこうがいしゃ", "よやく", "とくに", "けれども", "それで", "だから", "だけど", "つぎに", "ですから", "というのは", "ところで", "まずはじめに", "また", "まぐろ","うとう","かた"]
    meaning = ["face","leg","world","morning","red","blue","station","bottom","salt","umbrella","listen","look","write","read","repeat","please","sorry","you're welcome","thing","bed","chair","desk","bookshelf","telephone","television","stereo","futon","chest (furniture)","closet","window","door","dog","cat","book","sofa","table","lamp","photo","clock","cabinet","picture","english","male","female","student","major","university","friend","name","Where are you from?","you","now","from","physics","what","where","who","room","tomorrow","part-time job","exercise","music","shopping","yesterday","car","parents","magazine","test","work","bicycle","weekend","newspaper","mail","alone","by foot","country","head","rain","doctor","arm","horse","mother","candy","grandfather","father","yonger brother","stomach","older brother","older sister","grandmother","key","school","wind","body","river","tree","ticket","milk","today","medicine","mouth","cloud","highschool","ice","sugar","photo","hiccup","departure","New Year's Day","moon","hand","train","street","bird","nose","beard","knee","balloon","star","ear","last name","daughter","eye","mountain","snow","finger","night","trip","feel sick","pale","sore throat","toothache","have a fever","stomach","back","blocked","itchy","cough","health","have an injury","get sick","cut one's finger","catch a cold","be weak","medicine","apply","doctor","temperature","measure","be absent","be hospitalized","overstrain","walk","sickness","slight","serious","all right","be troubled","wf happened?","take care","what should I do?","symptoms","probably","weather forecast","sunny","cloudy","rain","snow","and then","sometimes","become cloudy","become sunny","precipitate","climate","a lot","a little","strong","weak","wind","cold","blows","fall","rise","temperature","humid","leaf","become","bloom","sky","because","medical studies","anthropology","mathematics","washing machine","frige","colour","backpack","place","town","purple","private tutor","egg","meat","vegetable","apple","strawberry","shrimp","beef","chicken (meat)","pork","swimming (noun)","shoes","socks","clothing","many/much","how many?","how much?","birthday","japanese food","water","together","a little","no thank you","head","smart","family","wife","hair","body","siblings","husband","height","personality","hat","glasses","to marry","is employed at","thin","fat","How old?","years (counter)","people (counter)","teacher","buttocks","beard","fingers","autumn","ocean","two years ago","money","season","church","last year","this year","last month","fishing","zoo","summer","summer vacation","museum","spring","spring vacation","airplane","winter","winter vacation","next month","strange","first time","a half year","date","after","souvenir","overseas","foreign country","sightseeing (noun)","airport","plan","lexicon","question","map","intention","location","before","lake","store","guest house","schedule","inn","travel","travel agency","reservation","particularly","however","then","so","but (not でも)","next","therefore","it's because","by the way","first of all","also","tuna","free time","how to do something"]
    meaning2 = ["face","leg","world","morning","red","blue","station","bottom","salt","umbrella","listen","look","write","read","repeat","please","sorry","you're welcome","thing","bed","chair","desk","bookshelf","telephone","television","stereo","futon","chest","closet","window","door","dog","cat","book","sofa","table","lamp","photo","clock","cabinet","picture","english","male","female","student","major","university","friend","name","where are you from?","you","now","from","physics","what?","where?","who?","room","tomorrow","part time job","exercise","music","shopping","yesterday","car","parents","magazine","test","work","bicycle","weekend","newspaper","mail","alone","by foot","country","head","rain","doctor","arm","horse","mother","candy","grandfather","father","yonger brother","stomach","older brother","older sister","grandmother","key","school","wind","body","river","tree","ticket","milk","today","medicine","mouth","cloud","highschool","ice","sugar","photo","hiccup","departure","New Year's Day","moon","hand","train","street","bird","nose","beard","knee","balloon","star","ear","last name","daughter","eye","mountain","snow","finger","night","trip","feel sick","pale","sore throat","toothache","have a fever","stomach","back","blocked","itchy","cough","health","have an injury","get sick","cut one's finger","catch a cold","be weak","medicine","apply","doctor","temperature","measure","be absent","be hospitalized","overstrain","walk","sickness","slight","heavy","all right","be troubled","What happened?","take care","What should I do?","symptoms","probably","forecast","sunny","cloudy","rain","snow","and then","with occasional","become cloudy","become sunny","precipitate","climate","a lot","a little","strong","weak","wind","cold","blows","fall","rise","temperature","humid","leaf","become","bloom","sky","because","medicine","anthropology","math","washing machine","refrigerator","color","napsack","place","city","purple","tutor","egg","meat","veggie","apple","strawberry","shrimp","beef","chicken","pork","swimming","shoes","socks","clothes","many","How many?","How much?","birthday","Japanese food","water","together","a little bit","no thanks","head","intelligent","family","wife","hair","body","siblings","husband","back","personality","cap","glasses","marry","works for","is skinny","is fat","how old?","years old","people","professor","bum","mustache","finger","fall","sea","the year before last","cash","season","church","last year","this year","last month","fishing","zoo","summer","summer break","museum","spring","spring break","plane","winter","winter break","next month","weird","for the first time","half year","date","after","souvenir","overseas","new country","sightseeing","airport","plan","language","question","map","intent","locale","before","lake","shop","guest house","plan","inn","trip","travel agency","reservation","especially","however","so","so","but","next","so","because","btw","firstly","also","tuna","free time","how to"]

    verbs = ["おきます","シャワーを　あびます","たべます","いきます","きます","じゅぎょうが　あります","べんきょうします","おわります","はじまります","かえります","しゅくだいを　します","おふろに　はいります","よみます","みます","ねます","のみます","つくります","せんたくを　します","そうじを　します","かきます","ききます","かいます","でかけます","はなします","つかいます","かします","とります","おしえます","タクシーのります","まちます","よびます","すわります","たちます","わかります","およぎます","つけます","けします","あけます","しめます","あそびます","いれます","みせます","もちます","すいます","なきます","のぼります","わらいます","いいます","おもいます","さがします","つかいます","つきます","とまります","はらいます","もっていきます","こたえます","しっています","しっていません","しらべます","たてます","でます","わすれます","たのみます","やります","かします","かりします","かえします","つれていきます","つれてきます","もっていきます","もってきます","おします","おぼえます","てつだいます","おくります"]
    dicform = ["おきる","シャワーを　あびる","たべる","いく","くる","じゅぎょうが　ある","べんきょうする","おわる","はじまる","かえる","しゅくだいを　する","おふろに　はいる","よむ","みる","ねる","のむ","つくる","せんたくを　する","そうじを　する","かく","きく","かう","でかける","はなす","つかう","かす","とる","おしえる","タクシーのる","まつ","よぶ","すわる","たつ","わかる","およぐ","つける","けす","あける","しめる","あそぶ","いれる","みせる","もつ","すう","なく","のぼる","わらう","いう","おもう","さがす","つかう","つく","とまる","はらう","もっていく","こたえる","しっている","しらない","しらべる","たてる","でる","わすれる","たのむ","やる","かす","かりる","かえす","つれていく","つれてきる","もっていく","もってきる","おす","おぼえる","てつだう","おくる"]
    verbmeaning = ["wake up","take a shower","eat","go","come","have class","study","end","begin","return","do homework","take a bath","read","watch","go to bed","drink","make","do laundry","clean","write","listen","buy","go out","speak","use","lend","take","teach","take a taxi","wait","call out","sit","stand","understand","swim","turn on","turn off","open","close","play","put in","show","hold","smoke","cry","climb","laugh","say","think","look for","use","arrive","stay at","pay","take","answer","know","don't know","explore","build","leave","forget","ask a favour","do a favour","lend","borrow","return","take someone","bring someone","take something","bring something","push","memorize","help out","send"]
    verbmeaning2 = ["wake","shower","eat","go","come","have class","study","end","begin","return","do homework","bathe","read","watch","go to sleep","drink","make","do laundry","clean","write","listen","buy","go out","speak","use","lend","take","teach","mount","wait","call out","sit","stand","understand","swim","turn on","turn off","open","close","play","put in","show","hold","sip","cry","climb","smile","say","think","look for","use","arrive","stay at","pay","take","answer","know","don't know","check","make","leave","forget","ask","do","lend","borrow","give back","take","bring","take","bring","push","memorize","lend a hand","send"]

    adjectives = ["おおきい","ちいさい","ながい","みじかい","たかい","ひくい","やすい","あたらしい","ふるい","おもい","かるい","ひろい","せまい","あかるい","くらい","あつい","さむい","つめたい","おもしろい","つまらない","やさしい","むずかしい","おいしい","まずい","あまい","からい","しろい","くろい","あかい","あおい","きいろい","ちゃいろい","はやい","おそい","とおい","ちかい","しずかな","うるさい","きれいな","きたない","いそかしい","ひまな","ハンサムな","にぎやかな","べんりな","ふべんな","かんたんな","ふくざつな","すきな","きらいな","ゆうめいな","しんせつな","ふしんせつな","いい","わるい","りっぱな","すてきな","たのしい","ざんねん","たいへん","あたたかい","あつい","うれしい","かなしい","さびしい","さむい","すずしい"]
    adjmeaning = ["big","small","long","short","tall","low","cheap","new","old","heavy","light","spacious","cramped","bright","dark","hot","cold weather","cold","interesting","boring","easy","difficult","tasty","bad-tasting","sweet","spicy","white","black","red","blue","yellow","brown","fast","slow","far","close","quiet","noisy","clean","dirty","busy","leisurely","handsome","lively","convenient","inconvenient","simple","complicated","likeable","dislikeable","famous","kind","unkind","good","bad","fine","attractive","fun","unfortunate","tough","warm","hot","happy","sad","lonely","cold","cool"]
    adjmeaning2 = ["big","small","long","short","expensive","low","cheap","new","old","heavy","light","wide","narrow","bright","dark","hot","cold weather","cold","interesting","boring","easy","difficult","tasty","bad-tasting","sweet","spicy","white","black","red","blue","yellow","brown","early","late","far","close","quiet","loud","beautiful","dirty","busy","free","handsome","lively","convenient","inconvenient","simple","complicated","likeable","dislikeable","famous","kind","unkind","good","bad","fine","attractive","fun","sorry","hectic","warm","hot","joyful","sad","ronery","cold","cool"]

    prompt1 = "Please input meaning \n"
    prompt2 = "Please input characters \n"

    mode = input("What would you like to study? Hirigana, Katakana or Vocab? \n")
    if mode == "Hirigana" or mode == "hirigana":
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
        elif mode2 == "Verbs" or mode2 == "verbs":
            mode3 = input("Would you like to study Polite or Dictionary forms? \n")
            if mode3 == "Polite" or mode3 == "polite":
                print('Type "reverse" at any point to reverse input mode\nType "end" at any point to try something else\nType "quit" at any point to quit\n-----')
                n=4
            elif mode3 == "Dictionary" or mode3 == "dictionary":
                print('Type "reverse" at any point to reverse input mode\nType "end" at any point to try something else\nType "quit" at any point to quit\n-----')
                verbs = dicform
                n=4
    elif mode == "Katakana" or mode == "katakana":
        print('Type "end" at any point to try something else \nType "quit" at any point to quit\n-----')
        n=5
    elif mode == "Test" or mode == "test":
        n = 6

    while n == 1:
        symbol = random.choice(hirigana)
        print(symbol)
        g = hirigana.index(symbol)
        answer = input("Please input pronunciation \n")
        if answer == pronunciation[g]:
            print("Correct! \n-----")
        elif answer == "end" or answer == "End":
            n = 0
        elif answer == "quit" or answer == "Quit":
            n = 0
            run = 0
        elif answer == "Go West" or answer == "go west":
            print("You go West, you come to a river, possible directions are north, east and japan")
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
        symbol = random.choice(verbs)
        print(symbol)
        g = verbs.index(symbol)
        answer = input(prompt1)
        if answer == verbmeaning[g] or answer == verbmeaning2[g]:
            print("Correct! \n-----")
        elif answer == "end" or answer == "End":
            n = 0
        elif answer == "quit" or answer == "Quit":
            n = 0
            run = 0
        elif answer == "reverse" or answer == "Reverse":
            temp = verbmeaning
            verbmeaning = verbs
            verbs = temp
            temp = prompt1
            prompt1 = prompt2
            prompt2 = temp
            print("Input mode reversed. \n-----")
        else:
            print("Incorrect, the correct answer is " + str(verbmeaning[g]) + ". \n-----")

    while n == 5:
        symbol = random.choice(katakana)
        print(symbol)
        g = katakana.index(symbol)
        answer = input("Please input pronunciation \n")
        if answer == pronunciation[g]:
            print("Correct! \n-----")
        elif answer == "end" or answer == "End":
            n = 0
        elif answer == "quit" or answer == "Quit":
            n = 0
            run = 0
        else:
            print("Incorrect, the correct pronunciation is " + str(pronunciation[g]) + ". \n-----")
