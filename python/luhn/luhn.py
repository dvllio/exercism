class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
        self.backup = self.card_num

    def valid(self):
        for x in self.card_num:
            if not str(x).isdigit():
                return False

        self.card_num = list(map(int, self.card_num))

        for i in range(len(self.card_num)-2,-1,-2):
            if self.card_num[i]*2 > 9:
                self.card_num[i] = (self.card_num[i]*2)-9
            else:
                self.card_num[i] *= 2

        if self.card_num == [0]:
            return False
        elif sum(self.card_num)%10 == 0:
            self.card_num = self.backup
            return True