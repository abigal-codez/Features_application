import sys
import os

#w_file = rfile.readlines()[1:]

#param parsing functions for demangling

def parse_xml_file(input_file):
    #feed this params.xml
    #cleans the .xml file and returns a dictionary of (keys) parameters and their values
    key_value_pairs = {}
    for line in input_file:
        #remove parameter xml tags
        new_line = line.rstrip().replace("<parameter name=\"", "")
        #new_line = new_line.replace("\">", "=")
        new_line = new_line.replace("</parameter>", "")
        
        splits = new_line.split("\">")
        #print splits
        if(len(splits) != 2):
            continue
          
        #if first item of the line is in the dictionary's keys, add the second item to its corresponding value
        if(splits[0] in key_value_pairs.keys()):
          key_value_pairs[splits[0]].append(splits[1])
        #otherwise, make it an empty list, then add that second item
        else:
          key_value_pairs[splits[0]] = []
          key_value_pairs[splits[0]].append(splits[1])
        
    #print ".xml file parsed" 
    return key_value_pairs

def get_mangled_file_mapping(params):
    #feed this cleaned params.xml
    #split the key, mangled name is the spec-0000X.mzXML file
    #original name is the metabolomics file
    all_mappings = params["upload_file_mapping"]
    mangled_mapping = {}
    for mapping in all_mappings:
        splits = mapping.split("|")
        mangled_name = splits[0]
        original_name = splits[1]
        mangled_mapping[mangled_name] = original_name
    

    return mangled_mapping


def eureka(m_file, m_ret):
    # user given rention time and mass/charge
    #called later, m_file = sfile, m_ret = ret
    orig_rt = float(m_ret)

    # parameter/tolerance allowed, just using 0.03 for now, *adjust later if needed*
    tol_rt = float(1)
    #print(orig_rt, orig_mz, tol)

    min_rt = orig_rt - tol_rt
    max_rt = orig_rt + tol_rt
    print orig_rt
    print min_rt 
    print max_rt
    float(min_rt)
    float(max_rt)
    sfile = open(m_file,"r")
    #iterate over each line in the sfile

    with open(m_file) as ff:
        #for line in f:

        next(ff)
        for sline in ff:
        #use ret time with tolerance to match
            sline = sline.strip()
            sline = sline.split()
            sret = float(sline[0])
            if (sret > min_rt) and (sret < max_rt):
                print "hi"
        #hard-matching, is unlikely to work
        #if ret = sline[0]
            #take the abundance, 3rd column/index 2
                abundance = sline[2]
                print "ret " + str(ret) + " found in line with abundance " + str(abundance)

            #abundance is added to the end of the line original 
                columns.append(abundance)
            #still have to write "columns" list into a new file
            else:
                pass
            #no matching ret was found, thus there was no corresponding abundance
    sfile.close()
    #min_mz = orig_mz - tol_mz
    #max_mz = orig_mz + tol_mz
    #float(min_mz)
    #float(max_mz)
    #print hello


#string containing the name of the file to be read
rfile = str(sys.argv[1])
count = 0

ofile = rfile + "_output"
o_f = open(ofile, 'w')

#open the params.xml file for the demanglers
#this .py should be run in the same folder containing the params.xml file
#which .xml file do we want? clustering/ or feature_xml/ ?
#paramdict is a dictionary, keys are parameters (parameter: value)
cluster_dict = parse_xml_file(open("clustering/params.xml"))
#print "cluster dict: " + str(cluster_dict)

#mapped is a dictionary, keys are spec-0000X files, values are data files (file name: file name)
#maybe pick a better variable name?
cluster_mapped = get_mangled_file_mapping(cluster_dict)
#print "cluster mapped: " + str(cluster_mapped)

feature_dict = parse_xml_file(open("feature_xml/params.xml"))
#print "feature dict: " + str(feature_dict)

feature_mapped = get_mangled_file_mapping(feature_dict)
#print "feature mapped: " + str(feature_mapped)


match = False
#loops through the file with the cluster averages
with open(rfile) as f:
    for line in f:
        if count == 0:
            o_f.write(line)
            #adjust count for the number of lines to read
        if count != 0 and count < 4:
            line = line.strip()
            columns = line.split()
            #corresponds with cluster ID, filename: need to map, ret_time to be matched
            clusterID = columns[0]
            filename = columns[1]
            ret = columns[6]
            
            #gives leaf filename in the form spec-0000X.mzML
            filename = os.path.basename(filename)


            #look for the mapped file (metabolomics, values are the same)
            #mapped file names in the form spec-0000X.mzXML
            for key in cluster_mapped:
                #for some reason 00003 is still mzML in the params
                if filename[:10] == key[:10]:
                    paramfilename = key
                    #print paramfilename
                    #print "cluster map: " 
                    #print cluster_mapped[paramfilename] 
                    #print "feature map: " 
                    #print feature_mapped[paramfilename]
                    if cluster_mapped[paramfilename] == feature_mapped[paramfilename]:
                        match = True
                        sfilename = "feature_xml/data/"+str(paramfilename)+".csv"
            #demangle this file name, though maybe already demangled?
            if match == True:
                eureka(sfilename,ret)
                #eureka('feature_xml/data/test.txt',ret)
                #call function that does the matching of the retention time and gives the value of it
                o_f.write(str(columns)+"\n")
                #attempt at writing things into an output file
            #this part is probably prone to errors
            #match to the other name by tolerance/ use abby's code
            #s can be for spec or search
            #giving the directory -> not modular at the moment if other folder names are used
                
                #print sfilename
            #actual file name: spec-0000X.mzXML.csv
            
            

        count+=1
    #var =clusterID


o_f.close()
