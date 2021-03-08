from functions import *

def encoder(msg, key):
    repeat = key[1]
    for i in range(0, repeat):
        msg = encrypt(msg, key)
    return msg

def decoder(msg, key):
    repeat = key[1]
    for i in range(0, repeat):
        msg = decrypt(msg, key)
    return msg

def test_enc_dec():
    key = [10, 852]
    msg = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
    msg_enc = encoder(msg, key)
    msg_dec = decoder(msg_enc, key)
    print("========================================")
    print("test_enc_dec")
    print("key: " + str(key))
    print("Input msg: " + msg)
    print("encrypted msg: " + msg_enc)
    print("decrypted msg: " + msg_dec)
    print("Is decrypted msg same as input? " + str(msg == msg_dec))

def test_hw_test1():
    key = [4, 5]
    msg = "CRYPTOLOGY IS THE PRACTICE AND STUDY OF TECHNIQUES FOR SECURE COMMUNICATION IN THE PRESENCE OF THIRD PARTIES CALLED ADVERSARIES"
    msg_enc = encoder(msg, key)
    print("========================================")
    print("test_hw_test1")
    print("key: " + str(key))
    print("Input msg: " + msg)
    print("encrypted msg: " + msg_enc)

def test_hw_test2():
    key = [3, 3]
    msg = "TAOTINEN KAT I ODIOAEI OHHLSCTE TTETOEL BI IHI GAO   EPSEA TO SS  EEK  ELRCPTSIY EANRPHMCYEK E CREAAIEJURTE  IEASHI MA DRN RH  AUWTA RF EFTFHENTPSF Q   TAILB E TTECAPMSIYIY SRPURNTBL YCL OANAO  E  TVREAOSHOTTNULSRHK"
    msg_dec = decoder(msg, key)
    print("========================================")
    print("test_hw_test2")
    print("key: " + str(key))
    print("Input msg: " + msg)
    print("decrypted msg: " + msg_dec)
    

if __name__ == "__main__":
    test_enc_dec()
    test_hw_test1()
    test_hw_test2()
