#





def list_ifname_ip(filename):
    
    file = open(filename)
    dic = dict()
    for line in file:
        line = line.split()
        for i in line:
            if any(line[i] == 'nameif'):
                nameif = line[i+1]
            if any(line[i] == 'ip')
                IPaddress = line[i+2]
                NetMask = line[i+3]
            if  
            dic[nameif]=(IPaddress,NetMask)
return dic







list_ifname_ip('running-config.cfg')


