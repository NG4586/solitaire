# Nathaniel Graves
import random
deck = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120,
        1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121,
        2, 12, 22, 32, 42, 52, 62, 72, 82, 92, 102, 112, 122,
        3, 13, 23, 33, 43, 53, 63, 73, 83, 93, 103, 113, 123]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
ranks = "A23456789TJQK"
suits = "♠♥♦♣"
playing = False
status = 0
def entry(low, high, end, message):
    global status
    reader = input(message)
    if len(reader) >= 4 and reader[:4].lower() == "menu":
        if playing and (len(reader) < 5 or reader[4] != "!"):
            reader = input("Return to the main menu? Any progress on the game will be lost. [y/n] ")
            if not reader[0].lower() == 'y':
                return entry(low, high, end, message)
        status = 0
        return "menu"
    if reader[:4].lower() == "quit":
        if playing and (len(reader) < 5 or reader[4] != "!"):
            reader = input("Exit the program? Any progress on the game will be lost. [y/n] ")
            if not reader[0].lower() == 'y':
                return entry(low, high, end, message)
        status = -1
        return "quit"
    if end < 2:
        good = not reader == ""
        for n in reader:
            if n not in numbers:
                good = False
                break
        if good and int(reader) >= low and int(reader) <= high:
            return reader
        print("\nInput an integer between ", low, " and ", high, ".\n", sep="")
    else:
        if len(reader) > 1 and reader[0].upper() in letters[:end]:
            reader = reader[0].upper() + reader[1:]
            number = reader[1:]
            good = True
            for n in number:
                if n not in numbers:
                    good = False
                    break
            if good and int(number) >= low and int(number) <= high:
                return reader
        print("\nInput a letter between A and ", letters[end - 1], sep = "", end = " ")
        print("followed by an integer between ", low, " and ", high, ".\n", sep = "")
    return entry(low, high, end, message)
def shuffle():
    global deck
    empty = [True, True, True, True, True, True, True, True, True, True, True, True, True,
             True, True, True, True, True, True, True, True, True, True, True, True, True,
             True, True, True, True, True, True, True, True, True, True, True, True, True,
             True, True, True, True, True, True, True, True, True, True, True, True, True]
    for n in range(52):
        place = random.randint(0, 51)
        while not empty[place]:
            place = random.randint(0, 51)
        deck[place] = n % 13 * 10 + int(n / 13)
        empty[place] = False
