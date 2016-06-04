x=range(1,101,1)
three=False
five=False
for number in x :
	flag=-1
	T_print=number
	if number%3 == 0 :
		three = True
	if number% 5 == 0 :
		five = True
	if three and five :
		T_print="FizzBuzz"
	elif five:
		T_print = "Buzz"
	elif three:
		T_print="Fizz"	
	three = False
	five = False
	print T_print
