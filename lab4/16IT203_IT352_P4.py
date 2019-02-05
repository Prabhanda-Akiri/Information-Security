import csv
import key_generation as key_file

def main():

	round_keys=key_file.generate_key()
	input_blocks=block_formation()

	plain_text_binary=binary_conversion(input_blocks)
	print('\nplain text:\n')
	display_text(plain_text_binary)

	ciphered_text=apply_DES(plain_text_binary,round_keys)
	print('\nciphered text:\n')
	display_text(ciphered_text)

	store_result(ciphered_text,1)

def store_result(text,k):
	if k==0:
		file=open('Output_Program_4.txt',"w")
	else:
		file=open('Output_Program_4.txt',"a")
	file.write('\n')
	for i in range(len(text)):
		for j in text[i]:
			file.write(str(j))
		file.write('\n')

def display_text(text):
	for i in text:
		print('Block',text.index(i)+1,end=':	')
		chunks = [i[x:x+8] for x in range(0, len(i), 8)]
		for j in range(8):
			chunks[j]=''.join(str(e) for e in chunks[j])
			print(chunks[j],end=' ')
		print('')

def apply_DES(plain_text_binary,round_keys):

	plain_text_binary=initial_permutation(plain_text_binary)
	#print(len(initial_permuted_blocks[0]))

	round_output=[]

	for iter_blocks in range(len(plain_text_binary)):
		print('\nRound outputs of Block:	',iter_blocks+1)
		plain_text=plain_text_binary[iter_blocks]
		left_plain_text=plain_text[:32]
		right_plain_text=plain_text[32:]
		strg=[]
		for iter_i in range(16):
			#print(right_plain_text)
			temp_right_plain_text=right_plain_text

			right_plain_text=apply_expansion_table(right_plain_text)
			right_plain_text=XOR_operation(right_plain_text,round_keys[iter_i])
			right_plain_text=apply_Sbox_table(right_plain_text)
			right_plain_text=apply_permutation_table(right_plain_text)			

			if iter_i==15:
				left_plain_text=XOR_operation(right_plain_text,left_plain_text)
				right_plain_text=temp_right_plain_text
				strg+=[''.join(str(e) for e in left_plain_text+right_plain_text)]
				display_intermediate_text(left_plain_text+right_plain_text,iter_i)
				continue
				
			right_plain_text=XOR_operation(right_plain_text,left_plain_text)
			left_plain_text=temp_right_plain_text

			strg+=[''.join(str(e) for e in left_plain_text+right_plain_text)]
			display_intermediate_text(left_plain_text+right_plain_text,iter_i)

		round_output.append(left_plain_text+right_plain_text)
		if iter_blocks==0:
			store_result(strg,0)
		else:
			store_result(strg,1)
	ciphered_text_binary=final_permutation(round_output)

	return ciphered_text_binary

def display_intermediate_text(text,i):
	print('Round',i+1,end=':	')
	chunks = [text[x:x+8] for x in range(0, len(text), 8)]
	for j in range(8):
		chunks[j]=''.join(str(e) for e in chunks[j])
		print(chunks[j],end=' ')
	print('')

def final_permutation(blocks):
	Final_permutation_table=[40,  8, 48,16,56,24,64,32,
							39,7, 47,15,55,23,63,31,
							38,6, 46,14,54,22,62,30,
							37,5, 45,13,53,21,61,29,
							36,4, 44,12,52,20,60,28,
							35,3, 43,11,51,19,59,27,
							34,2, 42,10,50,18,58,26,
							33,1, 41,9, 49,17,57,25
							]
	num_blocks=len(blocks)
	final_permuted_blocks=[]

	for i in range(num_blocks):
		final_permuted_blocks.append(list(map(lambda x:blocks[i][x-1], Final_permutation_table)))

	return final_permuted_blocks
def apply_permutation_table(plain_text):

	permutation_table=[16, 7, 20,21,29,12,28,17,
						1, 15,23,26,5, 18,31,10,
						2, 8, 24,14,32,27,3, 9,
						19,13,30,6, 22,11,4, 25]

	return list(map(lambda x: plain_text[x-1], permutation_table))

