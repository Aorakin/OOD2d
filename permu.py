def toString(List):
	return ''.join(List)

def permute(string, l, r):
	if l == r:
		print(toString(string))
	else:
		for i in range(l, r):
			string[l], string[i] = string[i], string[l]
			permute(string, l+1, r)
			string[l], string[i] = string[i], string[l] # backtrack

string = "TnT"
n = len(string)
# permute(list(string),0,n)

answer = []

def permute2(input_string,data,index,size):
	if len(data) == size:
		return [data]
	elif index >= len(input_string):
		return []
	else:
		string1 = permute2(input_string[:index] + input_string[index+1:],data + input_string[index],0,size)
		string2 = permute2(input_string,data,index+1,size)
	return string1 + string2

answer = permute2(string,"",0,3)
answer.sort()
print(answer)