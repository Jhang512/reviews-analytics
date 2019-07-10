
data = []

count = 0
word = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if (count % 1000) == 0:
			print(len(data))

sum_len = 0

for d in data:
	sum_len += len(d)
	print(sum_len)


print('File read complete.', len(data), 'records in total')
print('Average lenght of message is ', sum_len / len(data))