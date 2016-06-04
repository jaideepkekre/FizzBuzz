#!/usr/bin/python 

"""
author: Jaideep Kekre
"""
import dis

def test():
	for number in range(1,101,1):
		if number%15 == 0 : 
			print "FizzBuzz"
		elif number%5 == 0 :
			print "Buzz"
		elif number%3==0:
			print"Fizz"
		else:
			print number


test()
print"**************"
#dis-assemble code toi see instructions, 109 in this case
dis.dis(test)