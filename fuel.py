def main():
    while True:
        try:
            # Prompt user for input
            fuel = input("Type fuel status in fraction, X/Y format: ")

            # Split the input and convert to integers
            x, y = map(int, fuel.split("/"))

            # Check for invalid inputs
            if y == 0:
                print("Y cannot be zero. Please try again.")
                continue

            if x > y:
                print("X cannot be greater than Y. Please try again.")
                continue

            # Calculate the fuel percentage
            p = x / y

            # Determine the fuel status
            if p >= 0.99:
                print('F')  # Full
            elif p <= 0.1:
                print('E')  # Empty
            else:
                print(f"{round(p * 100)}%")  # Display percentage as a rounded integer
            break  # Exit the loop after valid input and output

        except ValueError:
            print("Invalid format. Please enter the fraction as X/Y where X and Y are integers.")

        except Exception as e:
            print(f"Unexpected error: {e}. Please enter the fraction in the correct format.")

main()



    

#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
#(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.



#Type 4/0 and press Enter. Your program should handle a ZeroDivisionError and prompt the user again.

#Type three/four and press Enter. Your program should handle a ValueError and prompt the user again.
#Type 1.5/3 and press Enter. Your program should handle a ValueError and prompt the user again.

#Type 5/4 and press Enter. Your program should prompt the user again.