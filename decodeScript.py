import gzip,base64,sys

def encode(codeStr):
    try:
        strBytes = codeStr.encode('ascii')
        encodedStr = base64.b64encode(strBytes)
        compressedStr = gzip.compress(encodedStr)
        compressedStrEncoded = base64.b64encode(compressedStr)
        compressedStrEncoded = compressedStrEncoded.decode('ascii')
        print(compressedStrEncoded)
    except:
        print('invalid codeString')

def decode(compressedStr):
    try:
        base64EncodeStr = compressedStr
        decodeToBytesStg = base64EncodeStr.encode('ascii')
        bytesDecoded = base64.b64decode(decodeToBytesStg)
        decompressedStr = gzip.decompress(bytesDecoded).decode('ascii')
        decodeStrTmp = decompressedStr.encode('ascii')
        finalCode = base64.b64decode(decodeStrTmp).decode('ascii')
        print(finalCode)
    except:
        print('invalid compressedString')

if(sys.argv[1] == 'encode'):
    encode(sys.argv[2])
elif(sys.argv[1] == 'decode'):
    decode(sys.argv[2])
else:
    raise Exception("invalid method")
