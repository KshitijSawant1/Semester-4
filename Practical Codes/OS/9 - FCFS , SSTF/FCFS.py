def fcfs (request,head):
    seek = 0 
    sequence = []
    
    for r in request :
        distance += abs(head-r)
        seek += distance 
        sequence.append(r)
        head=r
        
    print(f"FSFC Disk Scheduling")
    print(f"Head : {head}")
    print(f"Seek Sequence : ",'->'.join(map(str,sequence)))
    print(f"Total Seek Time : {seek}")
    
request = [19,28,37,46,55,64,73,82,91]
head = 50
fcfs(request,head)
