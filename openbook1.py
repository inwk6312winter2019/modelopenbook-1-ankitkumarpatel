#





def list_ifname_ip(filename):
    """function for task1"""
    fin = open(filename)
    dic = dict()
    for line in fin:
        if 'no' not in line: 
            if 'nameif' in line:
                name = line.strip().split()
	    	#print(name)


	    if 'ip address' in line:
	        ip = line.strip().split()
	    	#print(ip)
                dic.setdefault(name[1],(ip[2],ip[3]))

    #print(dic)
    return(dic)        


def new_config_file(filename):
    """function for task2"""
    fout = open("new_config.cfg","wa")
    fin = open(filename,"r")
    for line in fin:
        if 'ip address' in line:
            if '172.' in line:
	        line = line.replace("172.", "10.")
               
	    if '192.' in line:
		line = line.replace("192.", "10.")
               
	    if '255.255.0.0' in line:
		line = line.replace("255.255.0.0","255.0.0.0")
		
	    if '255.255.255.0' in line:
		line = line.replace("255.255.255.0","255.0.0.0")
		
        fout.write(line)
    fout.close()




def access_list(filename):
    """function for task3"""
    fin = open(filename,'r')
    global_access=[]
    transit_access_in=[]
    fw_management_access_in=[]



    for line in fin:
        if 'global_access' in line:
            lst1 = []
            line = line.strip().split()
	    for word in line:
                if word[0].isupper():
                    lst1.append(word)
            global_access.extend([lst1])


        if 'transit_access_in' in line:
            lst2 = []
            line = line.strip().split()
	    for word in line:
                if word[0].isupper():
                    lst2.append(word)
            transit_access_in.extend([lst2])


	if 'fw-management_access_in' in line:
            lst3 = []
            line = line.strip().split()
	    for word in line:
                if word[0].isupper():
                    lst3.append(word)
            fw_management_access_in.extend([lst3])


    print("\naccess list for global_access:")
    print(global_access)


    print("\naccess list for transit_access_in:")
    print(transit_access_in)


    print("\naccess list for fw_management_access_in:")
    print(fw_management_access_in)





#task 1 starts here
result = list_ifname_ip('running-config.cfg')
print("Required dictionary is as below:\n")
print(result)


#task 2 starts here
new_config_file('running-config.cfg')


#task 3 starts here
access_list('running-config.cfg')






