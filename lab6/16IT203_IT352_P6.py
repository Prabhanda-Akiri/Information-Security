import sys
import fractions

def main():

	plain_text=input('\nEnter the plain text:\n')
	P=int(input('\nP:	'))
	Q=int(input('\nQ:	'))
	N=P*Q
	#phi_N=calculate_phi_N(N)
	phi_N=(P-1)*(Q-1)

	e,d=get_multiplicative_inverse(phi_N,'e')
	r,r_inv=get_multiplicative_inverse(N,'r')


	plain_text_blocks=block_formation(plain_text,N)
	print('blocks',plain_text_blocks)
	wrapped_blocks=wrap_messages(plain_text_blocks,r,e,N)
	print('message*r_power_e:\n',wrapped_blocks)
	signed_blocks=sign_messages(wrapped_blocks,d,N)
	print('signed_blocks: m_power_d:\n',signed_blocks)
	signatures=get_signatures(signed_blocks,r_inv,N)
	print('signatures:\n',signatures)

	calculated_signatures=calculate_signatures(plain_text_blocks,d,N)
	print('calculated_signatures:\n',calculated_signatures)

def calculate_signatures(plain_text_blocks,d,N):
	calculated_signatures=[]
	for block in plain_text_blocks:
		calculated_signatures.append(get_pow_mod(block,d,N))

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

def wrap_messages(plain_text_blocks,N,e,r):

	wrapped_blocks=[]
	for block in plain_text_blocks:
		t1=block % N
		t2=get_pow_mod(r,e,N)
		temp=(t1*t2) % N   #(A * B) mod C = (A mod C * B mod C) mod C
		wrapped_blocks.append(temp)

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
	print(plain_text_hex)

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

if __name__ == '__main__':
	main()