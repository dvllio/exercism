class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):

        if self.minute < 0:
            if (self.minute / -60) >= 1:
                self.hour -= (self.minute / -60)
            else:
                self.hour -= 1
 
        if (self.minute / 60) >= 1:
            self.hour += (self.minute / 60)

        return "%02d" % (self.hour % 24) +":""%02d" % (self.minute % 60)

    def __eq__(self, other):
        return str(self) == str(other) 

    def __add__(self, minutes):
        return Clock(self.hour,(self.minute + minutes))

    def __sub__(self, minutes):
        return Clock(self.hour,(self.minute - minutes))