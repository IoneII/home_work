file = open('prices.txt', 'r', encoding='utf-8')
content = file.readlines()
text_list =[]
for text in content:
    text_list.append([i for i in text.split()])
print(sum(list((map(lambda x: int(x[1]) * int(x[2]), text_list)))))
file.close()