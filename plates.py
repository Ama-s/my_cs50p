def main():
    plate = input("Plate: ")
    if is_valid(plate): #i.e if is_value returns true
        print("Valid")
    else:
        print("Invalid")

def startswith(plate_number):
    #to check if the first two characters of plate number starts with an alphabet
    #in irder to avoid indexing error, whereby the computer touches invalid ...
    #memory space, first check if the plate number is greater than two characters
    if len(plate_number) > 1:
        if plate_number[0].isalpha() and plate_number[1].isalpha():
            return True
    return False

def char_range(min_max):
    if 2 <= len(min_max) <= 6:
        return True
    return False

def endswith_digit(plate_number):
    #digit_count is to keep the index
    digit_count = 0
    for each in plate_number:
        if each.isdigit():
            #if the current char up to the last is digit, it meets d requirement
            if each != '0' and plate_number[digit_count: ].isdigit():
                return True
            return False
        digit_count += 1

def is_valid(s):
    #if startswith and char_range returns true after being called, then you execute
    if startswith(s) and char_range(s):
        #this
        if s.isalpha():
            return True
        elif s.isalnum():
            #if it's an alphanum, call the endswith_digit fxn which checks if...
            #....numbers are in between letters (i.e invalid)
            return endswith_digit(s)
    return False

main()
