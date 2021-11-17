eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"








def encrypt(text, key, language, power):
	result=''
	while language== 'английский':
		for i in range(len(text)):
			if text[i].isalpha():
				if text[i]==text[i].lower():
					result=result + eng_lower_encrypt(text[i], key, power)
				elif text[i]==text[i].upper():
					result=result + eng_upper_encrypt(text[i], key, power)
			else:
				result=result + text[i]
		break
	while language== 'русский':
		for i in range(len(text)):
			if text[i].isalpha():
				if text[i]==text[i].lower():
					result=result + rus_lower_encrypt(text[i], key, power)
				elif text[i]==text[i].upper():
					result=result + rus_upper_encrypt(text[i], key, power)
			else:
				result=result + text[i]
		break
	return result

def rus_lower_encrypt(text, key, power):
	result=''
	for i in range(len(rus_lower_alphabet)):
		if text==rus_lower_alphabet[i]:
			result=result+rus_lower_alphabet[((i-key)%32)]
			break
	return result

def rus_upper_encrypt(text, key, power):
	result=''
	for i in range(len(rus_upper_alphabet)):
		if text==rus_upper_alphabet[i]:
			result=result+rus_upper_alphabet[((i-key)%32)]
			break 
	return result

def eng_lower_encrypt(text, key, power):
	result=''
	for i in range(len(eng_lower_alphabet)):
		if text==eng_lower_alphabet[i]:
			result=result+eng_lower_alphabet[((i-key)%26)]
			break
	return result

def eng_upper_encrypt(text, key, power):
	result=''
	for i in range(len(eng_upper_alphabet)):
		if text==eng_upper_alphabet[i]:
			result=result+eng_upper_alphabet[((i-key)%26)]
			break 
	return result
for i in range(25):
	print(encrypt('Hawnj pk swhg xabkna ukq nqj.', i, 'английский', 26), i)