#





def list_ifname_ip(filename):
    
    file = open(filename)
    dic = dict()
    for line in file:
        if 'no' not in line: 
            if 'nameif' in line:
                name = line.strip().split()
	    	print(name)


	    if 'ip address' in line:
	        ip = line.strip().split()
	    	print(ip)
                dic.setdefault(name[1],(ip[2],ip[3]))

    print(dic)        




list_ifname_ip('running-config.cfg')


