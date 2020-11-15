def main():
    #ask user how many Numbers they want in Array/Target Sum
    print("How large do you want the subset to be?" + "\n"
          "Input: ")
    N = int(input())

    print("Please Input {} numbers: ".format(N))
    #initialize arrays
    S = [0]*N
    X = [0]*N
    
    for i in range(0,N):
        S[i] = int(input())

    print("Please Input Target Sum: ")
    T = int(input())

    

    #subsetSum([3,5,6,1,2],[0,0,0,0,0],0,8,N)
    print(subsetSum(S,X,0,T,N,[]))

def feasible(S,X,T,r):
    Sum = 0
    for i in range(0,r+1):
        if X[i] == 1:
            Sum += S[i]
    if Sum > T:
        return False
    return True


def subsetSum(S,X,index,Target,N,RES):  
    Sum = 0
    res = []
    
    #iterate through X to get Sum of S
    for num in range(0,N):
        if X[num] == 1:
            Sum += S[num]
            res.append(S[num])
    
    if Sum == Target:
        if res not in RES:
            RES.append(res)
            print(res)
        X[index-1] = 0

    #base case
    if index == N:
        return

    #Mark index as Valid, then check whether it can be used further
    X[index] = 1
    if feasible(S,X,Target,index) == True:
        subsetSum(S,X,index+1,Target,N,RES)

    X[index] = 0
    subsetSum(S,X,index+1,Target,N,RES)
    

    
if __name__ == "__main__":
    main()
