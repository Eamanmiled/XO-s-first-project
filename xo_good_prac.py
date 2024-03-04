class Game:

    def play(self):
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


jack = Game()
jack.play()
