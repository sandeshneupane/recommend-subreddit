import re
import ast
from enum import IntEnum


class Labels(IntEnum):
	hiking = 0
	hacking = 1
	Fitness = 2
	iphone = 3
	gaming = 4
	science = 5
	Art = 6
	explainlikeimfive = 7
	travel = 8
	technology = 9
	Documentaries = 10
	politics = 11
	MMA = 12
	computer = 13
	relationship_advice = 14
	storage = 15
	AnimalCrossing = 16
	UpliftingNews = 17
	Futurology = 18
	JoeRogan = 19
	Economics = 20
	shrooms = 21
	MovieDetails = 22
	careerguidance = 23
	askscience = 24
	coding = 25
	funny = 26
	snakes = 27
	worldpolitics = 28
	amazon = 29
	soccer = 30
	techsupport = 31
	aww = 32
	linux = 33
	space = 34
	walmart = 35
	Astronomy = 36
	news = 37
	americanairlines = 38
	Showerthoughts = 39
	aggies = 40
	help = 41
	nasa = 42
	legaladvice = 43
	hiphopheads = 44
	manga = 45
	history = 46
	cscareerquestions = 47
	Bitcoin = 48
	Coronavirus = 49
	sports = 50
	apple = 51
	BasicIncome = 52
	learnpython = 53
	oculus = 54
	AskHistorians = 55
	sysadmin = 56
	Steam = 57
	exit = 58
	computervision = 59
	dataisbeautiful = 60
	india = 61
	trashy = 62
	financialindependence = 63
	atheism = 64
	nba = 65
	ethereum = 66
	recipes = 67
	mildlyinteresting = 68
	relationships = 69
	modernwarfare = 70
	drawing = 71
	philosophy = 72
	texas = 73
	gardening = 74
	AskWomen = 75
	javahelp = 76
	google = 77
	movies = 78
	literature = 79
	DIY = 80
	GetMotivated = 81
	programming = 82
	pharmacy = 83
	worldnews = 84
	ComputerEngineering = 85
	btc = 86
	CryptoCurrency = 87
	tifu = 88
	offmychest = 89
	guns = 90
	learnprogramming = 91
	chemistry = 92
	Cooking = 93
	MachineLearning = 94
	resumes = 95
	learnjava = 96
	TAMU = 97
	CasualConversation = 98
	Fantasy = 99
	Music = 100
	europe = 101
	nvidia = 102
	todayilearned = 103
	marvelstudios = 104
	conspiracy = 105
	camping = 106
	unpopularopinion = 107
	pics = 108
	self = 109
	nfl = 110
	AMA = 111
	australia = 112
	dating_advice = 113
	Jokes = 114
	Tinder = 115
	keto = 116
	datascience = 117
	teenagers = 118
	anime = 119
	datastorage = 120
	computerscience = 121
	AskReddit = 122
	wow = 123
	gmaing = 124
	GetEmployed = 125
	videos = 126
	pcgaming = 127
	lifehacks = 128
	jobs = 129
	JobFair = 130
	Parenting = 131
	NoStupidQuestions = 132
	bodybuilding = 133
	socialskills = 134
	Home = 135
	biology = 136
	UTAustin = 137
	AskMen = 138
	memes = 139
	cars = 140
	food = 141
	csMajors = 142
	Python = 143
	Minecraft = 144
	leagueoflegends = 145
	italy = 146
	wallstreetbets = 147
	LifeProTips = 148


class Dataset:
	TRAIN = "modules/datas/train.txt"

	def __init__(self, split='train'):
		self.data = []
		self.docs_path = self.TRAIN

		self.read_dataset()
		

	def read_dataset(self):
		with open(self.docs_path, 'r') as file :
			filedata = file.read().split('\n\n')
			for i in range(len(filedata)):
				myList = ast.literal_eval(filedata[i])
				bodyTitle = myList[0] #taking title only
				labl = Labels.__dict__[myList[1]].value
				bodyTitle = re.sub(r'\r\n', " ", bodyTitle)
				bodyTitle = re.sub(r"[^a-zA-Z]+", " ", bodyTitle)
				bodyTitle = re.sub(r'[" "]+', " ", bodyTitle)
				self.data.append((bodyTitle, Labels(int(labl))))


	def fetch(self):
		return self.data