def minesweeper():
    def output():
        print(end = "\n   ")
        for n in range(len(grid[0])):
            print(end = letters[n] + " ")
        for y in range(len(grid)):
            print()
            if y < 9:
                print(end = " ")
            print(end = str(y + 1) + "|")
            for x in range(len(grid[y])):
                print(end = grid[y][x][0] + "|")
        print("\n")
    def number(x, y):
        counter = 0
        if y > 0:
            if x > 0 and grid[y - 1][x - 1][1]:
                counter += 1
            if x < len(grid[y]) - 1 and grid[y - 1][x + 1][1]:
                counter += 1
            if grid[y - 1][x][1]:
                counter += 1
        if y < len(grid) - 1:
            if x > 0 and grid[y + 1][x - 1][1]:
                counter += 1
            if x < len(grid[y]) - 1 and grid[y + 1][x + 1][1]:
                counter += 1
            if grid[y + 1][x][1]:
                counter += 1
        if x > 0 and grid[y][x - 1][1]:
            counter += 1
        if x < len(grid[y]) - 1 and grid[y][x + 1][1]:
            counter += 1
        grid[y][x][0] = str(counter)
        if counter == 0:
            if y > 0:
                if x > 0 and grid[y - 1][x - 1][0] == "_":
                    number(x - 1, y - 1)
                if x < len(grid[y]) - 1 and grid[y - 1][x + 1][0] == "_":
                    number(x + 1, y - 1)
                if grid[y - 1][x][0] == "_":
                    number(x, y - 1)
            if y < len(grid) - 1:
                if x > 0 and grid[y + 1][x - 1][0] == "_":
                    number(x - 1, y + 1)
                if x < len(grid[y]) - 1 and grid[y + 1][x + 1][0] == "_":
                    number(x + 1, y + 1)
                if grid[y + 1][x][0] == "_":
                    number(x, y + 1)
            if x > 0 and grid[y][x - 1][0] == "_":
                number(x - 1, y)
            if x < len(grid[y]) - 1 and grid[y][x + 1][0] == "_":
                number(x + 1, y)
    grid = []
    response = entry(2, 26, 0, "Enter grid length > ")
    if response == "menu" or response == "quit":
        return
    length = int(response)
    response = entry(2, 99, 0, "Enter grid height > ")
    if response == "menu" or response == "quit":
        return
    height = int(response)
    response = entry(1, length * height - 1, 0, "Enter number of mines > ")
    if response == "menu" or response == "quit":
        return
    mines = int(response)
    for y in range(height):
        grid.append([])
        for x in range(length):
            grid[y].append(["_", False])
    for n in range(mines):
        if n >= len(grid) * len(grid[0]):
            break
        while True:
            y = random.randint(0, len(grid) - 1)
            x = random.randint(0, len(grid[y]) - 1)
            if not grid[y][x][1]:
                grid[y][x][1] = True
                break
    output()
    response = entry(1, height, length, "Enter search coordinates > ")
    if response == "menu" or response == "quit":
        return
    search = response
    y = int(search[1:]) - 1
    x = 0
    for n in range(len(letters)):
        if letters[n] == search[0]:
            x = n
            break
    finished = False
    while not grid[y][x][1]:
        number(x, y)
        finished = True
        for n in grid:
            for m in n:
                if m == ["_", False]:
                    finished = False
                    break
        if finished:
            break
        output()
        response = entry(1, height, length, "Enter search coordinates > ")
        if response == "menu" or response == "quit":
            return
        search = response
        y = int(search[1:]) - 1
        for n in range(len(letters)):
            if letters[n] == search[0]:
                x = n
                break
    for n in range(len(grid)):
        for m in range(len(grid[n])):
            if grid[n][m][1]:
                if finished:
                    grid[n][m][0] = "☺"
                else:
                    grid[n][m][0] = "X"
    output()
    return
