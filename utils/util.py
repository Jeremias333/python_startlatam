def yesorno(res):#variável irá retornar    
    if(res == 'sim' or res == 's' or res == 'yes' or res == 'y'):
        val = 1
    elif(res == 'nao' or res == 'n' or res == 'no'):
        val = 0
    else:
        val = "invalid"
    return val