def validate(msg, key):
    DEPTH = key[0]
    REPEAT = key[1]
    ErrMsg = 0
    if DEPTH <= 1:
        print("Depth needs to meet the condition:  DEPTH = integer, DEPTH >=2")
        ErrMsg += 1
    if REPEAT < 1:
        print("Repeat needs to meet the condition:  REPEAT = integer, REPEAT >=1")
        ErrMsg += 1
    N = len(msg)
    if N <= 1:
        print("THe message needs to be longer than 1 character")
        ErrMsg += 1
    if ErrMsg > 0:
        exit(-1)
    return DEPTH, N


def getTable(row, col):
    table = []
    for r in range(0, row):
        temp = []
        for c in range(0, col):
            temp.append('')
        table.append(temp)
    return table

def getNextRow(idx, DEPTH):
    temp = idx/(DEPTH-1)
    return (DEPTH-1) - (idx%(DEPTH-1)) if temp%2 ==1 else idx%(DEPTH-1)

def encrypt(msg, key):
    DEPTH, N = validate(msg, key)

    table = getTable(DEPTH, N)
    for idx in range (0, N):
        r = getNextRow(idx, DEPTH)
        table[r][idx] = msg[idx]

    msg_enc = ''
    for r in range (0, DEPTH):
        msg_enc += ''.join(table[r])
    return msg_enc

def decrypt(msg, key):
    DEPTH, N = validate(msg, key)

    table = getTable(DEPTH, N)
    for idx in range (0, N):
        r = getNextRow(idx, DEPTH)
        table[r][idx] = idx
    
    msg_table = getTable(DEPTH, N)
    
    idx = 0
    for i in range(0, DEPTH):
        row = table[i]
        for col in range(0, N):
            char = row[col]
            if (char != ''):
                msg_table[i][col] = msg[idx]
                idx += 1
    
    msg_dec = ''
    for idx in range (0, N):
        r = getNextRow(idx, DEPTH)
        msg_dec += msg_table[r][idx]

    return msg_dec


if __name__ == "__main__":
    d = 3
    r = 1
    key = [d, r]
    msg = "0123456789"
    msg_enc = encrypt(msg, key)
    print(msg_enc)
    msg_dec = decrypt(msg_enc, key)
    print(msg_dec)
