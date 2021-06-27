# sorting function
ourlist = ['juma', 'isha', 'alli', 'pita']
def sorter(nlist):
    for i in range(len(nlist) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if nlist[j + 1] < nlist[j]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                no_swap = False
                
        
        if no_swap:
            return 
    