import random


class Game:

    def ai(self):
        jack = 0
        grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # this is for the "AI"
        rows = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        column = [1, 1, 1, 2, 2, 2, 3, 3, 3]
        # this is where the game begins
        while self.haveyouwon(grid) != True:
            # this is to make the grid
            i = 0
            print("---------------")
            while i < 3:
                print(grid[i])
                print("---------------")
                i += 1
            # this is to add "x"
            r = int(input("Row? 1-3: "))
            c = int(input("Column? 1-3: "))
            while grid[r - 1][c - 1] != " " or r > 3 or c > 3:
                print("try again dipshit")
                r = int(input("Row? 1-3: "))
                c = int(input("Column? 1-3: "))
            grid[r - 1][c - 1] = "X"
            if self.haveyouwon(grid) == True:
                print("You Win")
                break
            # this is "AI" turn
            bill = len(rows) - 1
            r = random.randint(0, bill)
            c = random.randint(0, bill)
            while grid[rows[r] - 1][column[c] - 1] != " ":
                rows.__delitem__(r)
                column.__delitem__(c)
                r = random.randint(0, len(rows) - 1)
                c = random.randint(0, len(column) - 1)
            grid[rows[r] - 1][column[c] - 1] = "O"
            rows.__delitem__(r)
            column.__delitem__(c)
            jack += 1
            if self.haveyouwon(grid) == True:
                print("AI won")
                break
            elif jack == 8:
                print("no winners :(")
                break
        print("Game over")

    def human(self):
        jack = 0
        grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        # this is where the game begins
        while self.haveyouwon(grid) != True:
            i = 0
            print("---------------")
            while i < 3:
                print(grid[i])
                print("---------------")
                i += 1
            print("press enter to exit")
            r = int(input("Row? 1-3: "))
            c = int(input("Column? 1-3: "))
            while grid[r - 1][c - 1] != " " or r > 3 or c > 3:
                print("try again dipshit")
                r = int(input("Row? 1-3: "))
                c = int(input("Column? 1-3: "))
            if jack % 2 == 0:
                grid[r - 1][c - 1] = "X"
            else:
                grid[r - 1][c - 1] = "O"
            jack += 1
            if jack == 8:
                break
        print("you win")

    def haveyouwon(self, grid):
        if grid[0][0] == grid[0][1] == grid[0][2] != " ":
            return True
        elif grid[1][0] == grid[1][1] == grid[1][2] != " ":
            return True
        elif grid[2][0] == grid[2][1] == grid[2][2] != " ":
            return True
        elif grid[0][0] == grid[1][0] == grid[2][0] != " ":
            return True
        elif grid[0][1] == grid[1][1] == grid[2][1] != " ":
            return True
        elif grid[0][2] == grid[1][2] == grid[2][2] != " ":
            return True
        elif grid[0][0] == grid[1][1] == grid[2][2] != " ":
            return True
        elif grid[0][2] == grid[1][1] == grid[2][0] != " ":
            return True
        else:
            return False


player = Game()
print("what game mode would you like to play")
type = input("human or AI: ")
if type == "human":
    player.human()
elif type == "AI":
    player.ai()
else:
    print("That's not right input either 'human' or 'AI'")
    while type != "human" and type != "AI":
        type = input("human or AI: ")
    if type == "human":
        player.human()
    elif type == "AI":
        player.ai()
