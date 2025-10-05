import os
import sys

def main():
    input_value = os.getenv("MY_VARIABLE", "")
    input_string = os.getenv("MY_STRING")
    if len(sys.argv) > 2:
        input_value = sys.argv[1]
        input_string = sys.argv[2]

    result = f"Hello, the input is: {input_value} and the string is: {input_string}"

    print(result)
    print("This is a test print statement.")
    
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    main()
