def main():

	cipher_text=int(input('\nEnter the cipher text:\n'))
	N=int(input('\nN = '))
	e=int(input('e= '))
	'''cipher_text=int(input('\nEnter the cipher text:\n'))
	N=int(input())
	e=int(input())

	print('\nCipher text:	',cipher_text)
	print('\nN=',N)
	print('\ne=',e)'''
	#blocks=generate_blocks(cipher_text,N)
	plain_text=apply_cyclic_attack(cipher_text,N,e)
	print('Plain Text Obtained:	',plain_text)

	verify_plain_text(plain_text,cipher_text,N,e)


def verify_plain_text(plain_text,cipher_text,N,e):

	new_cipher_text=(plain_text**e) % N
	print('\nCipher text computed from plain text Obtained:	',new_cipher_text)
	if new_cipher_text==cipher_text:
		print('\nBoth cipher texts are same. Plain text obatined is correct.!')
		return
	else:
		print('\nBoth cipher texts are not same. Plain text obatined is not correct.!')

def apply_cyclic_attack(cipher_text,N,e):

	plain_text=None
	curr=cipher_text
	derived_ciphers=[curr]
	status=False
	
	c=0
	while status==False:
		c+=1
		c_dash=(curr**e) % N
		#print(c_dash)
		derived_ciphers.append(c_dash)
		if c_dash==cipher_text:
			plain_text=derived_ciphers[-2]
			status=True
		curr=c_dash
	print('\n')
	'''for i in range(1,len(derived_ciphers)):
		print('Cycle',i,':	',derived_ciphers[i])'''
		
	return plain_text

def generate_blocks(cipher_text,N):

	cipher_ascii=[]
	for i in cipher_text:
		cipher_ascii.append(ord(i))

	blocks=[]
	'''curr=[]
	for i in cipher_ascii:
		curr.append(i)
		if int(''.join(curr))>N:
			blocks.append(''.join(curr))'''
	return cipher_ascii

if __name__ == '__main__':
	main()
