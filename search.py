def WordSearch(Len, s, subs):
    st = s.split()
    result = []
    len_of_str = len(st)
    array_of_str=[]
    
    for i in range(len_of_str):
        if len(st[i]) > Len:
            too_much = len(st[i]) - Len
            del_end = len(st[i])+too_much
            st.insert(i+1,st[i][Len:Len + too_much])
            del_sym = list(st[i])
            del del_sym[len(st[i])-too_much:del_end]
            st[i] = ''.join(del_sym)
            
            
            
    for i in range(len(st)):
        b = []
        b.append(st[i])
        array_of_str.append(b)
        
    lenght =len(array_of_str)-1  
    for q in range(lenght-1):
        if q > lenght:
            break
        lenght =len(array_of_str)-1
        for j in range(len(array_of_str[q-1])):
            if  j!=1 and q < lenght and len(array_of_str[q][j]) <=5:
                array_of_str[q].append(array_of_str[q+1][j])
                array_of_str.pop([q+1][j])
                lenght =len(array_of_str)-1
                break
            else:
                lenght =len(array_of_str)-1
                
    word_in_str = False
    
    for i in range(len(array_of_str)): 
        for j in range(len(array_of_str[i])):
            if subs == array_of_str[i][j]:
                word_in_str = True
                break
            else:
                word_in_str = False
        if word_in_str:
            result.append(1)
        else:
            result.append(0)

    return result