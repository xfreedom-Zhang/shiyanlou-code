num=range(1,101)
for i in num:
	if i%7 != 0 and i%10 != 7 and i//10 != 7:
		print(i)
	else:
		continue

