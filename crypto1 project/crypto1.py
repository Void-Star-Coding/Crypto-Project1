import hmac
import os
import maux_crypto

#The first program should take two user inputs as arguments: directory1 and directory2.
#Your program should compute a hash value (using HMAC) for __each file__ (based on its content) 
	#in the folder directory1
#and store that hash value in a new file that will be saved under the folder directory2.

#For example, if you have two files, file1 and file2, in directory1,
#your program should create two files, say file1-hash and file2-hash that 
	#store the hash values of the contents of the corresponding two files under directory2.

def r0n():
	my_input_d, my_output_d = maux_crypto.getInputOutputDirs()

	print("\nCalculating hashes...\n")
	
	maux_crypto.dir2HashFiles(my_input_d,my_output_d)
	

if __name__ == "__main__":
	print(f"{__file__} Running...")
	r0n()
	
	print("End.")