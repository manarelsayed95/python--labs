#!/usr/bin/env python3

import random
value=1

user_trials=[]
flag='yes'
win_count=0
lost_count=0
try_count=0
count=0

my_file = open('trials.txt', 'w')
my_file.write("welcome ")
my_file.close()

while (flag=='yes'):
	rand = random.randrange(1, 100, 1)
	print(rand)
	user_trials=[]
	#print(' welcome!! you plays ',try_count,'trials and won',win_count,'and lost',lost_count)

	my_file = open('trials.txt', 'r')
	content=my_file.read()
	my_file.close()
	print(content)

	while value!=11:

		user=int(input('enter a number  '))
		if (user>100 or user<1):
			print('out of range,enter another number')
			value-=1
			if(value!=10):
				count=10-value
				print('you still have ',count,'trials')
		elif user in user_trials:
			print('you entered this number before, enter another number')		
			value-=1
			if(value!=10):
				count=10-value
				print('you still have ',count,'trials')
		else:
					
			if (user>rand):
				print('number is bigger than the random number.')
				lost_count+=1
				
				if(value!=10):
					count=10-value
					print('you still have ',count,'trials')
				user_trials.append(user)
			elif user<rand:
				print('number is smaller than the random number.')
				lost_count+=1
				if(value!=10):
					count=10-value
					print('you still have ',count,'trials')
				user_trials.append(user)
			elif user==rand:
				print('congratulations!!')
				win_count+=1
				if(value!=10):
					count=10-value
					print('you still have ',count,'trials')
				if(value!=11):
					rand = random.randrange(1, 100, 1)
					print(rand)
			
		
		value+=1
		if(value==11):
			try_count+=1
			my_file = open("trials.txt", "a")
			my_file.write("you win ")
			my_file.write(str(win_count))
			my_file.write(" you lost ")
			my_file.write(str(lost_count))
			my_file.write(" you play ")
			my_file.write(str(try_count))
			my_file.close()
		
			
			print('if you want to play again please enter yes if not enter no  ')
			flag=input()
			if flag=='yes':
				value=1	
				#user_trials=0
				break
	
	

