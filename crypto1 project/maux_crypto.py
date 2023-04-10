import hmac
import os

my_digest_str = 'some-long-key-thing'
encoded_digest = my_digest_str.encode("ascii","ignore")

def getInputOutputDirs():
	print("Exclude '<Drive>:\\' to use current directory instead of direct reference\nLeave blank to use default folders: 'input' and 'output'")
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
	
	return directory1_input, directory2_output
	
#given a filename
#returns the hash value of a file using my_digest_maker
def filename4hash(vstr_filename):
	file = open(vstr_filename,'rb')
	
	tmsg = file.read()
	#tenc = tmsg.encode()
	dmod = "sha256"
	
	d_mak = hmac.new(encoded_digest,msg=tmsg,digestmod=dmod)
	ret = d_mak.digest()
	
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
	
def dir2HashFiles(vmy_input_d,vmy_output_d,vcompare=False):
	for filename in os.listdir(vmy_input_d):
		full_filename = os.path.join(vmy_input_d, filename)
		nbytes = filename4hash(full_filename)
		
		new_filename = os.path.splitext(filename)[0] + "-hash.txt"
		newfull_filename = os.path.join(vmy_output_d,new_filename)
		
		#"og hash"
		b2str = str(nbytes)
		print(f"FILE: {new_filename}\nHASH: {b2str}")
		if not vcompare:
			openNwrite(newfull_filename,b2str)

		else:
			f2str = fileToString(newfull_filename)
			print(f"OHSH: {f2str}")
			print("SAME: ",end="")
			if f2str.find(b2str) != -1:
				print('YES - The output and files in the directory are the same')
			else:
				print('NO - The output and files in the directory are different')
			#'''
		
		print("\n")
		
	