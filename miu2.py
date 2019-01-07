#miu2.py

strThrm = 'MI'
lstThrm = list(strThrm)
count = 1
displayList = []

def assess(strThrm, lstThrm):
	if 'I' in strThrm[-1]: # Rule1
		print('\nEnter 1 to add U to the end of', strThrm)
	if 'I' or 'U' in strThrm[1]: # Rule2
		print('Enter 2 to add', strThrm[1:], 'to the end of', strThrm)
	if 'III' in strThrm: # Rule3
		print('Enter 3 to substitute U for some III of', strThrm)
	if 'UU' in strThrm: # Rule4
		print('Enter 4 to remove a U from an instance of two consecutive Us')

def Rule1(strThrm):
	lstThrm = list(strThrm)
	lstThrm.append('U')
	strThrm = ''.join(lstThrm)
	return strThrm

def Rule2(strThrm):
	add = ''.join(lstThrm[1:])
	lstThrm.append(add)
	strThrm = ''.join(lstThrm)
	return strThrm

def Rule3(strThrm):
	IIIList = []
	for index, item in enumerate(strThrm):
		a = index
		b = index + 3
		if 'III' in strThrm[a:b]:
			IIIList.append(index)
			print('III at index position', index, 'of', strThrm)
	u = int(input('III --> U at which index position? '))
	v = u + 1
	lstThrm = list(strThrm)
	lstThrm[u] = 'U'
	del lstThrm[v]
	del lstThrm[v]
	strThrm = ''.join(lstThrm)
	return strThrm

def Rule4(strThrm):
	UUList = []
	for index, item in enumerate(strThrm):
		a = index
		b = index + 2
		if 'UU' in strThrm[a:b]:
			UUList.append(index)
			print('UU at index position', index, 'of', strThrm)
	u = int(input('UU --> U at which index position? '))
	v = u + 1
	lstThrm = list(strThrm)
	del lstThrm[v]
	strThrm = ''.join(lstThrm)
	return strThrm

def display(count, str, strThrm):
	tinyList = [count, str, strThrm]
	displayList.append(tinyList)
	print('\n\t Step\t From\t Theorem')
	for eachList in displayList:
		print('\t', eachList[0], '\t', eachList[1], '\t', eachList[2])
	print()

def welcome():
	print('\n*Welcome to the MIU-System*')
	print('\nThere are four Rules:')
	print('\tRule 1: If the theorem ends with I then you can add U')
	print('\tRule 2: Anything after M can be doubled (Mx --> Mxx)')
	print('\tRule 3: Take any occurrence of III and substitute U')
	print('\tRule 4: Any occurrence of UU can be replaced by U\n')
	display(count, 'Axiom', strThrm)

welcome()
assess(strThrm, lstThrm)

while True:
	d = input('\nEnter your desired transformation, or ENTER to end: ')
	if d == '1': 
		strThrm = Rule1(strThrm)
		lstThrm = list(strThrm)	
		count += 1
		display(count, 'Rule1', strThrm)
		assess(strThrm, lstThrm)
	if d == '2':
		strThrm = Rule2(strThrm)
		lstThrm = list(strThrm)	
		count += 1
		display(count, 'Rule2', strThrm)
		assess(strThrm, lstThrm)
	if d == '3':
		strThrm = Rule3(strThrm)
		lstThrm = list(strThrm)
		count += 1
		display(count, 'Rule3', strThrm)
		assess(strThrm, lstThrm)
	if d == '4':
		strThrm = Rule4(strThrm)
		lstThrm = list(strThrm)
		count += 1
		display(count, 'Rule4', strThrm)
		assess(strThrm, lstThrm)
	if d == '': 
		print('Goodbye!\n')
		break