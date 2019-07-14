
data = []

count = 0
word = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if (count % 1000) == 0:
			print(len(data))

print('File read complete.', len(data), 'records in total')


sum_len = 0

for d in data:
	sum_len += len(d)
	print(sum_len)

print('Average lenght of message is ', sum_len / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('Found', len(new), 'message less then 100 words')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)

bad = ['bad' in d for d in data]

print(bad)


print('There are ', len(good),'messages contains the word "good"')
print(good[0])







wc = {} # word count

for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print (len(wc))
print (wc['Allen'])


while True:
	usr_input = input('Enter the work you want to search: ')
	if usr_input == 'q':
		break
	if 	usr_input in wc:
		print (usr_input, 'The occurenace is: ', wc[usr_input])
	else:
		print('The word not exist....')
print('Thank you for using our searching!')


