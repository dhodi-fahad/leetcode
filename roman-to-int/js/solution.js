/**
 * @param {string} s
 * @return {number}
 */
 function romanToInt(s) {
    // i, v5, x10, l50, c100, d500, m1000
    
    let myHashTable = {
        I:1,
        V:5,
        X:10,
        L:50,
        C:100,
        D:500,
        M:1000
    }
    let finalValue = 0
    for(let i=0;i<s.length; i++){
        if(s[i]==="I" && s[i+1]==="V"){
            finalValue+=4
            i++
        }else if(s[i]==="I" && s[i+1]==="X"){
            finalValue+=9
            i++
        }else if(s[i]==="X" && s[i+1]==="L"){
            finalValue+=40
            i++
        }else if(s[i]==="X" && s[i+1]==="C"){
            finalValue+=90
            i++
        }else if(s[i]==="C" && s[i+1]==="D"){
            finalValue+=400
            i++
        }else if(s[i]==="C" && s[i+1]==="M"){
            finalValue+=900
            i++
        }else{
            finalValue +=myHashTable[s[i]]
        }

    }

    return finalValue
    
};

module.exports = romanToInt;