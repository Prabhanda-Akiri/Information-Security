def main():

	cipher_text=input('\nEnter the cipher text:\n')
	N=int(input('\nN = '))
	e=int(input('e= '))

	blocks=generate_blocks(cipher_text,N)
	plain_text=apply_cyclic_attack(blocks,N,e)
	print(plain_text)
def apply_cyclic_attack(blocks,N,e):

	plain_text=[]
	for block in blocks:
		curr=block
		derived_ciphers=[block]
		status=False
		print('\n',block)
		c=0
		while status==False:
			c+=1
			c_dash=(curr**e) % N
			#print(c_dash)
			derived_ciphers.append(c_dash)
			if c_dash==block:
				plain_text.append(derived_ciphers[-2])
				status=True
			curr=c_dash
			if c>50:
				break

	for i in range(len(plain_text)):
		plain_text[i]=chr(plain_text[i])
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
