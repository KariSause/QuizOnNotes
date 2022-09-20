import random 
capitals = {'Austria': 'Vienna', 'Albania': 'Tirana', 'Belarus': 'Minsk', 'Belgium': 'Brussels', 'Bulgaria': 'Sofia', 'Bosnia and Herzegovina': 'Sarajevo', 'Vatican': 'Vatican', 'United Kingdom': 'London', 'Hungary': 'Budapest', 'Germany': 'Berlin', 'Greece': 'Athens', 'Denmark': 'Copenhagen', 'Ireland': 'Dublin', 'Iceland': 'Reykjavik', 'Spain': 'Madrid', 'Italy': 'Rome', 'Kosovo': 'Pristina', 'Latvia': 'Riga', 'Lithuania': 'Vilnius', 'Liechtenstein': 'Vaduz', 'Luxembourg': 'Luxembourg', 'Macedonia': 'Skopje', 'Malta': 'Valletta', 'Moldova': 'Chisinau', 'Monaco': 'Monaco', 'Netherlands': 'Amsterdam', 'Norway': 'Oslo', 'Poland': 'Warsaw', 'Portugal': 'Lisbon', 'Russia': 'Moscow', 'Romania': 'Bucharest', 'San-Marino': 'San-Marino', 'Serbia': 'Belgrade', 'Slovakia': 'Bratislava', 'Slovenia': 'Ljubljana', 'Ukraine': 'Kiev', 'Finland': 'Helsinki', 'France': 'Paris', 'Croatia': 'Zagreb', 'Montenegro': 'Podgorica', 'Czech Republic': 'Prague', 'Switzerland': 'Bern', 'Sweden': 'Stockholm', 'Estonia': 'Tallinn', 'Japan': 'Tokyo', 'Iran': 'Tehran', 'Afghanistan' : 'Kabul', 'Azerbaijan': 'Baku', 'China': 'Beijing', 'India': 'New Delhi'}
for quizNum  in range(35):
	quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
	answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
	quizFile.write("Имя:\n\nДата:\n\nКурс:\n\n")
	quizFile.write((" " * 15)+ "Проверка знаний столиц стран Европы (Билет %s)" % (quizNum + 1))
	quizFile.write("\n\n")
	states = list(capitals.keys())
	
	random.shuffle(states)
	for questionNum in range(50):
		print(questionNum)
		state = states[questionNum]
		correctAnswer = capitals[state]
		wrongAnswer = list(capitals.values())
		del wrongAnswer[wrongAnswer.index(correctAnswer)]
		wrongAnswer = random.sample(wrongAnswer, 3)
		answerOptions = wrongAnswer + [correctAnswer]
		random.shuffle(answerOptions)

		quizFile.write('%s. Выберите столицу страны %s.\n\n' % (questionNum+1, states[questionNum]))
		for i in range(4):
			quizFile.write("%s. %s\n" % ("ABCD"[i],answerOptions[i]))
		quizFile.write('\n\n\n')


		answerKeyFile.write("%s. %s\n" % (questionNum + 1, "ABCD"[answerOptions.index(correctAnswer)]))
	quizFile.close()
	answerKeyFile.close()