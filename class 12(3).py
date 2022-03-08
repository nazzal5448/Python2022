while True:
	print("Welcome to smart home mini!\n Select the item to operate:\n	")
	item=input("Bulb, TV, Fan, AC, Geaser \n")
	if item=="bulb":
		user=input("Switch: On/ Off \n")
		if user=="on":
			print("Bulb is switched on")
		elif user=="off":
			print("Bulb is switched off")
	elif item.lower()=="ac":
		user=input("Switch: On/ Off \n")
		if user=="on":
			print("AC is switched on")
		elif user=="off":
			print("AC is switched off")
	elif item=="fan":
		user=input("Switch: On/ Off \n")
		if user=="on":
			print("Fan is switched on")
		elif user=="off":
			print("Fan is switched off")
	elif item.lower()=="tv":
		user=input("Switch: On/ Off \n")
		if user=="on":
			print("TV is switched on")
		elif user=="off":
			print("TV is switched off")
	elif item=="geaser":
		user=input("Switch: On/ Off\n")
		if user=="on":
			print("Geaser is switched on")
		elif user=="off":
			print("Geaser is switched off")
	print("Thanks for using my services ♡")
	user=input("Do you want to exit : Yes/No \n")
	if user=="yes":
		break
	else:
		continue