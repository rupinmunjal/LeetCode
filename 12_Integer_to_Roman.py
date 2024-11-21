def intToRoman(num):
    roman = ""
    arr = [int(x) for x in str(num)]

    while(len(arr) != 4):
        arr.insert(0, 0)

    # For arr[0]
    roman = arr[0] * "M"

    # For arr[1]
    if arr[1]>=5:
        if arr[1] == 9:
            roman += "CM"
        else:
            roman += "D"
            roman += (arr[1] - 5) * "C"
    else:
        if arr[1] == 4:
            roman += "CD"
        else:
            roman += (arr[1]) * "C"
    
    #For arr[2]
    if arr[2]>=5:
        if arr[2] == 9:
            roman += "XC"
        else:
            roman += "L"
            roman += (arr[2] - 5) * "X"
    else:
        if arr[2] == 4:
            roman += "XL"
        else:
            roman += (arr[2]) * "X"

    #For arr[3]
    if arr[3]>=5:
        if arr[3] == 9:
            roman += "IX"
        else:
            roman += "V"
            roman += (arr[3] - 5) * "I"
    else:
        if arr[3] == 4:
            roman += "IV"
        else:
            roman += (arr[3]) * "I"

    return roman