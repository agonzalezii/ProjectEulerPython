from utils import is_triangular, word_sum

f = open('p042_words.txt','r')
content = f.read()
content = content.replace("\"","")

words = content.split(",")

triangle_words = 0

for word in words:
	word_value = word_sum(word)
	if(is_triangular(word_value)):
		triangle_words += 1
		
	#print(word_sum)
print(triangle_words)