#





def list_ifname_ip(filename):
    
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

    print(dic)        


def new_config_file(filename):
    
    fout = open("new_config.cfg","wa")
    fin = open(filename,"r")
    for line in fin:
        if 'ip address' in line:
            if '172.0' in line:
	        line = line.replace("172.", "10.")
               
	    if '192.0' in line:
		line = line.replace("192.", "10.")
               
	    if '255.255.0.0' in line:
		line = line.replace("255.255.0.0","255.0.0.0")
		
	    if '255.255.255.0' in line:
		line = line.replace("255.255.255.0","255.0.0.0")
		
        fout.write(line)
    fout.close()


#list_ifname_ip('running-config.cfg')

new_config_file('running-config.cfg')

