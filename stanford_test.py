#Sentence Tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
import sys
input = ''
with open(sys.argv[1], 'r') as my_file:
    input = my_file.read()
    input = input.replace("."," .")
sents = sent_tokenize(input)
stops = set(stopwords.words('english'))

print (input)

#StanfordPOSTagger converter to Bikel Format
from nltk.tag.stanford import StanfordPOSTagger
postagger = StanfordPOSTagger('english-bidirectional-distsim.tagger')
# postags=[postagger.tag(sent.split()) for sent in sents]
postags_stanford=[]
postags_bikel = "("
for sent in sents:
	postags = postagger.tag(sent.split())
	postags_stanford.append(postags)
	for word in postags:
		postags_bikel+="("+word[0]+" ("+word[1]+"))"

print (postags_stanford)
print (postags_bikel)

#StanfordParser
from nltk.parse.stanford import StanfordParser
parser=StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
# parsed_sents= sum([list(dep_graphs) for dep_graphs in parser.tagged_parse_sents(postags_stanford)],[])
# print (parsed_sents)
parsed_sents= parser.tagged_parse_sents(postags_stanford)
# print (type(parsed_sents))
for sent in parsed_sents:
	try:
		for i in sent:
			print(i)
			next(sent)
	except StopIteration:
		pass	



#Bikel

#PARSEVAL