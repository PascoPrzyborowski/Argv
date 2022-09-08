import getopt, sys


# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

# Options
options = "hmoflskn:"

# Long options
long_options = ["Help", "My_file", "Output=","Fast_Mode","Lowly_Mode","Stealth_Mode","New_Mode","Kill_Switch"]

try:
	# Parsing argument
	arguments, values = getopt.getopt(argumentList, options, long_options)
	
	# checking each argument
	for currentArgument, currentValue in arguments:

		if currentArgument in ("-h", "--Help"):
			print()
			print()
			print("Displaying Help Mode")
			print("If you want some Help ask Google!")
			print()
			print("Ok I give you a hint and some Options: ")
			print()
			print("-h : Give you this HelpFile!")
			print("-m : Give you the Name of this File!")
			print("-o : Give you some Output!")
			print("-f : Give you the Fast Mode!")
			print("-l : Give you the Slow Mode!")
			print("-s : Give you the Stealth Mode!")
			print("-k : Give you a Kill Switch!")


		elif currentArgument in ("-m", "--My_file"):
			print("Displaying file_name:", sys.argv[0])
			
		elif currentArgument in ("-o", "--Output"):
			print(("Enabling special output mode (% s)") % (currentValue))
			
		elif currentArgument in ("-f", "--Fast_Mode"):
			print ("Displaying Fast Mode now!")
			print ("You running on RedBull, now!")

		elif currentArgument in ("-l", "--Lowly_Mode"):
			print ("Displaying Slowly Mode now!")
			print ("You are in Chill Mode, now!")
			
		elif currentArgument in ("-s", "--Stealth_Mode"):
			print ("Displaying Stealth Mode now!")
			print ("You are very Stealthy, now!")
			
		elif currentArgument in ("-k", "--Kill_Switch"):
			print ("Kill Switch enable Displaying file_name to Delete:", sys.argv[0])
		
		if currentArgument in ("-n", "--New_Mode"):
			print ("Displaying file_name:", sys.argv[0])
		

except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
