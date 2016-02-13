def mergesort(something):
    n=len(something)
    if n<2:
        return something[:]
    else:
        left=mergesort(something[:n/2])
        right=mergesort(something[(n/2):])
        merged=merge(left,right)
        return merged

def merge(list1,list2):
    n1=len(list1)
    n2=len(list2)
    n=n1+n2
    count_list1=0
    count_list2=0
    count_result=0
    result=[0]*n
    while count_list1<n1 and count_list2<n2:
        if list1[count_list1]<=list2[count_list2]:
            result[count_result]=list1[count_list1]
            count_list1+=1
        else:
            result[count_result]=list2[count_list2]
            count_list2+=1

        count_result+=1

    while count_list1<n1:
        result[count_result]=list1[count_list1]
        count_list1+=1
        count_result+=1

    while count_list2<n2:
        result[count_result]=list2[count_list2]
        count_list2+=1
        count_result+=1

    return result

print mergesort([1,5,6,7,2,5,7])

            
