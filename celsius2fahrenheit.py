import re

def convert_temperature(input_str):
    match = re.match(r'^([-+]?[0-9]+)([CF])$', input_str)

    if match:
        input_num = int(match.group(1))
        temp_type = match.group(2)

        if temp_type == "C":
            celsius = input_num
            fahrenheit = (celsius * 9 / 5) + 32
        else:
            fahrenheit = input_num
            celsius = (fahrenheit - 32) * 5 / 9

        return f"{celsius:.2f} C is {fahrenheit:.2f} F"
    else:
        return f'Expecting a number followed by "C" or "F", so I don\'t understand "{input_str}".'

def main():
    print("Enter a temperature (e.g., 32F, 100C):")
    input_str = input().strip()
    result = convert_temperature(input_str)
    print(result)

if __name__ == "__main__":
    main()
