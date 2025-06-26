def calculate(first, second, operator):
    match operator:
        case '+': return first + second
        case '-': return first - second
        case '*': return first * second
        case "/": return first / second
        case '//': return first // second
        case '%': return first % second
        case '**': return first ** second


first_num = 5
second_num = 2
for char in ["+", "-", "/", "//", "%", "**"]:
    calculated = float(calculate(first_num, second_num, char))
    print(f'==> {first_num} {char} {second_num} = {calculated}')
    