def apply_Sbox_table(plain_text):

	Sboxes=[[[14,4, 13,1, 2, 15,11,8, 3, 10,6, 12,5, 9, 0, 7],
			[0, 15,7, 4, 14,2, 13,1, 10,6, 12,11,9, 5, 3, 8],
			[4, 1, 14,8, 13,6, 2, 11,15,12,9, 7, 3, 10,5, 0],
			[15,12,8, 2, 4, 9, 1, 7, 5, 11,3, 14,10,0, 6, 13]],

			[[15,1, 8, 14,6, 11,3, 4, 9, 7, 2, 13,12,0, 5, 10],
			[3, 13,4, 7, 15,2, 8, 14,12,0, 1, 10,6, 9, 11,5],
			[0, 14,7, 11,10,4, 13,1, 5, 8, 12,6, 9, 3, 2, 15],
			[13,8, 10,1, 3, 15,4, 2, 11,6, 7, 12,0, 5, 14,9]],

			[[10,0, 9, 14,6, 3, 15,5, 1, 13,12,7, 11,4, 2, 8],
			[13,7, 0, 9, 3, 4, 6, 10,2, 8, 5, 14,12,11,15,1],
			[13,6, 4, 9, 8, 15,3, 0, 11,1, 2, 12,5, 10,14,7],
			[1, 10,13,0, 6, 9, 8, 7, 4, 15,14,3, 11,5, 2, 12]],

			[[7,13,14,3, 0, 6, 9, 10,1, 2, 8, 5, 11,12,4, 15],
			[13,8, 11,5, 6, 15,0, 3, 4, 7, 2, 12,1, 10,14,9],
			[10,6, 9, 0, 12,11,7, 13,15,1, 3, 14,5, 2, 8, 4],
			[3, 15,0, 6, 10,1, 13,8, 9, 4, 5, 11,12,7, 2, 14]],

			[[2,12,4, 1, 7, 10,11,6, 8, 5, 3, 15,13,0, 14,9],
			[14,11,2, 12,4, 7, 13,1, 5, 0, 15,10,3, 9, 8, 6],
			[4, 2, 1, 11,10,13,7, 8, 15,9, 12,5, 6, 3, 0, 14],
			[11,8, 12,7, 1, 14,2, 13,6, 15,0, 9, 10,4, 5, 3]],

			[[12,1, 10,15,9, 2, 6, 8, 0, 13,3, 4, 14,7, 5, 11],
			[10,15,4, 2, 7, 12,9, 5, 6, 1, 13,14,0, 11,3, 8],
			[9, 14,15,5, 2, 8, 12,3, 7, 0, 4, 10,1, 13,11,6],
			[4, 3, 2, 12,9, 5, 15,10,11,14,1, 7, 6, 0, 8, 13]],

			[[4,11,2, 14,15,0, 8, 13,3, 12,9, 7, 5, 10,6, 1],
			[13,0, 11,7, 4, 9, 1, 10,14,3, 5, 12,2, 15,8, 6],
			[1, 4, 11,13,12,3, 7, 14,10,15,6, 8, 0, 5, 9, 2],
			[6, 11,13,8, 1, 4, 10,7, 9, 5, 0, 15,14,2, 3, 12]],

			[[13,2, 8, 4, 6, 15,11,1, 10,9, 3, 14,5, 0, 12,7],
			[1, 15,13,8, 10,3, 7, 4, 12,5, 6, 11,0, 14,9, 2],
			[7, 11,4, 1, 9, 12,14,2, 0, 6, 10,13,15,3, 5, 8],
			[2, 1, 14,7, 4, 10,8, 13,15,12,9, 0, 3, 5, 6, 11]]]

	new_text=[]

	for i in range(8):
		chunk=plain_text[i*6:(i+1)*6]
		
		row=int(''.join(str(e) for e in ([chunk[0]]+[chunk[5]]) ),2)
		col=int(''.join(str(e) for e in chunk[1:5]),2)

		val=Sboxes[i][row][col]
		#print(val)
		val=bin(val)[2:]
		remaining=4-len(val)
		
		for k in range(remaining):
			val="0"+val
		val=list(val)
		
		for k in range(4):
			val[k]=int(val[k])

		new_text+=val

	return new_text

