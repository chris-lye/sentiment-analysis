import nltk
import matplotlib.pyplot as plt
from nltk.corpus import opinion_lexicon

nltk.download('opinion_lexicon') #Download Opinion Dictionary
positive_wds = set(opinion_lexicon.positive())
negative_wds = set(opinion_lexicon.negative())

textfile = open('../FrankensteinText.txt','r', encoding="utf8")

def score_line(line):
    """Returns a score btw -1 and 1"""
    line = [e.lower() for e in line.split() if e.isalnum()]
    total = len(line)
    pos = len([e for e in line if e in positive_wds])
    neg = len([e for e in line if e in negative_wds])
    if total > 0:
        return (pos - neg)
    else:
        return 0

line_score = {}
line_num = 1

for line in textfile:
    score = score_line(line)
    line_score.update({line_num: score})
    line_num += 1
    
total_lines = line_num
lists = sorted(line_score.items()) # sorted by key, return a list of tuples

count = 1
accum_score = 0
line_num = 0
new_line_score = {}
for lines_tuple in lists:
    accum_score += lines_tuple[1]
    line_num = lines_tuple[0]
    if count == 100:
        new_line_score.update({(line_num/total_lines): accum_score} )
        count = 1
        accum_score = 0
    count += 1

if count > 1:
    new_line_score.update({(line_num/total_lines): accum_score} )
    
lists2 = sorted(new_line_score.items())
    
x, y = zip(*lists2) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()


# Log
# opinion_lexicon from nltk doesn't seem to work on frankenstein
# ok nvm i forgot to split into words instead of characters 