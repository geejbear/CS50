import re

#amex
fifteen_digits_long = 15
#mc and visa
sixteen_digits_long = 16
#visa
thirteen_digits_long = 13

def main():
	card_num = []
	card_num = input('Enter card number:')
	##print(digit_sum(card_num))

	amex_pattern = re.compile(r"^(37|34\d{13})")
	mc_pattern = re.compile(r"^(51|52|53|54|55\d{14})")
	visa_pattern = re.compile(r"^(4\d{12|15})")

	if (amex_pattern.match(card_num) 
		and len(card_num) == fifteen_digits_long):
		##and digit_sum(card_num) % 10 == 0): 
			print('AMEX')
	elif (mc_pattern.match(card_num) 
		and len(card_num) == sixteen_digits_long):
			if digit_sum(card_num) % 10 == 0: 
				print('MASTERCARD')
	elif (visa_pattern.match(card_num) 
		and len(card_num) == sixteen_digits_long): 
			if digit_sum(card_num) % 10 == 0: 
				print('VISA')
	elif (visa_pattern.match(card_num) 
		and len(card_num) == thirteen_digits_long):
			if digit_sum(card_num) % 10 == 0: 
				print('VISA')
	else:
		print('INVALID')

def digit_sum(num):
	sum_odds = 0
	sum_pairs = 0
	for i in range(0, len(num), 2):
		n = int(num[i])
		n *= 2
		if n > 9:
			n = int_to_str_to_int(n)
		##print(f"1.{n}")
		sum_odds += n 
	for j in range(1, len(num), 2):
		n = int(num[j])
		sum_pairs += n
		##print(f"\t2.{n}")
	return sum_odds + sum_pairs

def int_to_str_to_int(n):
	tmp = str(n)
	total = 0
	for i in range(len(tmp)):
		total += int(tmp[i])
	return total
	
main()

