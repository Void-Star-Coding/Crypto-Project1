import maux_crypto

#The second program should perform the verification process.  
#It also takes two input arguments as the first program.  
#It should generate hashes again 
	#(you can reuse some code  from  the  first  program  here)  and  
	#check  whether  they  are  matching  with  the corresponding values 
	#stored in directory 2.  

#For each file,  this program should output two strings:  
	#the filename and 
	#YES/NO (denoting whether the hashes are matching or not)

def r0n():
	my_input_d, my_output_d = maux_crypto.getInputOutputDirs()

	print("\nComparing hashes...\n")
	
	maux_crypto.dir2HashFiles(my_input_d,my_output_d,True)
	

if __name__ == "__main__":
	print(f"{__file__} Running...")
	r0n()
	
	print("End.")



