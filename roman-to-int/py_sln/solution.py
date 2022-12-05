


def romanToInt(s)->str:
    final_value = 0
    myHashTable = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    position = 0
    for i in range(len(s)):
        if( position<len(s) and s[position] == 'I' and s[position+1] == 'V'):
            final_value = final_value + 4
            position = position + 2
        elif(position<len(s) and s[position] == 'I' and s[position+1] == 'X'):
            final_value = final_value + 9
            position = position + 2
        elif(position<len(s) and s[position] == 'X' and s[position+1] == 'L'):
            final_value = final_value + 40
            position = position + 2
        elif(position<len(s) and s[position] == 'X' and s[position+1] == 'C'):
            final_value = final_value + 90
            position = position + 2
        elif(position<len(s) and s[position] == 'C' and s[position+1] == 'D'):
            final_value = final_value + 400
            position = position + 2
        elif(position<len(s) and s[position] == 'C' and s[position+1] == "M"):
            final_value = final_value + 900
            position = position + 2
        else:
            final_value = final_value + myHashTable[s[position]]
            
    return final_value