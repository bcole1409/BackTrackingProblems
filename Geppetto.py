#Global Variable, return value of algorithm
Count = 1

##############################   Feasability FUNCTION   #####################
def isValid(Potential,Restrictions):
    #[1,2]
    for option in Restrictions:
        COUNTER = 0
        for choice in option:
            #tells us if restricted ingredient is used
            if Potential[choice-1] == 1:
                #If counter == 2, this tells us we found a mismatch and we should stop
                COUNTER += 1
                if COUNTER == 2:
                    return False
    return True
            
    

##############################   Backtracking FUNCTION   #####################
def Geppetto(Potential,Choice,N,Restrictions):
    global Count

    #Stop recusive Calls
    if Choice == N:
        return False
    
    #[1,0,0]
    Potential[Choice] = 1

    #check to see if combo is feasible
    if isValid(Potential,Restrictions) == True:
        Count += 1
        Geppetto(Potential,Choice+1,N,Restrictions)
        
    Potential[Choice] = 0

    Geppetto(Potential,Choice+1,N,Restrictions)

    #Finished our recursive calls
    return Count

 
##############################   MAIN FUNCTION   ###############################
def main():
    #N is the number of ingredients
    #M is the number of mismatches
    N,M = map(int, input().split())

    #Create List of Mismatches
    Mismatches = [0]*M
    #Create List of possible combonations
    Potential = [0]*N
    
    for i in range(0,M):
        in1,in2 = map(int, input().split())
        Mismatches[i] = [in1,in2]
    
    print(Geppetto(Potential,0,N,Mismatches))

if __name__ == "__main__":
    main()
