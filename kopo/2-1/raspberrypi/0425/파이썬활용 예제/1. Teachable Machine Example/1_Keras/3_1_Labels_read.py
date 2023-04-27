def readLabels():
    f = open("labels.txt", 'r')
    list_labels = []
    try:
        while True:
            line = f.readline()
            if not line: break
            getlabel = line.split(' ')
            getlabel = getlabel[1].split('\n')
            list_labels.append(getlabel[0])
        f.close()
    except Exception as e :
        print(e)
    return list_labels

list_labels = readLabels()
for i in list_labels:
    print(i)