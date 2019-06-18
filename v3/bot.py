#Import Modules


#Import Save File
with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Documents\GitHub\factorAlgorithm\v2\ResultsBackup.txt') as f:
    results=f.readlines()

results = [x.strip() for x in results]
number_of_results=len(results)


#Find Current Number
current_result=results[-1]
current_number=current_result.split('-')[0].strip()

#Convert to Integer
current_number=int(current_number)


#Algorithim
k=1
consecutive_factors=False
while consecutive_factors==False:
    factors=[1] #1 is always a factor
    
    for i in range(2,(current_number)): #Test All Possible Numbers
        if current_number%i == 0: #Test if i is a factor of the current number
            factors.append(i) #If a factor then apppend to list of factors

    factors.append(current_number)
    
    
    #Check If Factors are consecutive
    consecutive_factors=True
    for j in range(1,(number_of_results+2)):
        if j in factors:
            pass
        else:
            consecutive_factors=False

    #Counter
    if k>=100:
        print(current_number)
        k=1
    else:
        k+=1
            
    if consecutive_factors==False:
        current_number+=1


if consecutive_factors==True:
    factor_string=','.join(str(factor) for factor in factors)
    new_result=f'{current_number} - {factor_string}'
    print(new_result)



#Add new result to results
results.append(new_result)


#Export Save File
with open(r'C:\Users\Isaac.LAPTOP-KA6VL0F5\Documents\GitHub\factorAlgorithm\v2\Results.txt','w') as f:
        for result in results:
            f.write(f"{result}\n")