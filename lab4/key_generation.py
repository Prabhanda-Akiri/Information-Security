def generate_key():

	key=get_key()  #8 char text key is obtained
	#print('\nThe key is:	',key,'\n')

	ascii_key,binary_key=get_binary_key(key) #64 bit binary key is obtained

	return generate_round_keys(binary_key)
	
def generate_round_keys(binary_key):

	permuted_key=apply_permutation_choice_1(binary_key)
	#print(permuted_key,len(permuted_key))

	c_key=permuted_key[:28]
	d_key=permuted_key[28:]

	#print(permuted_key,c_key,d_key)

	round_keys=[None for i in range(16)]

	for i in range(16):

		c_key=apply_left_shift(c_key,i)
		d_key=apply_left_shift(d_key,i)
		round_key=apply_permutation_choice_2(c_key,d_key)
		round_keys[i]=round_key

		'''chunks = [round_key[x:x+8] for x in range(0, len(round_key), 8)]
		#print('Round key of',i+1,end='		')

		for j in range(6):
			chunks[j]=''.join(chunks[j])
			#print(chunks[j],end=' ')

		#print('	48 bits')'''

		for j in range(len(round_keys[i])):
			round_keys[i][j]=int(round_keys[i][j])
		#print('')

	return round_keys

def apply_left_shift(key,i):

	if i+1==1 or i+1==2 or i+1==9 or i+1==16:
		return shift(key,1)
	else:
		return shift(key,2)


def apply_permutation_choice_2(c_key,d_key):

	key=c_key+d_key

	permutation_choice2_table=[14,17,11,24,1, 5,
								3, 28,15,6, 21,10,
								23,19,12,4, 26,8,
								16,7, 27,20,13,2,
								41,52,31,37,47,55,
								30,40,51,45,33,48,
								44,49,39,56,34,53,
								46,42,50,36,29,32]

	permutation_choice2_table+=[1,1,1,1,1,1,1,1]

	round_key=list(map(lambda x:key[x-1], permutation_choice2_table))
	round_key=round_key[:48]

	return round_key

def apply_permutation_choice_1(binary_key):

	permutation_choice1_table=[57,49,41,33,25,17,9,
								1,58,50,42,34,26,18,
								10,2,59,51,43,35,27,
								19,11,3,60,52,44,36,
								63,55,47,39,31,23,15,
								7,62,54,46,38,30,22,
								14,6,61,53,45,37,29,
								21,13,5,28,20,12,4]

	permutation_choice1_table+=[1,1,1,1,1,1,1,1]
	#print(len(permutation_choice1_table),len(binary_key))

	permuted_key=list(map(lambda x: binary_key[x-1], permutation_choice1_table))
	permuted_key=permuted_key[:56]
	return permuted_key

def get_binary_key(key):

	ascii_key=[None for i in range(8)]
	binary_key=[]

	for i in range(8):
		ascii_key[i]=ord(key[i])
		binary_key=binary_key+convert_to_binary(ascii_key[i])
		#print(ascii_key[i],bin(ascii_key[i])[2:])

	#print(binary_key,len(binary_key))
	return ascii_key,binary_key

def convert_to_binary(x):

	val=bin(x)[2:]
	remaining=8-len(val)

	for i in range(remaining):
		val="0"+val
	return list(val)

def get_key():

	text=input('\nEnter a text for the key:\n')
	text=text.replace(" ","")

	while(len(text)!=8):
		text=input('\nEnter a valid key of 8 chars:     ')
		text=text.replace(" ","")

	'''key_opt=input('\nChoose the option for key\n1. first 8 chars\n2. last 8 chars\n')

	if key_opt=='1':
		key=text[:8]
	else:
		key=text[len(text)-8:]'''

	return text

def shift(l, n):
	return l[n:] + l[:n]
