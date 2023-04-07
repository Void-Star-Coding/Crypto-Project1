import hmac
import os

#The second program should perform the verification process.  
#It also takes two input arguments as the first program.  
#It should generate hashes again 
	#(you can reuse some code  from  the  first  program  here)  and  
	#check  whether  they  are  matching  with  the corresponding values 
	#stored in directory 2.  

#For each file,  this program should output two strings:  
	#the filename and 
	#YES/NO (denoting whether the hashes are matching or not)

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
	
#
def fileToString(vstr_filename):
	file = open(vstr_filename,"r")
	ret = str(file.read())
	return ret

print("\nComparing hashes...\n")
#CHANGED FROM C1
for filename in os.listdir(my_input_d):
	full_filename = os.path.join(my_input_d, filename)
	nbytes = filename4hash(full_filename)
	
	new_filename = os.path.splitext(filename)[0] + "-hash.txt"
	newfull_filename = os.path.join(my_output_d,new_filename)
	#print(f"{newfull_filename} --> {nbytes}")
	
	#"og hash"
	b2str = str(nbytes)
	'''
	openNwrite(newfull_filename,b2str)'''	#CHANGED
	
	#added
	
	f2str = fileToString(newfull_filename)
	#print(f"{newfull_filename}\n{f2str}\n\n")
	
	#'''
	
	print(f"file:{newfull_filename}\n{b2str}\n{f2str}\n")
	if f2str.find(b2str) != -1:
		print('YES - The output and files in the directory are the same')
	else:
		print('NO - The output and files in the directory are different')
	#'''
	print("\n")
#removed

#moved