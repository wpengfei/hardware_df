import os
import os.path
import shutil
import json



# a tool used to copy files from source to stage1_identify/
class Tool:
	def __init__(self ):
		if not os.path.exists("stage1_identified/"):
			os.mkdir('stage1_identified/')
			#os.path.isfile('test.txt') 

		self.result_handler = open("record_identified.txt","r")
		if not self.result_handler:
			print "open record_indentified.txt failed!"

		self.buffer = ""

		self.counter = 0

	def get_dst(self, src, num):
		p = src.rfind('/')
		filename = src[p+1:]
		return 'stage1_identified/'+str(num)+'---'+filename #add 'num' in the file name to distinguish files with same name in the same dir

		
	def main(self):
		
		while True:
			line_str = self.result_handler.readline()
			if not line_str:
				print "Finished copying."
				break
			else:
				
				line = line_str[:len(line_str)-1] #cut \n
				data = json.loads(line) #switch to python dict
				src = data['origin_file']
				num = data['No.']
				if src != self.buffer: #skip copying the same file
					self.buffer = src
					self.counter = self.counter + 1
					dst = self.get_dst(src, num)
					print "Copying from: ", src, "\tto: ", dst
					shutil.copy(src,dst) 
					
					
	def finish(self):
		self.result_handler.close()
		print self.counter, "file copied"

###########################################
mytool = Tool()
mytool.main()
mytool.finish()


