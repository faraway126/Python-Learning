import random
digits:'0123456789'
lowercase_letters:'abcdefghijklmnopqrstuvwxyz'
uppercase_letters:'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation:'!#$%&*+-=?@^_'
chars=''
def user_input():
	pass_count=0
	punct_status=True
	dif_symbols_flag=True
	while True:
		print('Сколько паролей тебе нужно?')
		pass_count=int(input())
		print('Использовать ли символы пунктуации?')
		punct_status=input()
		if punct_status!=True or punct_status!=False:
			print('Введите пожалуйста True или False')
		print('Исключать ли неоднозначные симаолы?(il1Lo0O)')
		dif_symbols_flag=input()
		if dif_symbols_flag!=True or dif_symbols_flag!=False:
			print('Введите пожалуйста True или False')
		break
	return pass_count, punct_status, dif_symbols_flag
def generate_password(password_lenght, chars,):
	for


	pass


def main():
	print('Сколько паролей тебе нужно?')
	pass_count=int(input())
	print('Использовать ли символы пунктуации?')
	punct_status=input()
	if punct_status!=True or punct_status!=False:
		print('Введите пожалуйста True или False')