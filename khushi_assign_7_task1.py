def encrypt_message(text, shift):
    
    letter_list = []
    
    for char in text:
       
        asc = ord(char)
        if char.isupper():
            asc = asc + shift
           
        letter_list.append(chr(asc))
        
 
    return "" .join(letter_list)


output = encrypt_message("DEVDOOT", 3)
print("Encrypted Result:", output)