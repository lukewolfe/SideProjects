#Language: Python 3
#Author: Luke Wolfe
#Date Created: February, 5, 2020
#Last Update: February 5, 2020
#Name: Caesar Cipher
#Description: This program will allow a user to decrypt and encrypt messages using the Caesar cipher which is a shift cipher. 

import re

print('############################################################################')
print('############################################################################')
print('##     ______                              _______       __               ##')
print('##    / ____/___ ____  _________ ______   / ____(_)___  / /_  ___  _____  ##')
print('##   / /   / __ `/ _ \/ ___/ __ `/ ___/  / /   / / __ \/ __ \/ _ \/ ___/  ##')
print('##  / /___/ /_/ /  __(__  ) /_/ / /     / /___/ / /_/ / / / /  __/ /      ##')
print('##  \____/\__,_/\___/____/\__,_/_/      \____/_/ .___/_/ /_/\___/_/       ##')
print('##                                            /_/                         ##')
print('##                                                                        ##')
print('############################################################################')
print('############################################################################\n\n')

timesThrough = 0

	#dictionary letter lookup by number
letterDict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
					15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z', ' ': ' '}
	#dictionary number lookup by letter
numberDict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
					'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': ' '}
		
	#converts message to all uppercase for less coding and then uses a dictionary to convert all the letters to numbers for shifting later
def convert(convertMessage):
	numericMessage = ''
	messageToUpper = convertMessage.upper()
	messageToConvert = re.sub('[^a-zA-Z ]', '', messageToUpper)
	for letter in messageToConvert:
		numericMessage += str(numberDict[letter]) + '|'
	numericMessage = numericMessage[:-1]
	return numericMessage
		
def shift(shiftMessage, shiftPosition):
	messageEncryptionFinished = ''
	shiftList = []
	shiftList = shiftMessage.split('|')
	for number in shiftList:
		if number != ' ':
			number = int(number) + shiftPosition
			if number > 26:
				number = number - 26
			messageEncryptionFinished += str(letterDict[number])
		else:
			messageEncryptionFinished += str(letterDict[number])
	return messageEncryptionFinished
	
def chooseShift():
	encrypting = True
	while encrypting == True:
		userShift = input('Please enter the shift you would like to use on the message and then press enter (should be a positive integer): ')
		userShift = re.sub('[^0-9]', '', userShift)
		
		if userShift == '':
			print('\n')
			print('WARNING! Integer expected. Please enter a positive integer to continue.\n')
		elif userShift != '':
			userShift = int(userShift)
			while userShift > 26:
				userShift = userShift%26
			encrypting = False
		else:
			print('\n')
			print('WARNING! Integer expected. Please enter a positive integer to continue.\n')
	return userShift

while True:
	
	if timesThrough > 0:
		print('\n###########################################################################')
		userChoice = input('\nWould  you like to encrypt or decrypt another message (type \'y\' or \'yes\' to go again): ')
		if userChoice == 'Y' or userChoice == 'y' or userChoice == 'yes' or userChoice == 'Yes' or userChoice == 'YES':
			print('\n\n###########################################################################')
			print('###########################################################################')
			print('###########################################################################')
			print('###########################################################################')
			timesThrough = timesThrough - 1
		else:
			break
		
	else:
	
		print('\n\nNOTE: This program can only handle alphabetic characters. Anything not alphabetic will be removed.')
		print('      In addition, all messages will be output to uppercase letters for code optimization.\n')
		choice = input('What would you like to do (please choose the corresponding number or bracketed letter):\n\n   1. [E]ncrypt a plaintext message\n   2. [D]ecrypt an encrypted message\n\nChoice: ')
	
		if choice == '1' or choice == 'e' or choice == 'E':
			print('\n########################################')
			print('#                                  _   #')
			print('#  ___ _ __   ___ _ __ _   _ _ __ | |_ #')
			print('# / _ \ \'_ \ / __| \'__| | | | \'_ \| __|#')
			print('#|  __/ | | | (__| |  | |_| | |_) | |_ #')
			print('# \___|_| |_|\___|_|   \__, | .__/ \__|#')
			print('#                      |___/|_|        #')
			print('########################################\n')
			
			selectedUserShift = chooseShift()
			userMessage = input('\nPlease enter the message to be encrypted (non-alphabetic characters will be stripped out): ')
			encryptMessage = convert(userMessage)
			messageEncrypted = shift(encryptMessage, selectedUserShift)
			print('\nEncrypted Message:   ' + messageEncrypted + '\n')
			
			x = input('Press enter to continue. ')
			
			timesThrough += 1
			
		elif choice == '2' or choice == 'd' or choice == 'D':
			print('\n########################################')
			print('#     _                            _   #')
			print('#  __| | ___  ___ _ __ _   _ _ __ | |_ #')
			print('# / _` |/ _ \/ __| \'__| | | | \'_ \| __|#')
			print('#| (_| |  __/ (__| |  | |_| | |_) | |_ #')
			print('# \__,_|\___|\___|_|   \__, | .__/ \__|#')
			print('#                      |___/|_|        #')
			print('########################################\n')
		
			choice = input('Would you like to iterate through all shifts or do you know which shift you would like to use?\n\n   1. [I]terate through all options\n   2. [S]elect a shift for the cipher\n\nChoice: ')
			print('\n')
			if choice == '2' or choice == 's' or choice == 'S':
				selectedUserShift = chooseShift()
				userMessage = input('\nPlease enter the message to be decrypted (non-alphabetic characters will be stripped out): ')
				decryptMessage = convert(userMessage)
				messageDecrypted = shift(decryptMessage, selectedUserShift)
				print('\nDecrypted Message:   ' + messageDecrypted + '\n')
				
				x = input('Press enter to continue. ')
				
			elif choice == '1' or choice == 'i' or choice == 'I':
				userMessage = input('\nPlease enter the message to be decrypted (non-alphabetic characters will be stripped out): ')
				decryptMessage = convert(userMessage)
				for shiftElement in range(1,26):
					messageDecrypted = shift(decryptMessage, shiftElement)
					print('\nDecrypted Message:   ' + messageDecrypted + '\n')
					next = input('Press enter to try the next shift or type in \'exit\' without the quotes to exit the loop. ')
					if next == 'exit':
						break
					else:
						pass
				
			timesThrough += 1
		
		else:
			print('\nYou did not make a valid choice, please try again.\n')
		