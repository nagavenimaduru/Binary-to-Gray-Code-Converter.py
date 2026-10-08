print("Binary to Gray Code Converter")
print("-----------------------------")

binary = input("Enter a binary number: ")

# Validate binary input
if all(bit in "01" for bit in binary):
    
    gray = binary[0]

    for i in range(1, len(binary)):
        gray += str(int(binary[i - 1]) ^ int(binary[i]))

    print("\nResult:")
    print("Binary    :", binary)
    print("Gray Code :", gray)

else:
    print("Invalid input! Please enter only 0 and 1.")
