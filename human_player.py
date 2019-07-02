class Human:
    @staticmethod
    def give_move(moves):
        while True:
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            if (row, col) in moves:
                return (row, col)