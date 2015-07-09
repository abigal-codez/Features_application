def outline():
    '''
    consensus_features.csv - predetermined consensus features
    based on "similar" rt and mz of species

    range of mz: 68-1349

    goal: evaluate if these consensus features are 
    well-determined (accurate), by considering the ms2 spectra 
    of the species that constitute a feature, as this is a property
    that should be independent of rt and mz, yet distinctive to
    a species/feature

    ms2 spectra are given by "cluster_spectra.clusterinfo"
    entries are sorted by clusterID, and also have mz and rt

    range of mz: 166-1200 (thinner than that of .csv)
    (index 4)

    for a given clusterID X, all entries with that clusterID
    are assumed to have the same ms2 properties
    (index 0)

    there is little variance between mz of a given clusterID,
    no more than 0.01

    mz may be used to "identify" species in the ms2 file but
    NOT as a basis for comparison, that is what ms2 is for

    however, it seems that even mz distributions between the files
    varies quite a bit

    somewhere the demangler comes into this, may also be 
    used for IDing?
    '''
    print "why did you call the outline"

import sys
#arg0 is the name of this file
#arg1 is the consensus features file
#arg2 is the spectra file

import os

print "running " + str(sys.argv[0])

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
    #returns another dictionary
    all_mappings = params["upload_file_mapping"]
    mangled_mapping = {}
    for mapping in all_mappings:
        splits = mapping.split("|")
        mangled_name = splits[0]
        original_name = splits[1]
        mangled_mapping[mangled_name] = original_name
    

    return mangled_mapping

cluster_dict = parse_xml_file(open("clustering/params.xml"))
cluster_mapped = get_mangled_file_mapping(cluster_dict)
feature_dict = parse_xml_file(open("feature_xml/params.xml"))
feature_mapped = get_mangled_file_mapping(feature_dict)
#mangling -> refers to the file names