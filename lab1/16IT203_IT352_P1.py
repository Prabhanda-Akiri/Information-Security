
def main():

	plain_text=input('\nEnter string for encryption:  ')
	Blocks=block_formation(plain_text)

	ascii_text,binary_text=binary_conversion(Blocks)

	initial_permuted_blocks=initial_permutation(binary_text)
	#print(initial_permuted_blocks,Blocks)

	final_permuted_blocks=final_permutation(initial_permuted_blocks)
	#print(final_permuted_blocks)

	display_results(Blocks,ascii_text,binary_text,initial_permuted_blocks,final_permuted_blocks)

	print('\nBinary plain text and Ciphered binary text are same?',compare_texts(binary_text,final_permuted_blocks),'\n')


def display_results(Blocks,ascii_text,binary_text,initial,final):

	num_blocks=len(Blocks)

	for iter_i in range(num_blocks):

		blk=''.join(Blocks[iter_i])
		print('\nBlock ',iter_i+1,':	',blk)
		asc=ascii_text[iter_i]
		print('ASCII values:	',asc)
		print('\nChar BinaryPlainText InitialPermutation FinalPermutation')
		k=0
		for j in range(0,8):
			ptxt=''.join(binary_text[iter_i][j*8:j*8+8])
			iptxt=''.join(initial[iter_i][j*8:j*8+8])
			fptxt=''.join(final[iter_i][j*8:j*8+8])
			print(Blocks[iter_i][k],'  | ',ptxt,'   |  ',iptxt,' 	|	',fptxt)
			k+=1

def compare_texts(initial,final):

	n=len(initial)
	txt=[]

	for i in range(n):
		for j in range(8):
			k=j*8
			asc=int(''.join(final[i][k:k+8]),2)
			#print(asc)
			txt=txt+[chr(asc)]

	print('\nString obtained from final permuted blocks is:	',''.join(txt))
	
	for i in range(n):
		for j in range(64):
			if initial[i][j]!=final[i][j]:
				return False

	return True

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

def final_permutation(initial_permuted_blocks):
	Final_permutation_table=[40,  8, 48,16,56,24,64,32,
							39,7, 47,15,55,23,63,31,
							38,6, 46,14,54,22,62,30,
							37,5, 45,13,53,21,61,29,
							36,4, 44,12,52,20,60,28,
							35,3, 43,11,51,19,59,27,
							34,2, 42,10,50,18,58,26,
							33,1, 41,9, 49,17,57,25
							]
	num_blocks=len(initial_permuted_blocks)
	final_permuted_blocks=[]

	for i in range(num_blocks):
		final_permuted_blocks.append(list(map(lambda x: initial_permuted_blocks[i][x-1], Final_permutation_table)))

	return final_permuted_blocks

def block_formation(plain_text):
	Blocks=[]
	plain_text=plain_text.replace(" ","")
	length=len(plain_text)
	#print(length,plain_text)

	#blocks are created
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

	return ascii_text,binary_text


def convert_to_binary(x):

	val=bin(x)[2:]
	remaining=8-len(val)

	for i in range(remaining):
		val="0"+val
	return val

main()