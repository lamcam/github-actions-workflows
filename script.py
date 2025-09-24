import os
import sys

def main():
    input_value = os.getenv("MY_VARIABLE", "")
    if len(sys.argv) > 1:
        input_value = sys.argv[1]

    result = f"Hello, the input is: {input_value}"

    print(result)
    
    
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    main()
