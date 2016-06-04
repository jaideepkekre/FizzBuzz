x=range(1,100,1)
three=False
five=False
for number in x :
	flag=-1
	T_print=number
	if number%3 == 0 :
		three = True
	if number% 5 == 0 :
		five = True
	if five:
		T_print = "Buzz"
	if three:
		T_print="Fizz"
	if three and five :
		T_print="FizzBuzz"
	three = False
	five = False
	print T_print
