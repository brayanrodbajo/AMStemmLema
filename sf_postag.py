from nltk.tree import Tree
from nltk.parse.stanford import StanfordParser
parser=StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")

# parsed = parser.raw_parse("The boy is blue.")

#print(list(parsed))
# try:
# 	for i in parsed:
# 	 	print(i)
# 	 	next(parsed)
# except StopIteration:
#     pass

postags=[[('Hello', 'UH'), ('Mr.', 'NNP'), ('Smith,', 'NNP'), ('how', 'WRB'), ('are', 'VBP'), ('you', 'PRP'), ('doing', 'VBG'), ('today?', 'NN')],
[('The', 'DT'), ('weather', 'NN'), ('is', 'VBZ'), ('great,', 'NNP'), ('and', 'CC'), ('Python', 'NNP'), ('is', 'VBZ'), ('awesome.', 'NN')]]
# parsed= parser.tagged_parse_sents(postags)
# try:
# 	#For each sentence
# 	j =0
# 	for sent in parsed:
# 		print (sent)
# 		for i in sent:
# 			print(i)
# 			next(sent)
# 		next(parsed)
# 		j+=1
# except StopIteration:
# 	pass

# parsed_sents= sum([list(dep_graphs) for dep_graphs in parser.tagged_parse_sents(postags)],[])# doctest: +NORMALIZE_WHITESPACE
parsed =  parser.tagged_parse_sents(postags)
parsed_sents= []
for sent in parsed:
	# print(list(sent))
	try:
		for i in sent:
			print(i)
			next(sent)
	except StopIteration:
		pass	

# vp = Tree('VP', [Tree('V', ['saw']),Tree('NP', ['him'])])
# s = Tree('S', [Tree('NP', ['I']), vp])
# print (s)