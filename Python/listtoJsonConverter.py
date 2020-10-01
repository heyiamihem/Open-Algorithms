s = "{\n"
while(True):
	print("press Quit to exit")	
	try:
		item = input()
	except:
		break
	if(item=="Quit"):
		break
	s+="\t'"+item+"',\n"
s+="\n}"
print(s)
