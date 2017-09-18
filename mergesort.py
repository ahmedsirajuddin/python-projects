def main(listy):

    myList = listy

    print("UnSorted: ")
    print(myList)
    

    myList = msort(myList)

    print("Sorted: ")
    print(myList)
    
  
def msort(unsorted): 

    if len(unsorted) == 1:
	      return unsorted

    left = []
    right = []

    left = unsorted[:len(unsorted)/2]
    right = unsorted[len(unsorted)/2:]

    

    left = msort(left)

    right = msort(right)

    return merge(left, right)
  



def merge(left, right):
    print("Merging")
    print("Left: ")
    print(left)
    print("Right: ")
    print(right)
    

    fin = []

    lp = 0
    rp = 0
    fp = 0
    

    while lp < len(left) and rp < len(right):

        if left[lp] < right[rp]:

            fin.append(left[lp])

            lp += 1

        else:

                fin.append(right[rp])
      
                rp += 1

        fp += 1


    # !ADDED
    if lp == len(left):
	while rp < len(right):
	    fin.append(right[rp])
	    rp += 1
    if rp == len(right):
	while lp < len(left):
	    fin.append(left[lp])
	    lp += 1





    print("MERGED: ")
    print(fin)
    print("-------------")
    return fin

if __name__ == "__main__":
    main([4, 10, 9, 2, 7, 6, 6, 1, 2])
