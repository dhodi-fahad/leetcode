


def romanToInt(s)->str:
    value = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    
    res = 0
    i = 0
 
    while (i < len( s)):
 
        # Getting value of symbol s[i]
        s1 = value[s[i]]
 
        if (i + 1 < len( s)):
 
            # Getting value of symbol s[i + 1]
            s2 = value[s[i + 1]]
 
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res


    # while position<i:
    #     if((position+1)<i):
    #         if(s[position] == 'I' and s[position+1] == 'V'):
    #             final_value = final_value + 4
    #             position = position + 2
    #         elif(s[position] == 'I' and s[position+1] == 'X'):
    #             final_value = final_value + 9
    #             position = position + 2
    #         elif(s[position] == 'X' and s[position+1] == 'L'):
    #             final_value = final_value + 40
    #             position = position + 2
    #         elif(s[position] == 'X' and s[position+1] == 'C'):
    #             final_value = final_value + 90
    #             position = position + 2
    #         elif(s[position] == 'C' and s[position+1] == 'D'):
    #             final_value = final_value + 400
    #             position = position + 2
    #         elif(s[position] == 'C' and s[position+1] == "M"):
    #             final_value = final_value + 900
    #             position = position + 2
    #     else:
    #         final_value = final_value + myHashTable[s[position]]
    #         position = position + 1
            
    # return final_value