eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def user_input():
	direction = input('Что мы должны сделать: шифровать или дешифровать? \n')
	while direction != 'шифровать' and direction != 'дешифровать':
		direction = input('Что-то не то ты ввёл. Напиши "шифровать" либо "дешифровать". \n')
	language = input('Какой нужен язык: русский или английский? \n')
	while language != 'русский' and language != 'английский':
		language = input('Что-то не то ты ввёл. Напиши "русский" либо "английский". \n')
	step = input('На сколько символовов мы сдвигаем буквы по алфавиту? Ответ напиши числом. \n')
	while step.isdigit() != True:
		step = input('Что-то не то ты ввёл. Напиши число. \n')
	text = input('Какой текст нужно использовать сейчас? \n')
	while text.isspace() == True:
		text = input('Что-то не то ты ввёл. Введи текст. \n')
	return direction, language, step, text

def rus_lower_crypt(text, key, power):
	result=''
	for i in range(len(rus_lower_alphabet)):
		if text==rus_lower_alphabet[i]:
			result=result+rus_lower_alphabet[((i+key)%32)]
			break
	return result

def rus_upper_crypt(text, key, power):
	result=''
	for i in range(len(rus_upper_alphabet)):
		if text==rus_upper_alphabet[i]:
			result=result+rus_upper_alphabet[((i+key)%32)]
			break 
	return result

def eng_lower_crypt(text, key, power):
	result=''
	for i in range(len(eng_lower_alphabet)):
		if text==eng_lower_alphabet[i]:
			result=result+eng_lower_alphabet[((i+key)%26)]
			break
	return result

def eng_upper_crypt(text, key, power):
	result=''
	for i in range(len(eng_upper_alphabet)):
		if text==eng_upper_alphabet[i]:
			result=result+eng_upper_alphabet[((i+key)%26)]
			break 
	return result


def crypt(text, key, language, power):
	result=''
#	print(text)
	while language=='русский':
		for i in range(len(text)):
			if text[i].isalpha():
				if text[i]==text[i].lower():
					result=result + rus_lower_crypt(text[i], key, power)

				elif text[i]==text[i].upper():
					result= result + rus_upper_crypt(text[i], key, power)
			else:
				result=result + text[i]
		break
	while language=='английский':
		for i in range(len(text)):
			if text[i].isalpha():
				if text[i]==text[i].lower():
					result=result + eng_lower_crypt(text[i], key, power)

				elif text[i]==text[i].upper():
					result= result + eng_upper_crypt(text[i], key, power)
			else:
				result=result + text[i]
		break
	return result
		
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



def main():
	print('Hello. Welcome to crypt/encrypt Caesar programm!')
	direction, language, step, text=user_input()
	alpabet_power=0
	if language=='русский' and direction=='шифровать':
		alpabet_power=32
		result=crypt(text, int(step), language, alpabet_power)
	elif language=='английский' and direction=='шифровать':
		alpabet_power=26
		result=crypt(text, int(step), language, alpabet_power)

	if language=='русский' and direction=='дешифровать':
		alpabet_power=32
		result=encrypt(text, int(step), language, alpabet_power)
	elif language=='английский' and direction=='дешифровать':
		alpabet_power=26
		result=encrypt(text, int(step), language, alpabet_power)
	print(result)
main()