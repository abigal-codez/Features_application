#comments for later

import sys
import os

#w_file = rfile.readlines()[1:]

def parse_xml_file(input_file):
    key_value_pairs = {}
    for line in input_file:
        #print line
        new_line = line.rstrip().replace("<parameter name=\"", "")
        #new_line = new_line.replace("\">", "=")
        new_line = new_line.replace("</parameter>", "")
        
        splits = new_line.split("\">")
        #print splits
        if(len(splits) != 2):
            continue
          

        if(splits[0] in key_value_pairs.keys()):
          key_value_pairs[splits[0]].append(splits[1])
        else:
          key_value_pairs[splits[0]] = []
          key_value_pairs[splits[0]].append(splits[1])
        
    print "blah blah does parse"   
    return key_value_pairs

def get_mangled_file_mapping(params):
    all_mappings = params["upload_file_mapping"]
    mangled_mapping = {}
    for mapping in all_mappings:
        splits = mapping.split("|")
        mangled_name = splits[0]
        original_name = splits[1]
        mangled_mapping[mangled_name] = original_name
    
    return mangled_mapping



rfile = str(sys.argv[1])
count = 0
with open(rfile) as f:
	for line in f:
 		if count != 0 and count < 2:
 			line = line.strip()
 			columns = line.split()
 			clusterID = columns[0]
 			filename = columns[1] 

 			with open(filename) as ff: #ff = fockin' file
 				key = parse_xml_file(filename)
 				print "Filename:", filename, ", key:", key
 			ret = columns[6]
 			print "doing loop once"
 			#demangle this file name
 			
 			#match to the other name
 			#use ret time to match
 			#take the abundance 
 			#create new column???
 			

 		count+=1
 		#var =clusterID



#rfile.close()