def XOR_operation(list_A,list_B):
	#pass
	result=[list_A[i]^list_B[i] for i in range(len(list_B))]
	return result

def apply_expansion_table(plain_text):
	expansion_table=[32,1,2,3,4,5,
					4,5,6,7,8,9,
					8,9,10,11,12,13,
					12,13,14,15,16,17,
					16,17,18,19,20,21,
					20,21,22,23,24,25,
					24,25,26,27,28,29,
					28,29,30,31,32,1]

	expanded_text=list(map(lambda x: plain_text[x-1], expansion_table))
	#print(plain_text,expanded_text,len(expanded_text))
	return expanded_text

def initial_permutation(binary_text):

	Initial_permutation_table=[58,50, 42,34,26,18,10,2,
								60,52,44,36,28,20,12,4,
								62,54,46,38,30,22,14,6,
								64,56,48,40,32,24,16,8,
								57,49,41,33,25,17,9, 1,
								59,51,43,35,27,19,11,3,
								61,53,45,37,29,21,13,5,
								63,55,47,39,31,23,15,7
							   ]
	num_blocks=len(binary_text)
	initial_permuted_blocks=[]

	for i in range(num_blocks):
		initial_permuted_blocks.append(list(map(lambda x: binary_text[i][x-1], Initial_permutation_table)))

	return initial_permuted_blocks

def binary_conversion(Blocks):

	num_blocks=len(Blocks)

	ascii_text=[[0 for i in range(8)] for j in range(num_blocks)]
	binary_text=[[] for j in range(num_blocks) ]

	for i in range(num_blocks):
		l=[]
		for j in range(8):
			ascii_text[i][j]=ord(Blocks[i][j])
			l+=convert_to_binary(ascii_text[i][j])
		binary_text[i]=l

	return binary_text

def convert_to_binary(x):

	if x==32:
		return [0,0,0,0,0,0,0,0]

	val=bin(x)[2:]
	remaining=8-len(val)
	val=list(val)

	for i in range(remaining):
		val=[0]+val
	val=list(val)
	
	for i in range(8):
		val[i]=int(val[i])
	#print(val)
	return val

def block_formation():

	'''f=open('input.txt',"r")
	#print(f.read())
	plain_text=f.read()'''
	plain_text=input('\nEnter plain text of Min-8chars and Max-40chars:\n')
	plain_text=plain_text.replace(" ","")

	while(len(plain_text)<8 or len(plain_text)>40):
		plain_text=input('\nEnter plain text of Min-8chars and Max-40chars:\n')
		text=text.replace(" ","")

	plain_text=plain_text.replace("\n","")
	print('\nText:\n',plain_text)

	Blocks=[]
	length=len(plain_text)
	
	for i in range(0,length,8):
		strg=[]
		j=0
		while j<8:
			if i+j<length:
				strg.append(plain_text[i+j])
				j+=1
			else:
				strg.append(" ")
				j+=1
		Blocks.append(strg)

	return Blocks

def get_round_keys():

	file_no=int(input('Choose the key:\n1. ROSE FLOWER\n2. Date is 170119\n3. Morning Tea\n4.Surprise test\n5.Paper Collection\n'))

	files_list=['roundkeys1_1.txt','roundkeys2_1.txt','roundkeys3_1.txt','roundkeys4_1.txt','roundkeys5_1.txt']

	file_name=files_list[file_no-1]

	round_keys=[]

	f = open(file_name, "r")
	for x in f:
		k=x.split()
		for i in range(len(k)):
			k[i]=int(k[i])
		round_keys.append(k)

	#print(round_keys)
	return round_keys

if __name__ == '__main__':
	main()