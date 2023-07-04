import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 8,
    "B": 6,
    "C": 4,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter The Deposit Amount: $")
        if(amount.isdigit()):
            amount = int(amount)

            if amount > 0:
                break
            else:
                print ("Deposit Amount Cannot Be Negative. Enter Again.")
        else:
            print(f"Value '{amount}' is not a valid number! Enter Again.")

    return amount

def get_number_of_lines():

    while True:
        lines = input("Enter The Number of Lines (1 - " + str(MAX_LINES) + ")? ")
        if(lines.isdigit()):
            lines = int(lines)

            if 0 <= lines <= MAX_LINES:
                break
            else:
                print ("Enter Valid Number of Lines.")
        else:
            print(f"Value '{lines}' is not a valid number! Enter Again.")

    return lines

def get_bet():
    while True:
        amount = input("Enter Your Bet For Each Line: $")
        if(amount.isdigit()):
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print (f"Bet Should be Between ${MIN_BET} - ${MAX_BET}")
        else:
            print(f"Value '{amount}' is not a valid number! Enter Again.")

    return amount

def spin(balance):
    lines = get_number_of_lines()


    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Balance Low!!!\nYour Current Balance = {balance}")
        else:
            break

    total_bet = lines * bet

    print(f"You're Betting ${bet} on {lines} line(s).\nYour Total Bet is ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)

    print(f"You Won ${winnings}")
    print(f"Winning Lines: ", *winning_lines)

    return winnings - total_bet

def main():

    balance = deposit()
    while True:
        print(f"Current Balance: ${balance}")
        answer = input("Press Enter to Spin (or q to quit): ")

        if answer == "q":
            break
        balance += spin(balance)

    print(f"You Left With ${balance}")

main()