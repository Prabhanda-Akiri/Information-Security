import sys
import fractions
import math
from tkinter import *

def display_text(txt,txt1):
	lbl = Label(wi, text=str(txt)+str(txt1))
	lbl.pack()

def apply_attack(plain_text,P,Q,e,r,window):

	global wi
	wi=window
	N=P*Q
	#phi_N=calculate_phi_N(N)
	phi_N=(P-1)*(Q-1)

	e,d=get_multiplicative_inverse(phi_N,'e',e)
	r,r_inv=get_multiplicative_inverse(N,'r',r)

	display_text('\n 	N=',N)
	plain_text_blocks=block_formation(plain_text,N)
	#display_text('\nOriginal Message:		(M)',plain_text_blocks)
	wrapped_blocks=wrap_messages(plain_text_blocks,r,e,N)
	#display_text('\nMessage wrapped by attacker:		(M_dash=M*r^e mod N)\n',wrapped_blocks)
	signed_blocks=sign_messages(wrapped_blocks,d,N)
	#display_text('\nSigned message from Bob:		(S=M^d *r mod N)\n',signed_blocks)
	signatures=get_signatures(signed_blocks,r_inv,N)
	#display_text('\nSignature of Bob:		(S_dash=M^d mod N)\n',signatures)

	recovered_message=recover_message(signatures,e,N)
	# display_text('\nMessage derived from Bob\'s Signature:\n',recovered_message)
	calculated_signatures=calculate_signatures(plain_text_blocks,d,N)
	#display_text('\ncalculated_signatures for verification:		(M^d mod N)\n',calculated_signatures)
	display_results(plain_text_blocks,wrapped_blocks,signed_blocks,recovered_message,signatures,calculated_signatures,plain_text)

def display_results(plain_text_blocks,wrapped_blocks,signed_blocks,recovered_message,signatures,calculated_signatures,plain_text):
	
	recovered_text=''.join(hex(e)[2:] for e in recovered_message)
	recovered_text=bytearray.fromhex(recovered_text).decode()


	for i in range(len(plain_text_blocks)):
		display_text('\n------------	BLOCK:',str(i+1)+'------------')
		display_text('Original Message M:			',plain_text_blocks[i])
		#display_text('Message wrapped by attacker(C_dash=C*r^e mod N):		',wrapped_blocks[i])
		#display_text('Signed message from Bob(S=P*r mod N):				',signed_blocks[i])
		display_text('Signature S:			',signatures[i])
		#display_text('Actual plain text (P=C^d mod N):				',calculated_signatures[i])

	# if signatures==calculated_signatures:
	# 	display_text('\n\nActual plain text  and derived plain text are matching..!\nChosen Cipher-text attack is Successful\n')

	# display_text('\nOriginal Message:		(M)\n',plain_text)
	# display_text('\nOriginal Message derived from Bob\'s Signature:		(M= S_dash^e mod N)\n',recovered_text)
	#signature_text=''.join(bytearray.fromhex(hex(e)[2:]).decode() for e in signatures)
	#display_text(signature_text)

	# signature_chars=[]
	# for block in signatures:
	# 	c=str(block)
	# 	ch=''
	# 	if len(c)%2!=0:
	# 		c='0'+c 

	# 	for i in range(0,len(c),2):
	# 		if i+1<len(c):
	# 			ch+=bytes.fromhex(hex(int(c[i]+c[i+1]))[2:]).decode('utf-8')
	# 		else:
	# 			ch+=bytes.fromhex(hex(int(c[i]))[2:]).decode('utf-8')

	# 	signature_chars.append(ch)
	
	# display_text('\nBob\'s Signature:\n',''.join(signature_chars))

	
def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]

def recover_message(signatures,e,N):
	calculated_signatures=[]
	for block in signatures:
		calculated_signatures.append(get_pow_mod(block,e,N))

	return calculated_signatures

def get_multiplicative_inverse(N,s,e):
	c=0
	while True:
		c+=1
		#display_text(s,end=':	')
		d=calculate_inv_modulo(e,N)
		if c<3: 
			if d==None:
				display_text('\nNo private key exists')
				sys.exit()
				continue
			else:
				break
		else:
			sys.exit()
	return e,d

def calculate_phi_N(n):
	count=0        
	for i in range(1, n + 1):
		if math.gcd(n, i) == 1:
			count += 1
	return count

def calculate_inv_modulo(a,N):
	if math.gcd(N,a)!=1:
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
		#display_text(t1,t2,temp)
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
	#display_text(plain_text_hex)

	powers=[8,16,24,32,40,48,56,64]
	block_size=0

	for i in range(len(powers)):
		temp=2**powers[i]
		if temp>N:
			block_size=i 
			break
	
	blocks=[plain_text_hex[i:i + block_size] for i in range(0, len(plain_text_hex), block_size)]
	blocks=[int(''.join(i),16) for i in blocks]

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

	val=bin(x)[2:]
	remaining=8-len(val)

	for i in range(remaining):
		val='0'+val

	return val

def calculate_signatures(plain_text_blocks,d,N):
	calculated_signatures=[]
	for block in plain_text_blocks:
		calculated_signatures.append(get_pow_mod(block,d,N))

	return calculated_signatures