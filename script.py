f = open('iowa-liquor-sample.csv', 'r')
categories = f.readline().split(",")
count = 0
for line in f:
	for word in line.split(","):
		if word.lower() == "single malt scotch":
			count += 1
			break
print count
