## Fun Stuff 1
import sys
import os

start = True
chance = 0
x = []
conditions_met = False

# is user ready ?
READY = raw_input('Ready ?(Y/N), E for exit: ')

	# PROGRAM STARTS HERE {step 0}
def main():
	
	if(READY == 'Y' or READY == 'y'):
		chance_emulator()
	elif (READY == 'E' or READY == 'e'):
		sys.exit()
	elif (READY == 'N' or READY == 'n'):
		ask_again()
	else:
		sys.exit()

# function to show design after each line
#   1  |  2  |  3
# ------------------
#   4  |  5  |  6
# ------------------
#   7  |  8  |  9
#

def design_emulator():
	global start
	global chance

    # check if user want to be X or 0 at first
	if(start):
		fill_blanks()
		x_or_zero_first = raw_input("Choose to put X or 0 ?? : ")
		if(x_or_zero_first is '0'):
			chance = 1


	show_design()

# visual representation of current status
def show_design():
	global x
	print "  " + str(x[0]) + "  |" + "  " + str(x[1]) + "  |"  + "  " + str(x[2]) 
	print '-----------------'
	print "  " + str(x[3]) + "  |" + "  " + str(x[4]) + "  |"  + "  " + str(x[5]) 
	print '-----------------'
	print "  " + str(x[6]) + "  |" + "  " + str(x[7]) + "  |"  + "  " + str(x[8]) 


def chance_emulator():
	global chance
	global conditions_met

	while(chance != 2 ):
		# if chance is 0 {X's chance}
		if (chance == 0):
			os.system('cls')
			os.system('clear')
			print " "
			print " "
			print " "
			design_emulator()
			print " "
			print " "
			print " "
			print "X's chance now !"
			block = int(raw_input('select block: '))
			block = block - 1;
			valid = check_validity(block,chance)
			if (valid == True):
				fill_values(block,chance)
				conditions_met = user_won(chance)

				if(conditions_met == True):
					os.system('cls')
					os.system('clear')
					print " "
					print " "
					print " "
					print "----------------------"
					print "      WINNER"
					print "----------------------"
					print " "
					print " "
					print " "
					design_emulator()
					print " "
					print " "
					print " "
					print "----------------------"
					print "|"
					print "|"
					print "|"
					print "|"
					print "|"
					print "v"
					print "X has WON !!!!!!!!"
					chance = 2
				else:
					chance = 1

				if all([conditions_met == False , all_blocks_filled() == True]):
					os.system('cls')
					os.system('clear')
					print " "
					print " "
					print " "
					print "----------------------"
					print "      DRAW GAME"
					print "----------------------"
					print " "
					print " "
					print " "
					design_emulator()
					print " "
					print " "
					print " "
					print "----------------------"
					print "|"
					print "|"
					print "|"
					print "|"
					print "|"
					print "v"
					print "Its a draw !!!!!!!!"
					chance = 2
			else:
				print " "
				print " "
				print "---------------------"
				print "BLOCK ALREADY FILLED"
				print "---------------------"
		# if chance is 1 {0's chance}
		elif (chance == 1):
			os.system('cls')
			os.system('clear')
			print " "
			print " "
			print " "
			design_emulator()
			print " "
			print " "
			print " "
			print "0's chance now !"
			block = int(raw_input('select block: '))
			block = block - 1;
			valid = check_validity(block,chance)
			if (valid == True):
				fill_values(block,chance)
				conditions_met = user_won(chance)

				if(conditions_met == True):
					os.system('cls')
					os.system('clear')
					print " "
					print " "
					print " "
					print "----------------------"
					print "      WINNER"
					print "----------------------"
					print " "
					print " "
					print " "
					design_emulator()
					print " "
					print " "
					print " "
					print "----------------------"
					print "|"
					print "|"
					print "|"
					print "|"
					print "|"
					print "v"
					print "0 has WON !!!!!!!!"
					chance = 2
				else:
					chance = 0

				if all([conditions_met == False , all_blocks_filled() == True]):
					os.system('cls')
					os.system('clear')
					print " "
					print " "
					print " "
					print "----------------------"
					print "      DRAW GAME"
					print "----------------------"
					print " "
					print " "
					print " "
					design_emulator()
					print " "
					print " "
					print " "
					print "----------------------"
					print "|"
					print "|"
					print "|"
					print "|"
					print "|"
					print "v"
					print "Its a draw !!!!!!!!"
					chance = 2
			else:
				print " "
				print " "
				print "---------------------"
				print "BLOCK ALREADY FILLED"
				print "---------------------"


# check horizontal/vertical/cross
def user_won(c):
	if(c == 0):
	# horizontal conditions
		if all([ x[0] is "X", x[1] is "X", x[2] is "X" ]):
			return True
		elif all([ x[3] is "X", x[4]is "X", x[5] is "X" ]):
			return True
		elif all([ x[6] is "X", x[8] is "X", x[7] is "X" ]):
			return True
	# vertical conditions
		elif all([ x[0] is "X", x[3] is "X", x[6] is "X" ]):
			return True
		elif all([ x[1] is "X", x[4] is "X", x[7] is "X" ]):
			return True
		elif all([ x[2] is "X", x[5] is "X", x[8] is "X" ]):
			return True
	# cross conditions
		elif all([ x[0] is "X", x[4] is "X", x[8] is "X" ]):
			return True
		elif all([ x[2] is "X", x[4] is "X", x[6] is "X" ]):
			return True
		else:
			return False
	elif(c == 1):
	# horizontal conditions
		if all([ x[0] is "0", x[1] is "0", x[2] is "0" ]):
			return True
		elif all([ x[3] is "0", x[4]is "0", x[5] is "0" ]):
			return True
		elif all([ x[6] is "0", x[8] is "0", x[7] is "0" ]):
			return True
	# vertical conditions
		elif all([ x[0] is "0", x[3] is "0", x[6] is "0" ]):
			return True
		elif all([ x[1] is "0", x[4] is "0", x[7] is "0" ]):
			return True
		elif all([ x[2] is "0", x[5] is "0", x[8] is "0" ]):
			return True
	# cross conditions
		elif all([ x[0] is "0", x[4] is "0", x[8] is "0" ]):
			return True
		elif all([ x[2] is "0", x[4] is "0", x[6] is "0" ]):
			return True
		else:
			return False

# check if all blocks filled
def all_blocks_filled():
	global x
	drum = []
	for z in range(9):
		if(x[z] != ' '):
			drum.append('a')
		else:
			drum.append(' ')

	for g in range(9):
		if(drum[g] is 'a'):
			return False
		else:
			return True

# check if user entered block is already filled and the value is valid
def check_validity(block,c):
	global x
	if(c == 0):
		if any([ x[block] is "X", x[block] is "0"]):
			return False
		else:
			return True
	elif(c ==1):
		if any([x[block] is "0", x[block] is "X"]):
			return False
		else:
			return True



# fill array with blanks at start
def fill_blanks():
	global x
	global start
	for i in range(9):
		x.append(' ')

	start = False

# fill values in blocks
def fill_values(b,c):
	if(c == 0):
		x[b] = "X"
	elif (c == 1):
		x[b] = "0"


def ask_again():
	global READY
	READY = raw_input('NOW ARE YOU READY ?(Y/N), E for exit: ')

	if(READY == 'Y' or READY == 'y'):
		design_emulator()
		chance_emulator()
	elif (READY == 'E' or READY == 'e'):
		sys.exit()
	elif (READY == 'N' or READY == 'n'):
		ask_again()
	else:
		sys.exit()



if __name__ == '__main__':
    main()
