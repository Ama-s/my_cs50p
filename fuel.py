def main():
    while True:
        fraction_gauge = input("Fraction: ")
        try:
            percentage = convert_gauge(fraction_gauge)
            break
        except (ValueError, ZeroDivisionError):
            pass
    if percentage <= 1:
        print ("E")
    elif percentage >= 99:
        print ("F")
    else:
        print(f"{percentage}" + "%")


def convert_gauge(gauge):
    x,y = gauge.split("/")
    numerator = int (x)
    denominator = int (y)
    if numerator <= denominator:
        z = round((numerator/denominator) * 100)
        return z
    else:
        raise ValueError
main()
