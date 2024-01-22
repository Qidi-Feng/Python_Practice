from collections import Counter
word_num = int(input())
word_order = list()
word_content = {}
#save the words into dic and list
for _ in range(word_num):
    word = input()
    word_order.append(word)
word_content = Counter(word_order)
unique = 0
#calcualte the unqiue number
unique_list= list(word_content.keys())
print(len(unique_list))
#print out the times of all words
res = list()
for word in word_order:
    if word_content[word]:
        res.append(word_content[word])
        del word_content[word]
    else:
        next
#print the number out
for i in res: print(i,end=' ')

