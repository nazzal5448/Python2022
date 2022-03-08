ac="off"
while True:
	temp=int(input("Enter the temperature in Celsius: \n"))
	if temp<=15:
		print("Turning off the AC.")
	elif temp>20:
		print("Turning On the AC.")
	if ac=="off":
		break