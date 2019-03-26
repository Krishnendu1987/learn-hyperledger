#!/usr/bin/python3

def check_passport_length(passport, length):
	stringlenght=len(passport)

	if stringlenght >= length:
 	 return 0
	else:
 	 return 1 


print(check_passport_length("PS1234",7))
print(check_passport_length("PS1234",5))

