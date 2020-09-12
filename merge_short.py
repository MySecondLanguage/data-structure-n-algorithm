def merge_short(nlist):
    print('spliting', nlist)
    if len(nlist) > 1:
        middle = len(nlist) // 2
        left_half = nlist[:middle]
        right_half = nlist[middle:]

        merge_short(left_half)
        merge_short(right_half)

        l = 0
        r = 0
        k = 0

        while l < len(left_half) and r < len(right_half):
            if left_half[l] < right_half[r]:
                nlist[k] = left_half[l]
                l=l+1
            else:
                nlist[k] = right_half[r]
                r=r+1
            k=k+1
        
        while l < len(left_half):
            nlist[k] = left_half[l]
            l=l+1
            k=k+1

        while r < len(right_half):
            nlist[k] = right_half[r]
            r=r+1
            k=k+1



        print('merging' ,nlist)



nlistt = [2,4,3,7,8,1,33,44,22,14,90,45]

print(merge_short(nlistt))

