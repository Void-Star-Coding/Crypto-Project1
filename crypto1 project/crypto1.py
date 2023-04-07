import hmac
import os
#The first program should take two user inputs as arguments: directory1 and directory2.
#Your program should compute a hash value (using HMAC) for __each file__ (based on its content) 
	#in the folder directory1
#and store that hash value in a new file that will be saved under the folder directory2.

#For example, if you have two files, file1 and file2, in directory1,
#your program should create two files, say file1-hash and file2-hash that 
	#store the hash values of the contents of the corresponding two files under directory2.

print("Running...")

my_digest_str = 'some-nonsene-key-thing-idk'
encoded_digest = my_digest_str.encode("ascii","ignore")




print("Exclude '<Drive>:\\' to use current directory instead of direct reference")
directory1_input = input("Directory1 (input folder): ")
if not directory1_input:
	directory1_input = "input"
directory2_output = input("Directory2 (output folder): ")
if not directory2_output:
	directory2_output = "output"

print("")

running_directory = os.getcwd()		#current directory

my_input_d = ""
if ":\\" not in directory1_input:
	#print("Input is current dir")
	my_input_d = my_input_d + running_directory + "\\"
my_input_d = my_input_d  + directory1_input
print(f"Directory1 input: {my_input_d}") 

my_output_d = ""
if ":\\" not in directory2_output:
	#print("Output is current dir")
	my_output_d = my_output_d + running_directory + "\\"
my_output_d = my_output_d  + directory2_output
print(f"Directory2 output: {my_output_d}") 


#given a filename
#returns the hash value of a file using my_digest_maker
def filename4hash(vstr_filename):
	file = open(vstr_filename,'rb')
	
	tmsg = file.read()
	#tenc = tmsg.encode()
	dmod = "sha256"
	
	d_mak = hmac.new(encoded_digest,msg=tmsg,digestmod=dmod)
	ret = d_mak.digest()
	'''
	try:
		while True:
			block = file.read(1024)
			if not block:
				break
			my_digest_maker.update(block)
	finally:
		file.close()
	
	ret = my_digest_maker.hexdigest()'''
	
	return ret

def openNwrite(vstr_filename,vvalue):
	file = open(vstr_filename,"w+")
	file.write(vvalue)
	file.close()

print("\nInput files:")
for filename in os.listdir(my_input_d):
	full_filename = os.path.join(my_input_d, filename)
	nbytes = filename4hash(full_filename)
	
	new_filename = os.path.splitext(filename)[0] + "-hash.txt"
	newfull_filename = os.path.join(my_output_d,new_filename)
	print(f"{newfull_filename} --> {nbytes}")
	
	b2str = str(nbytes)
	
	openNwrite(newfull_filename,b2str)
	
	#checking if it is a file
    #if os.path.isfile(f):
    #    print(f)
	
print("End.")