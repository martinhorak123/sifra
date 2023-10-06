def encode(key, message):
    key = ord(key)
    message = ord(message)
    result = key 
    return ""

def decode(key, message):
    return encode(key, message)

znak = 'a'
cislo_unicode = ord(znak)
binarni_reprezentace = bin(cislo_unicode)
binarni_reprezentace = binarni_reprezentace[2:]
print(binarni_reprezentace)

znak = 'b'
cislo_unicode = ord(znak)
binarni_reprezentace2 = bin(cislo_unicode)
binarni_reprezentace2 = binarni_reprezentace2[2:]
print(binarni_reprezentace2)

vysledek =binarni_reprezentace ^ binarni_reprezentace2
print(vysledek)



