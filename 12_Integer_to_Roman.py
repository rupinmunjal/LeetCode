def intToRoman(num):
    # Mapping of integers to Roman numerals
    values = [
        1000, 900, 500, 400, 
        100, 90, 50, 40, 
        10, 9, 5, 4, 
        1
    ]
    symbols = [
        "M", "CM", "D", "CD", 
        "C", "XC", "L", "XL", 
        "X", "IX", "V", "IV", 
        "I"
    ]
    
    roman = ""
    
    # Loop through each symbol, reducing the number as we go
    for i in range(len(values)):
        while num >= values[i]:
            roman += symbols[i]
            num -= values[i]
    
    return roman
num = 3749
print(intToRoman(num))