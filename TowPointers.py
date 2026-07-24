def TwoSum():
    arr = [5,7,8,9,10,12,14,18]
    target = 22
    elements = []
    for i in arr:
        if(len(elements) != 0): break
        for j in arr:
            if(i + j == target):
                elements.append(i)
                elements.append(j)
    if(len(elements) == 0):
        print("no Elements found")
            
    for i in elements:
        print(i)
# TwoSum()

# two pointer
def TwoSumWith2Pointer():
    arr = [5,7,8,9,10,12,14,18]
    target = 20
    elements = []
    
    # start the 2 pointer
    i = 0
    j = len(arr) - 1
    
    while(i<j):
        sum = arr[i] + arr[j]
        if(sum == target): 
            elements.append(arr[i])
            elements.append(arr[j])
            break;
        elif(sum < target):
            i+=1
        else:
            j-=1
    if(len(elements) == 0):
        print("No elements are there whose sum is equal to target")
    else:
        print(elements)
# TwoSumWith2Pointer()

def checkPalindrome():
    string = input("Enter the string: ");
    stringCopy = string
    l1 = []
    for i in string:
        l1.append(i)
    i, j = 0, len(l1) - 1
    while(i<j):
        l1[i], l1[j] = l1[j], l1[i]
        i+=1
        j-=1
    result = "".join(l1)
    if(result == stringCopy):
        print("String is plaindrome")
    else:
        print("String is not palindrome")
# checkPalindrome()
def CountMatchingCharacters():
    string = "aabbcdacdbbaa"
    i,j=0,len(string)-1
    count=0
    while(i<j and string[i]==string[j]):
        count+=2
        i+=1
        j-=1
    print(f"number of repetative elements are {count}")
# CountMatchingCharacters()

def ShiftAllZeros():
    arr = [0,1,0,3,12]
    left = 0
    for right in range(len(arr)):
        if(arr[right] != 0):
            # swap number
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
    print(arr)
# ShiftAllZeros()

def separateEvenOdd():
    arr = [3,6,1,8,5,2]
    start = arr[0]
    left = 1
    isEven = start % 2 == 0
    
    if(isEven):
        for right in range(1,len(arr)):
            if(arr[right] % 2 == 0):
                # swap the element with left
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
    else:
        for right in range(1,len(arr)):
            if(arr[right] % 2 != 0):
                # swap the element with left
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
    
    print(arr)
# separateEvenOdd()

def countTwoSum():
    arr = [1,2,5,8,9,10,11,13,14,15,16,18,19,22]
    target, left, right =24, 0, len(arr) - 1
    l1 = []
    while(left<right):
        sum = arr[left] + arr[right]
        if (sum==target):
            elements = (arr[left], arr[right])
            l1.append(elements)
            left+=1
            right-=1
        elif sum < target:
            left += 1
        else:
            right =- 1
    print(l1)
# countTwoSum()


def removeDuplicates():
    arr = [1,1,2,2,3,4,4,5,6,6]
    left = 0
    for right in range(1, len(arr)):
        # check if left is equal to right
        if(arr[left] != arr[right]):
            # shift left to next position and then assign right to left
            left += 1
            arr[left] = arr[right]
        
    print(arr[0:left+1])
# removeDuplicates()

def mergeTwoSortedList():
    arr1 = [1,5,6,8]
    arr2 = [2,4,9,10]
    left, right = 0, 0
    l1 = []
    while(left<len(arr1) and right<len(arr2)):
        if(arr1[left] < arr2[right]):
            l1.append(arr1[left])
            left += 1
        else:
            l1.append(arr2[right])
            right += 1
            
    # if any element is left
    if(left<len(arr1)):
        l1.extend(arr1[left:])
    if(right<len(arr2)):
        l1.extend(arr2[right:])
    print(l1)

# mergeTwoSortedList()

def compareStrToRev():
    str1="abcde"
    str2="edcba"
    
    if len(str1)!=len(str2):
        print("Both strings have different length")
    
    left=0
    right=len(str1) - 1
    while(left<len(str1) and right>0):
        if str1[left]==str2[right]:
            left+=1
            right-=1
        else:
            print("reverse of string1 is not equal to string2")
            break
    else:
        print("revese of string1 is equal to string2")
# compareStrToRev()
        
def commonElements():
    arr1=[2,4,6]
    arr2=[1,2,3,4,5]
    i,j=0,0
    while(i<len(arr1)and j<len(arr2)):
        if arr1[i]==arr2[j]:
            print(arr1[i])
            i+=1
            j+=1
        elif arr1[i]>arr2[j]:
            j+=1
        else:
            i+=1
commonElements()

            