class card:
    def __init__(self, cardlines):
        self.numbers = []
        self.marked = []
        self.last_called = 0

        for line in cardlines:
            row = line.split()
            self.numbers.append(row)
        
        cardrow = [False] * 5
        for row in range(5):
            self.marked.append(cardrow.copy())            

    def showit(self):
        print(self.numbers)
        print(self.marked)

    def mark(self, mark_number):
        self.last_called = int(mark_number)
        for row in range(5):
            for col in range(5):
                if (self.numbers[row][col] == mark_number):
                    self.marked[row][col] = True
                    return

    def winner(self):
        for row in range(5):
            did_i_win = True
            for col in range(5):
                did_i_win = did_i_win and self.marked[row][col]
            if (did_i_win):
                return True

        for col in range(5):
            did_i_win = True
            for row in range(5):
                did_i_win = did_i_win and self.marked[row][col]
            if (did_i_win):
                return True
        return False

    def score(self):
        myscore = 0
        for row in range(5):
            for col in range(5):
                if (self.marked[row][col] == False):
                    myscore += int(self.numbers[row][col])
        myscore = myscore * self.last_called
        return myscore


bingo_cards = []
winners = []
losers = []

def check_for_winner():
    for card in range(len(bingo_cards)):
        if (bingo_cards[card].winner()):
            return card
    return None

def tally_winners():
    winners.clear()
    losers.clear()
    for card in range(len(bingo_cards)):
        if (bingo_cards[card].winner()):
            winners.append(card)
        else:
            losers.append(card)

with open('day4input.txt', 'r') as fp:
    line = fp.readline().strip()
    drawn = line.split(",")
    count = 0
    cardline = []
    for line in fp:
        if (count):
            cardline.append(line.strip())
        count += 1
        if (count == 6):
            bcard = card(cardline)
            bingo_cards.append(bcard)
            cardline.clear()
            count = 0
        
for pick in drawn:
    print(f"pick: {pick}")
    for bcard in bingo_cards:
        bcard.mark(pick)
    tally_winners()
    if (len(losers) == 1):
        big_loser = losers[0]
    if (len(losers) == 0):
        print(f"big loser is card #{big_loser}!")
        bingo_cards[big_loser].showit()
        score = bingo_cards[big_loser].score()
        print(f"Score: {score}")
        break

