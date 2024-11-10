def pr_list(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    pr_list(list, idx+1)
    
    
ap=[1,2,'sachin','sunil','virat',4,5]

pr_list(ap)
