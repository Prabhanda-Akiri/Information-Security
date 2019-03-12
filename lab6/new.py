import sys
import fractions

def main():

	plain_text=input('\nEnter the Message:\n')
	P=int(input('\nP:	'))
	Q=int(input('Q:	'))
	N=P*Q
	#phi_N=calculate_phi_N(N)
	phi_N=(P-1)*(Q-1)

	e,d=get_multiplicative_inverse(phi_N,'e')
	r,r_inv=get_multiplicative_inverse(N,'r')

	print('N=',N)
	plain_text_blocks=block_formation(plain_text,N)
	print('\nOriginal Message',plain_text_blocks)
	wrapped_blocks=wrap_messages(plain_text_blocks,r,e,N)
	print('\nMessage wrapped by attacker:\n',wrapped_blocks)
	signed_blocks=sign_messages(wrapped_blocks,d,N)
	print('\nSigned message from Bob:\n',signed_blocks)
	signatures=get_signatures(signed_blocks,r_inv,N)
	print('\nSignature of Bob:\n',signatures)

	recovered_message=recover_message(signatures,e,N)
	print('\nMessage derived from Bob\'s Signature:\n',recovered_message)
	#calculated_signatures=calculate_signatures(plain_text_blocks,d,N)
	#print('calculated_signatures:\n',calculated_signatures)
	display_results(plain_text_blocks,recovered_message,plain_text)

def display_results(original_message,recovered_message,plain_text):
	
	recovered_text=''.join(hex(e)[2:] for e in recovered_message)
	#recovered_text=hex(int(recovered_text))[2:]
	#print(recovered_text)
	recovered_text=bytearray.fromhex(recovered_text).decode()
	print('\n\nOriginal Message:\n',plain_text)
	print('\nMessage derived from Bob\'s Signature:\n',recovered_text)

	if original_message==recovered_message:
		print('\n\nOriginal message and Message derived from Bob\'s Signature are matching..!\nBlinding attack is Successful\n')

def recover_message(signatures,e,N):
	calculated_signatures=[]
	for block in signatures:
		calculated_signatures.append(get_pow_mod(block,e,N))

	return calculated_signatures

def get_multiplicative_inverse(N,s):
	c=0
	while True:
		c+=1
		print(s,end=':	')
		e=int(input())	
		d=calculate_inv_modulo(e,N)
		if c<3:
			if d==None:
				print('inverse modulo can\'t be calculated for given',s,', enter another value')
				continue
			else:
				break
		else:
			sys.exit()
	return e,d

def calculate_phi_N(n):
	count=0        
	for i in range(1, n + 1):
		if fractions.gcd(n, i) == 1:
			count += 1
	return count

def calculate_inv_modulo(a,N):
	if fractions.gcd(N,a)!=1:
		return 
	q=[]
	r1=N
	r2=a
	r=None
	count=0
	while r2!=0:
		q.append(r1//r2)
		r=r1%r2
		r1=r2
		r2=r 
	t1=0
	t2=1
	t=None
	for q_i in q:
		t=t1-(q_i*t2)
		t1=t2
		t2=t 
	if t1<0:
		return t1+N
	return t1

def wrap_messages(plain_text_blocks,r,e,N):

	wrapped_blocks=[]
	for block in plain_text_blocks:
		t1=block % N
		t2=get_pow_mod(r,e,N)
		temp=(t1*t2) % N   #(A * B) mod C = (A mod C * B mod C) mod C
		wrapped_blocks.append(temp)
		#print(t1,t2,temp)
	return wrapped_blocks

def sign_messages(wrapped_blocks,d,N):
	signed_blocks=[]

	for block in wrapped_blocks:
		temp=get_pow_mod(block,d,N)
		signed_blocks.append(temp)

	return signed_blocks

def get_signatures(signed_blocks,r_inv,N):
	signatures=[]
	for block in signed_blocks:
		temp=(block*(r_inv%N)) % N
		signatures.append(temp)
	return signatures

def block_formation(plain_text,N):
	blocks=[]
	plain_text_hex=[]
	buff=''

	for character in plain_text:
		plain_text_hex.append(hex(ord(character))[2:])
	#print(plain_text_hex)

	for iter_i in plain_text_hex:
		#print(int(buff,16),int(iter_i,16))
		#print(int(buff+iter_i,16))
		if int(buff+iter_i,16) > N:
			blocks.append(int(buff,16))
			buff=iter_i
		else:
			buff+=iter_i
	blocks.append(int(buff,16))
	#print(plain_text_hex)
	#blocks=[89]
	return blocks

def get_pow_mod(a,p,N):
	
	#get binary split of power
	bin_p=bin(p)[2:]
	bin_nums=[]
	c=0
	for i in range(len(bin_p)-1,-1,-1):
		if bin_p[i]=='1':
			bin_nums.append(c)
			k=c+1
		c+=1
	vals=[]
	for i in range(k):
		if len(vals)==0:
			vals.append(a)
		else:
			temp=pow(vals[-1],2)%N
			vals.append(temp)
	p=1
	for i in bin_nums:
		p*=vals[i]
	return p%N

def convert_to_binary(x):

	'''if x==32:
		return [0,0,0,0,0,0,0,0]'''

	val=bin(x)[2:]
	remaining=8-len(val)

	for i in range(remaining):
		val='0'+val
	
	# for i in range(8):
	# 	val[i]=int(val[i])
	#print(val)
	return val

def calculate_signatures(plain_text_blocks,d,N):
	calculated_signatures=[]
	for block in plain_text_blocks:
		calculated_signatures.append(get_pow_mod(block,d,N))

	return calculated_signatures

if __name__ == '__main__':
	main()
