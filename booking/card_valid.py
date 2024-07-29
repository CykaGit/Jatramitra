def valid(number):
    # Remove any spaces or hyphens from the input
    number = number.replace(" ", "").replace("-", "")

    # Check if the input consists only of digits and has a length between 13 and 19
    if not number.isdigit() or not 13 <= len(number) <= 19:
        return False

    # Apply Luhn algorithm
    total = 0
    reverse_number = number[::-1]
    for i, digit in enumerate(reverse_number):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    # Check if the total is divisible by 10
    return total % 10 == 0
