import numpy as np
import random

class Password :
    def __init__(self) -> None:
        pass

    MossCode = {
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--."'',
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--."
    }
    CeacerCodeMin = random.randint(1, 45)
    CeacerCodeMax = random.randint(1, 32)
    CeacerRecode = []

    # FUN 轉譯摩斯密碼
    def mos( s : str ) :
        s = s.upper()
        re = ''
        for i in s :
            try :
                re += Password.MossCode[i]
                re += " "
            except KeyError :
                re += i

        return re
    
    # FUN 轉譯 ascii
    def asc( s : str ) :
        re = ''
        for i in s :
            re += str(ord(i))
            re += " "

        return re
    
    # FUN 轉譯 str
    def unasc( s : str ) :
        s = s.split()
        re = ''
        for i in s :
            if i != " " :
                re += chr(int(i))
        
        return re
    
    # FUN 取因數
    def factor( num : int ) :
        i = 1
        re = np.array([]).reshape(0, 2)

        while i <= num :
            if num % i == 0 :
                s = np.array([int(i), int(num / i)]).reshape(1, 2)
                re = np.append(re, s, axis = 0)
            i += 1

        re = re.astype(int)
        if len(re)%2 == 0 :
            return re[ int( ( len(re)/2 ) - 1 ) ]
        else :
            return re[ int( ( len(re)/2 ) ) ]

    # FUN 轉譯 ascii 輸出 numpy 資料
    def npasc( s : str ) :
        s = Password.asc(s)
        s = np.array(s.split())
        re = s.reshape(Password.factor(len(s)))
        return re
    
    # FUN numpy 轉 str
    def nptostr( n : np.ndarray ) :
        n = n.reshape(-1, )
        re = ''
        for i in n :
            re += i
            re += " "
        return re
    
    # FUN numpy ascii 轉 中文
    def unnpasc( n : np.ndarray ) :
        n = Password.nptostr(n)
        return Password.unasc(n)
    
    # FUN 轉譯凱薩密碼
    def ceacer( s : str ) :
        s = Password.asc(s).split()
        re = []
        res = ''
        for i in s :
            if int(i) <= 80 :
                re.append( int(i) + Password.CeacerCodeMin )
                Password.CeacerRecode.append(0)
            else :
                re.append( int(i) - Password.CeacerCodeMax )
                Password.CeacerRecode.append(1)
        for i in re :
            res += chr(i)
        return  res
    
    # FUN 破譯凱薩密碼
    def unceacer( s : str ) :
        s = Password.asc(s).split()
        re = []
        res = ''
        for i, j in zip(s, Password.CeacerRecode) :
            if j == 1 :
                re.append( int(i) + Password.CeacerCodeMax )
            else :
                re.append( int(i) - Password.CeacerCodeMin )
        for i in re :
            res += chr(i)

        return res

    # FUN 柵欄加密
    def fence( s : str ) :
        s = Password.npasc(s).T
        return Password.unnpasc(s)