def solitaire():
    def output():
        print(end = " ___  ")
        if table[0][0] < 0:
            print(end = "       ")
        elif table[0][1] < 0:
            print(end = "___    ")
        elif table[0][2] < 0:
            print(end = "_ ___  ")
        else:
            print(end = "_ _ ___")
        print(end = "   ___  ___  ___  ___ \n|")
        if table[8][0] < 0:
            print(end = "   ")
        else:
            print(end = "  X")
        print(end = "|")
        if table[0][0] > -1:
            if table[0][1] > -1:
                if table[0][2] > -1:
                    print(end = "|" + suits[table[0][0] % 10] + "|")
                    print(end = suits[table[0][1] % 10] + "|" + suits[table[0][2] % 10] + "  |")
                else:
                    print(end = "|" + suits[table[0][0] % 10] + "|" + suits[table[0][1] % 10] + "  |  ")
            else:
                print(end = "|" + suits[table[0][0] % 10] + "  |    ")
        else:
            print(end = "         ")
        found = ["|   ||   ||   ||   |", "|   ||   ||   ||   |", "|   ||   ||   ||   |",
                  "", "", "", "", "", "", "", "", "", "", "", "", ""]
        for n in range(4):
            if table[n + 16][0] > -1:
                found[0] = found[0][:n * 5 + 1] + suits[n] + found[0][n * 5 + 2:]
                if table[n + 16][1] > -1:
                    found[0] = found[0][:n * 5 + 2] + "A" + found[0][n * 5 + 3:]
                    found[1] = found[1][:n * 5 + 1] + suits[n] + found[1][n * 5 + 2:]
                    if table[n + 16][2] > -1:
                        found[1] = found[1][:n * 5 + 2] + "2‾" + found[1][n * 5 + 4:]
                        found[2] = found[2][:n * 5 + 1] + suits[n] + found[2][n * 5 + 2:]
                        if table[n + 16][3] > -1:
                            found[2] = found[2][:n * 5 + 2] + "3‾" + found[2][n * 5 + 4:]
                        else:
                            found[2] = found[2][:n * 5 + 2] + "‾‾" + found[2][n * 5 + 4:]
                    else:
                        found[1] = found[1][:n * 5 + 2] + "‾‾" + found[1][n * 5 + 4:]
                        found[2] = found[2][:n * 5 + 2] + "2" + found[2][n * 5 + 3:]
                else:
                    found[1] = found[1][:n * 5 + 2] + "A" + found[1][n * 5 + 3:]
                    found[2] = found[2][:n * 5 + 3] + suits[n] + found[2][n * 5 + 4:]
        for n in range(3, 16):
            for m in range(4):
                if table[m + 16][n - 3] > -1:
                    if table[m + 16][n - 2] > -1:
                        found[n] += "|"
                        if table[m + 16][n - 1] > -1:
                            if table[m + 16][n] > -1:
                                if table[m + 16][n + 1] > -1:
                                    found[n] += suits[m] + ranks[n] + "‾"
                                else:
                                    found[n] += suits[m] + "‾‾"
                            else:
                                found[n] += " " + ranks[n - 1] + " "
                        else:
                            found[n] += "  " + suits[m]
                        found[n] += "|"
                    else:
                        found[n] += " ‾‾‾ "
                elif n > 3:
                    found[n] += "     "
                else:
                    found[n] += " ‾‾‾ "
        print(end = " " + found[0] + "\n|")
        if table[8][0] < 0:
            print(end = "   ")
        else:
            print(end = " X ")
        print(end = "|")
        if table[0][0] > -1:
            if table[0][1] > -1:
                if table[0][2] > -1:
                    print(end = "|" + ranks[int(table[0][0] / 10)] + "|")
                    print(end = ranks[int(table[0][1] / 10)] + "| " + ranks[int(table[0][2] / 10)] + " |")
                else:
                    print(end = "|" + ranks[int(table[0][0] / 10)] + "| " + ranks[int(table[0][1] / 10)] + " |  ")
            else:
                print(end = "| " + ranks[int(table[0][0] / 10)] + " |    ")
        else:
            print(end = "         ")
        print(end = " " + found[1] + "\n|")
        if table[8][0] < 0:
            print(end = "   ")
        else:
            print(end = "X  ")
        print(end = "|")
        if table[0][0] > -1:
            if table[0][1] > -1:
                if table[0][2] > -1:
                    print(end = "| | |  " + suits[table[0][2] % 10] + "|")
                else:
                    print(end = "| |  " + suits[table[0][1] % 10] + "|  ")
            else:
                print(end = "|  " + suits[table[0][0] % 10] + "|    ")
        else:
            print(end = "         ")
        print(end = " " + found[2] + "\n ‾‾‾  ")
        if table[0][0] < 0:
            print(end = "       ")
        elif table[0][1] < 0:
            print(end = "‾‾‾    ")
        elif table[0][2] < 0:
            print(end = "‾ ‾‾‾  ")
        else:
            print(end = "‾ ‾ ‾‾‾")
        print(end = "  ")
        for n in range(3, 16):
            if n > 3:
                print(end = "   ")
            print(found[n])
            if n < 15:
                print(end = "            ")
        print("\n ___  ___  ___  ___  ___  ___  ___ ")
        for n in range(22):
            for m in range(1, 8):
                if table[m][0] < 0:
                    if n > 3:
                        print(end = "     ")
                    elif n > 2:
                        print(end = " ‾‾‾ ")
                    else:
                        print(end = "|   |")
                elif n > 12:
                    if table[m][n - 3] < 0:
                        print(end = "     ")
                    elif table[m][n - 2] < 0:
                        print(end = " ‾‾‾ ")
                    elif table[m][n - 1] < 0:
                        print(end = "|  " + suits[table[m][n - 2] % 10] + "|")
                    elif table[m][n] < 0:
                        print(end = "| " + ranks[int(table[m][n - 1] / 10)] + " |")
                    elif table[m][n + 1] < 0:
                        print(end = "|" + suits[table[m][n] % 10] + "‾‾|")
                    else:
                        print(end = "|" + suits[table[m][n] % 10] + ranks[int(table[m][n] / 10)] + "‾|")
                elif table[m][n + 1] < 0:
                    if table[m][n] < 0:
                        if n > 2 and table[m][n - 3] < 0:
                            print(end = "     ")
                        elif n > 1 and table[m][n - 2] < 0:
                            print(end = " ‾‾‾ ")
                        elif n > 0 and table[m][n - 1] < 0:
                            print(end = "|  " + suits[table[m][n - 2] % 10] + "|")
                        elif table[m][n] < 0:
                            print(end = "| " + ranks[int(table[m][n - 1] / 10)] + " |")
                        else:
                            print(end = "|" + suits[table[m][n - 1] % 10] + "‾‾|")
                    elif table[20][m - 1] > n:
                        if n == 0:
                            print(end = "|  ")
                        else:
                            print(end = "|‾‾")
                        print(end = "X|")
                    else:
                        print(end = "|" + suits[table[m][n] % 10])
                        if n == 0:
                            print(end = "  |")
                        else:
                            print(end = "‾‾|")
                elif table[20][m - 1] > n:
                    if n == 0:
                        print(end = "|  ")
                    else:
                        print(end = "|‾‾")
                    print(end = "X|")
                else:
                    print(end = "|" + suits[table[m][n] % 10] + ranks[int(table[m][n] / 10)])
                    if n == 0:
                        print(end = " |")
                    else:
                        print(end = "‾|")
            print()
    shuffle()
    table = [[-1, -1, -1],
             [deck[0], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1],
             [deck[1], deck[2], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1],
             [deck[3], deck[4], deck[5], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1],
             [deck[6], deck[7], deck[8], deck[9], -1, -1, -1, -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1],
             [deck[10], deck[11], deck[12], deck[13], deck[14], -1, -1, -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [deck[15], deck[16], deck[17], deck[18], deck[19], deck[20], -1, -1, -1, -1,
              -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [deck[21], deck[22], deck[23], deck[24], deck[25], deck[26], deck[27], -1, -1,
              -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [deck[28], deck[29], deck[30]], [deck[31], deck[32], deck[33]],
             [deck[34], deck[35], deck[36]], [deck[37], deck[38], deck[39]],
             [deck[40], deck[41], deck[42]], [deck[43], deck[44], deck[45]],
             [deck[46], deck[47], deck[48]], [deck[49], deck[50], deck[51]],
             [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [0, 1, 2, 3, 4, 5, 6]]
    while True:
        output()
        if table[16][12] > -1 and table[17][12] > -1 and table[18][12] > -1 and table[19][12] > -1:
            print("\nYou win!\n")
            return
        response = entry(1, 4, 0, "1: Draw from the deck\n2: Take the top card from the draw pile\n"
                                  "3: Move a stack\n4: Move a card to the foundation\n\n> ")
        if response == "menu" or response == "quit":
            return
        if response == "1":
            if table[8][0] < 0:
                print("\nThe deck is empty.\n")
            else:
                hole = [0, -1]
                for n in range(8, 15):
                    if table[n + 1][0] > -1 and table[n][0] > -1:
                        if table[n][2] < 0:
                            hole[1] = n
                            hole[0] += 1
                            if table[n][1] < 0:
                                hole[0] += 1
                for n in range(15, 7, -1):
                    if table[n][0] > -1:
                        holder = table[0]
                        table[0] = table[n]
                        table[n] = holder
                        if hole[0] > 0 and (table[n][0] > -1 and table[n][2] < 0):
                            if table[n][1] < 0:
                                hole.append(2)
                            else:
                                hole.append(1)
                            for m in range(n - 1, hole[1], -1):
                                table[m + 1][2] = table[m][2]
                                table[m][2] = -1
                                if hole[2] > 1:
                                    table[m + 1][1] = table[m][1]
                                    table[m][1] = -1
                            if hole[0] < 2 and hole[2] < 2:
                                table[hole[1] + 1][2] = table[hole[1]][1]
                                table[hole[1]][1] = -1
                            else:
                                if hole[0] < 2:
                                    table[hole[1] + 1][1] = table[hole[1]][0]
                                    table[hole[1] + 1][2] = table[hole[1]][1]
                                else:
                                    table[hole[1] + 1][2] = table[hole[1]][0]
                                table[hole[1]] = [-1, -1, -1]
                                for l in range(hole[1], 15):
                                    table[l] = table[l + 1]
                                    table[l + 1] = [-1, -1, -1]
                        break
                for n in range(9, 16):
                    if table[n][0] < 0:
                        if table[n - 1][0] > -1:
                            holder = [table[8], table[9]]
                            for m in range(9, n):
                                table[m] = holder[0]
                                holder[0] = holder[1]
                                holder[1] = table[m + 1]
                            table[8] = holder[0]
                        break
        elif response == "2":
            if table[0][0] < 0:
                print("\nThe draw pile is empty.\n")
            else:
                if table[0][1] < 0:
                    card = table[0][0]
                elif table[0][2] < 0:
                    card = table[0][1]
                else:
                    card = table[0][2]
                response = entry(1, 7, 0, "\nChoose which stack to place the card upon. Stacks are numbered"
                                          " from left to right, starting with 1.\n\n> ")
                if response == "menu" or response == "quit":
                    return
                stack = int(response)
                above = table[stack][0]
                if above < 0:
                    if int(card / 10) == 12:
                        table[stack][0] = card
                        if table[0][1] < 0:
                            table[0][0] = -1
                        elif table[0][2] < 0:
                            table[0][1] = -1
                        else:
                            table[0][2] = -1
                    else:
                        print("\nThat card cannot be placed there.\n")
                else:
                    for n in range(1, 20):
                        if table[stack][n] < 0:
                            above = table[stack][n - 1]
                            break
                    if int(card / 10) == int(above / 10) - 1 and (card % 10 - 1.5) ** 2 != (above % 10 - 1.5) ** 2:
                        for n in range(1, 20):
                            if table[stack][n] < 0:
                                table[stack][n] = card
                                break
                        if table[0][1] < 0:
                            table[0][0] = -1
                        elif table[0][2] < 0:
                            table[0][1] = -1
                        else:
                            table[0][2] = -1
                    else:
                        print("\nThat card cannot be placed there.\n")
        elif response == "3":
            response = entry(1, 7, 0, "\nChoose which stack to move. Stacks are numbered from left to right,"
                                      " starting with 1.\n\n> ")
            if response == "menu" or response == "quit":
                return
            stack = int(response)
            if table[stack][0] < 0:
                print("\nThat stack is empty.\n")
            else:
                bottom = 1
                while bottom < 17 and table[stack][bottom + 1] > -1:
                    bottom += 1
                response = entry(0, bottom, 0, "\nChoose the cutoff point of the stack. Cards in a stack"
                                               " are numbered from top to bottom, starting with 1. To"
                                               " move the entire stack, enter 0.\n\n> ")
                if response == "menu" or response == "quit":
                    return
                cutoff = int(response)
                if cutoff < table[20][stack - 1]:
                    print("\nYou cannot move an unrevealed card.\n")
                else:
                    holder = []
                    for n in range(cutoff, bottom + 1):
                        holder.append(table[stack][n])
                    response = entry(1, 7, 0, "\nChoose where to move the stack. Stacks are numbered"
                                              " from left to right, starting with 1.\n\n> ")
                    if response == "menu" or response == "quit":
                        return
                    above = int(response)
                    if above == stack:
                        print("\nYou have successfully moved the stack onto itself.\n")
                    else:
                        if table[above][0] < 0:
                            if int(holder[0] / 10) == 12:
                                for n in range(len(holder)):
                                    table[above][n] = holder[n]
                                if table[20][stack - 1] > cutoff - 1:
                                    table[20][stack - 1] -= 1
                                while table[stack][cutoff] > -1:
                                    table[stack][cutoff] = -1
                                    cutoff += 1
                            else:
                                print("\nThat stack cannot be placed there.\n")
                        else:
                            for n in range(len(table[above])):
                                if table[above][n + 1] < 0:
                                    if int(holder[0] / 10) == int(table[above][n] / 10) - 1 and\
                                       (holder[0] % 10 - 1.5) ** 2 != (table[above][n] % 10 - 1.5) ** 2:
                                        for m in range(len(holder)):
                                            table[above][n + 1 + m] = holder[m]
                                        if table[20][stack - 1] > cutoff - 1:
                                            table[20][stack - 1] -= 1
                                        while table[stack][cutoff] > -1:
                                            table[stack][cutoff] = -1
                                            cutoff += 1
                                    else:
                                        print("\nThat stack cannot be placed there.\n")
                                    break
        else:
            response = entry(0, 7, 0, "\nChoose which stack to take the top card from. Stacks are numbered"
                                      " from left to right, starting with 1. To take the top card from the"
                                      " draw pile, enter 0.\n\n> ")
            if response == "menu" or response == "quit":
                return
            if response == "0":
                if table[0][0] < 0:
                    print("\nThe draw pile is empty.\n")
                else:
                    index = 0
                    if table[0][1] < 0:
                        card = table[0][0]
                    elif table[0][2] < 0:
                        card = table[0][1]
                        index = 1
                    else:
                        card = table[0][2]
                        index = 2
                    if int(card / 10) == 0 or table[16 + card % 10][int(card / 10) - 1] > -1:
                        table[16 + card % 10][int(card / 10)] = card
                        table[0][index] = -1
                    else:
                        print("\nThe foundation does not contain the preceding card.\n")
            else:
                stack = int(response)
                if table[stack][0] < 0:
                    print("\nThat stack is empty.\n")
                else:
                    card = table[stack][0]
                    index = 0
                    for n in range(0, 19):
                        if table[stack][n + 1] < 0:
                            card = table[stack][n]
                            index = n
                            break
                    if int(card / 10) == 0 or table[16 + card % 10][int(card / 10) - 1] > -1:
                        table[16 + card % 10][int(card / 10)] = card
                        table[stack][index] = -1
                        if table[20][stack - 1] > index - 1:
                            table[20][stack - 1] -= 1
                    else:
                        print("\nThe foundation does not contain the preceding card.\n")
def tictactoe():
    def output():
        print("\n  A B C ")
        for n in range(3):
            print(end = str(n + 1) + "|")
            for m in range(3):
                if grid[n][m] < 0:
                    print(end = "_")
                elif grid[n][m] < 1:
                    print(end = "X")
                else:
                    print(end = "O")
                print(end = "|")
            print()
    def finished():
        if grid[0][0] == 0 and grid[0][1] == 0 and grid[0][2] == 0:
            return 0
        if grid[0][0] == 1 and grid[0][1] == 1 and grid[0][2] == 1:
            return 1
        if grid[1][0] == 0 and grid[1][1] == 0 and grid[1][2] == 0:
            return 0
        if grid[1][0] == 1 and grid[1][1] == 1 and grid[1][2] == 1:
            return 1
        if grid[2][0] == 0 and grid[2][1] == 0 and grid[2][2] == 0:
            return 0
        if grid[2][0] == 1 and grid[2][1] == 1 and grid[2][2] == 1:
            return 1
        if grid[0][0] == 0 and grid[1][0] == 0 and grid[2][0] == 0:
            return 0
        if grid[0][0] == 1 and grid[1][0] == 1 and grid[2][0] == 1:
            return 1
        if grid[0][1] == 0 and grid[1][1] == 0 and grid[2][1] == 0:
            return 0
        if grid[0][1] == 1 and grid[1][1] == 1 and grid[2][1] == 1:
            return 1
        if grid[0][2] == 0 and grid[1][2] == 0 and grid[2][2] == 0:
            return 0
        if grid[0][2] == 1 and grid[1][2] == 1 and grid[2][2] == 1:
            return 1
        if grid[0][0] == 0 and grid[1][1] == 0 and grid[2][2] == 0:
            return 0
        if grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1:
            return 1
        if grid[0][2] == 0 and grid[1][1] == 0 and grid[2][0] == 0:
            return 0
        if grid[0][2] == 1 and grid[1][1] == 1 and grid[2][0] == 1:
            return 1
        if grid[0][0] > -1 and grid[0][1] > -1 and grid[0][2] > -1 and\
           grid[1][0] > -1 and grid[1][1] > -1 and grid[1][2] > -1 and\
           grid[2][0] > -1 and grid[2][1] > -1 and grid[2][2] > -1:
            return 2
        return -1
    grid = [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1], [-1]]
    response = entry(1, 2, 0, "\nChoose which player goes first:\n\n1: You\n2: Computer\n\n> ")
    if response == "menu" or response == "quit":
        return
    grid[3][0] += int(response)
    while finished() < 0:
        if grid[3][0] < 1:
            output()
            response = entry(1, 3, 3, "\nMake your move.\n\n> ")
            if response == "menu" or response == "quit":
                return
            if response[0] == "A":
                if grid[int(response[1]) - 1][0] < 0:
                    grid[int(response[1]) - 1][0] += 1
                    grid[3][0] += 1
                else:
                    print("\nThat tile is full.\n")
            if response[0] == "B":
                if grid[int(response[1]) - 1][1] < 0:
                    grid[int(response[1]) - 1][1] += 1
                    grid[3][0] += 1
                else:
                    print("\nThat tile is full.\n")
            if response[0] == "C":
                if grid[int(response[1]) - 1][2] < 0:
                    grid[int(response[1]) - 1][2] += 1
                    grid[3][0] += 1
                else:
                    print("\nThat tile is full.\n")
        else:
            grid[3][0] -= 1
            found = False
            for n in range(3):
                if grid[n][0] < 0 and grid[n][1] > 0 and grid[n][2] > 0:
                    grid[n][0] = 1
                    found = True
                    break
                if grid[n][0] > 0 and grid[n][1] < 0 and grid[n][2] > 0:
                    grid[n][1] = 1
                    found = True
                    break
                if grid[n][0] > 0 and grid[n][1] > 0 and grid[n][2] < 0:
                    grid[n][2] = 1
                    found = True
                    break
                if grid[0][n] < 0 and grid[1][n] > 0 and grid[2][n] > 0:
                    grid[0][n] = 1
                    found = True
                    break
                if grid[0][n] > 0 and grid[1][n] < 0 and grid[2][n] > 0:
                    grid[1][n] = 1
                    found = True
                    break
                if grid[0][n] > 0 and grid[1][n] > 0 and grid[2][n] < 0:
                    grid[2][n] = 1
                    found = True
                    break
            if found:
                continue
            if grid[0][0] < 0 and grid[1][1] > 0 and grid[2][2] > 0:
                grid[0][0] = 1
                continue
            if grid[0][0] > 0 and grid[1][1] < 0 and grid[2][2] > 0:
                grid[1][1] = 1
                continue
            if grid[0][0] > 0 and grid[1][1] > 0 and grid[2][2] < 0:
                grid[2][2] = 1
                continue
            if grid[0][2] < 0 and grid[1][1] > 0 and grid[2][0] > 0:
                grid[0][2] = 1
                continue
            if grid[0][2] > 0 and grid[1][1] < 0 and grid[2][0] > 0:
                grid[1][1] = 1
                continue
            if grid[0][2] > 0 and grid[1][1] > 0 and grid[2][0] < 0:
                grid[2][0] = 1
                continue
            for n in range(3):
                if grid[n][0] < 0 and grid[n][1] == 0 and grid[n][2] == 0:
                    grid[n][0] = 1
                    found = True
                    break
                if grid[n][0] == 0 and grid[n][1] < 0 and grid[n][2] == 0:
                    grid[n][1] = 1
                    found = True
                    break
                if grid[n][0] == 0 and grid[n][1] == 0 and grid[n][2] < 0:
                    grid[n][2] = 1
                    found = True
                    break
                if grid[0][n] < 0 and grid[1][n] == 0 and grid[2][n] == 0:
                    grid[0][n] = 1
                    found = True
                    break
                if grid[0][n] == 0 and grid[1][n] < 0 and grid[2][n] == 0:
                    grid[1][n] = 1
                    found = True
                    break
                if grid[0][n] == 0 and grid[1][n] == 0 and grid[2][n] < 0:
                    grid[2][n] = 1
                    found = True
                    break
            if found:
                continue
            if grid[0][0] < 0 and grid[1][1] == 0 and grid[2][2] == 0:
                grid[0][0] = 1
                continue
            if grid[0][0] == 0 and grid[1][1] < 0 and grid[2][2] == 0:
                grid[1][1] = 1
                continue
            if grid[0][0] == 0 and grid[1][1] == 0 and grid[2][2] < 0:
                grid[2][2] = 1
                continue
            if grid[0][2] < 0 and grid[1][1] == 0 and grid[2][0] == 0:
                grid[0][2] = 1
                continue
            if grid[0][2] == 0 and grid[1][1] < 0 and grid[2][0] == 0:
                grid[1][1] = 1
                continue
            if grid[0][2] == 0 and grid[1][1] == 0 and grid[2][0] < 0:
                grid[2][0] = 1
                continue
            choices = []
            for n in range(3):
                for m in range(3):
                    if grid[n][m] < 0:
                        choices.append([n, m])
            choice = choices[random.randint(0, len(choices) - 1)]
            grid[choice[0]][choice[1]] = 1
    output()
    if finished() < 1:
        print("\nYou win!\n")
    elif finished() < 2:
        print("\nComputer wins!\n")
    else:
        print("\nIt's a tie!")
    return
print("Welcome to 3 Text Games!")
while status > -1:
    status = 1
    response = entry(1, 2, 0, "\n1: New Game\n2: Instructions\n\n> ")
    if response == "menu" or response == "quit":
        continue
    menu = int(response)
    if menu == 1:
        response = entry(1, 3, 0, "\nSelect a game:\n\n1: Minesweeper\n2: Solitaire\n3: TicTacToe\n\n> ")
        if response == "menu" or response == "quit":
            continue
        game = int(response)
        while status > 0:
            print()
            playing = True
            if game == 1:
                minesweeper()
            elif game == 2:
                solitaire()
            else:
                tictactoe()
            playing = False
            complete = status > 0
            if complete:
                response = entry(1, 3, 0, "1: Play Again\n2: Return to Menu\n3: Exit\n\n> ")
                if response == "menu" or response == "quit":
                    continue
                status = 2 - int(response)
    else:
        print("\nHello! I hope you enjoy these three games.\n\nTo navigate the menu, and for most of the"
              " decisions you make during the games,\nenter one of the specified numbers corresponding to"
              " the option you want.\n\nSometimes you will be asked to enter a coordinate, which is a letter"
              "\n(uppercase or lowercase) followed by a number. Do not add any spaces\nor other additional"
              " characters into your inputs.\n\nAt any time, enter \"menu\" to go back to the main menu, or"
              " \"quit\" to exit the game.\n\nHave fun!")
