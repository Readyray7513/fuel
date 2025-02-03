def convert(fraction):
    try:
        x, y = fraction.strip().split("/")
        x = int(x)
        y = int(y)

        # Validate the fraction
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        
        percentage = round((x / y) * 100)
        return percentage

    except (ValueError, ZeroDivisionError):
        raise



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"



def main():
    while True:
        try:
            fraction = input("Fraction: ").strip()
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)
            break
        except (ValueError):
            print(ValueError)
        except ZeroDivisionError :
            print(ZeroDivisionError)
            break



if __name__ == "__main__":
    main()