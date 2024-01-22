def merge_a(string, k):
    # your code goes here
    chunck_len = int(len(string)/k)
    u=list()
    for i in range(0, len(string), chunck_len):
        sub_u=list()
        for j in range(i, (i+chunck_len)):
            if(string[j] in sub_u):
                next
            else:
                sub_u.append(string[j])
        sub_u_str = "".join(sub_u)        
        u.append(sub_u_str)
    return(u)
