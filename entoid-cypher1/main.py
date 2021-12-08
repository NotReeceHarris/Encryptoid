import random
import hashlib

'''
  ____|   \  |   ___|   _ \ \ \   /   _ \ __ __|  _ \ _ _|  __ \  
  __|      \ |  |      |   | \   /   |   |   |   |   |  |   |   | 
  |      |\  |  |      __ <     |    ___/    |   |   |  |   |   | 
 _____| _| \_| \____| _| \_\   _|   _|      _|  \___/ ___| ____/  
                                                                  
Name            : entoid-cypher1
Type            : Cypher Shuffle
Security Rating : 2
'''

def shiftGen(key, len):
    shiftValue = []
    for i in range(len):
        for x in key.hexdigest():
            random.seed(f'{x}{i}{len}')
            shiftValue.append([random.randint( 0, ( round(len - 1) ) ), random.randint( 0, ( round(len - 1) ) ) ])
            
    return shiftValue

def keyGen(key):
    random.seed(key)
    return hashlib.sha256( f'{ hashlib.sha256(key.encode()).hexdigest() }{ hashlib.sha256(random.randbytes(10)).hexdigest() }'.encode() )

def fillerGen(content, shift):
    fillerAmount =  round((len(content) / 2) * 10)
    filler = []
    for x in range(fillerAmount):
        filler.append(random.randbytes(1))
    
    return filler


def ecr(key, content):

    fillerLen = round((len(content) / 2) * 10)
    cypherSize = len(str(len(content) + fillerLen)) + len(content) + fillerLen
    key = keyGen(key)

    cypherShift = shiftGen(key, cypherSize)
    cypherContent = [x.encode('utf-8') for x in content]
    cypherFiller = fillerGen(content, cypherShift)

    random.seed(hashlib.sha256(str(cypherShift).encode()).hexdigest())
    print(f'''
    // Encryption
    cypherShift : {hashlib.sha256(str(cypherShift).encode()).hexdigest()} : {random.randint(-1000,1000)}
    ''')

    preShift = [x for x in str(len(cypherContent))] + cypherContent + cypherFiller

    for x in cypherShift:

            i = preShift[x[0]]
            y = preShift[x[1]]
            preShift[x[0]] = y
            preShift[x[1]] = i
    
    return preShift

def dcr(key, content):

    cypherSize = len(content)
    key = keyGen(key)

    cypherShift = shiftGen(key, cypherSize)

    random.seed(hashlib.sha256(str(cypherShift).encode()).hexdigest())
    print(f'''
    // Decryption
    cypherShift : {hashlib.sha256(str(cypherShift).encode()).hexdigest()} : {random.randint(-1000,1000)}
    ''')

    cypherShift.reverse()
    preShift = content

    for x in cypherShift:

        i = preShift[x[0]]
        y = preShift[x[1]]
        preShift[x[0]] = y
        preShift[x[1]] = i

    messageLength = ''

    for x in range(len(preShift)):
        
        if type(preShift[x]) != type(bytes()):
            messageLength += preShift[x]
        else:
            break
    
    message = ''

    for x in range(int(messageLength)+3):
        try:
            message += str(preShift[x].decode())
        except:
            pass
    

    
    return message



if __name__ == '__main__':

    psw='abc123#'

    a = ecr(psw, 'Hello World')
    b = dcr(psw, a)
    print(b)
