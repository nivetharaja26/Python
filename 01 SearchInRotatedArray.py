#Search in Rotated array 

nums=[]
n=int(input("Enter number of elements : "))

for i in range (0,n):
    nums.append(int(input("ele : ")))

k=int(input("Rotate : "))

new=[]

new=nums[k:]+nums[0:k]

target=int(input("target  : "))

'''
pos=new.index(target)

if pos!=-1:
    print(pos)
else:
    print(-1)
'''
pos=-1
def search(num,tar):
    l=0
    u=len(num)-1
    
    while l<=u:
        mid=(l+u)//2
        print("mid" , mid)
        if num[mid]==tar:
            globals()['pos']=mid
            return True
        
        else:
            if num[mid]<tar:
                l=mid
            else:
                u=mid
                

result = search(new,target)

if result==True:
    print(pos)
else:
    print("-1")

                
                
