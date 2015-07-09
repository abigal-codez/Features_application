import sys



def compare(o_rt, o_mz):
	specfiles = ['spec-00000.mzXML.csv','spec-00001.mzXML.csv','spec-00002.mzXML.csv','spec-00003.mzML.csv','spec-00004.mzXML.csv','spec-00005.mzXML.csv','spec-00006.mzXML.csv','spec-00007.mzXML.csv','spec-00008.mzXML.csv','spec-00009.mzXML.csv','spec-00010.mzXML.csv','spec-00011.mzML.csv']
	tol_rt = 20
	tol_mz = .3
	for spec in specfiles:
		#with open(str(sys.argv[1])) as f:
		print spec
		with open ("cluster_to_feature_test/feature_xml/data/"+spec) as f:
			c = 0
			for l in f: 
				if c != 0:
					ll = l.strip()
					ll = ll.split()
					rt1 = float(ll[0])
					mz1 = float(ll[1])
					
					min_rt = rt1 - tol_rt
					max_rt = rt1 + tol_rt
					min_mz = mz1 - tol_mz
					max_mz = mz1 + tol_mz
					 #print orig_rt
					 #print min_rt 
					 #print max_rt
					float(min_rt)
					float(max_rt)
					float(min_mz)
					float(max_mz)


					#print "rt1: " + rt1
					#print "mz1: " + mz1
					if (float(o_rt) > min_rt) and (float(o_rt) < max_rt):
						if (float(o_mz) > min_mz) and (float(o_mz) < max_mz):
							print l

					
				c+=1

"""#checking feature consensus accuracy
count = 0
file1 = open(str(sys.argv[1]))
#file2 = open(str(sys.argv[2]))
#with file1 as readfile:
	#next(readfile)



for line in file1:
	if count != 0:
		line = line.strip()
		line = line.split()
		rt = line[0]

		mz = line[1]
		#print "rt: " + rt
		#print " mz: " + mz"""
#file1 = open(str(sys.argv[1]))
rt = 537.834
mz = 70.013

compare(rt,mz)



"""	#else:
	count = count + 1
	#print "i am counting"
file1.close()"""