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
	
		
	return plain_text