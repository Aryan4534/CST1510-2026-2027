# Fixed: every instance method receives self first.
class Record:
    def status(self, percent):
        return percent

r = Record()
print(r.status(95))
