def setting(data):
	return data[1]


n = int(input())
array = []
for _ in range(n):
	lst = []
	lst.append(input())
	lst.append(int(input()))
	array.append(lst)
print(sorted(array[0],key = setting))