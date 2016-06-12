#Sentence Tokenize
from nltk.tokenize import sent_tokenize
import sys
input = ''
with open(sys.argv[1], 'r') as my_file:
    input = my_file.read()
sents = sent_tokenize(input)
print (input)

#StanfordPOSTagger
from nltk.tag.stanford import StanfordPOSTagger
postagger = StanfordPOSTagger('english-bidirectional-distsim.tagger')
postags=[]
for sent in sents:
	print (postagger.tag(sent.split()))
	postags.append(postagger.tag(sent.split()))

#StanfordParser
from nltk.parse.stanford import StanfordParser
parser=StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
parsed_sents= sum([list(dep_graphs) for dep_graphs in parser.tagged_parse_sents(postags)],[])
print (parsed_sents)

#Bikel

#PARSEVAL