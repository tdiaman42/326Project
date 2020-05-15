import csv
import sys
import re



class PlayerName():

    def __init__(self, data):
        self.player     = data['Player']
        self.height     = float(data['Height'] or 0)
        self.wingspan   = float(data['Wingspan'] or 0)
        self.vertical   = float(data['Vertical'] or 0)
        self.weight     = float(data['Weight'] or 0)
        self.bodyfat    = float(data['Body Fat'] or 0)
        self.bench      = float(data['Bench'] or 0)
        self.agility    = float(data['Agility'] or 0)
        self.sprint     = float(data['Sprint'] or 0)

    def contain(self, stat):
        s = re.search(stat, self.player)
        if s:
            return True
        else:
            return False


class Dataset():
    def __init__(self, fn):
        self.fn_stats = []
        with open(fn) as fh:
            for row in csv.DictReader(fh):
                t = PlayerName(row)
                self.fn_stats.append(t)


def main():
    ds = Dataset(sys.argv[1])
    search_stat = sys.argv[2]
    results = []
    for stats in ds.fn_stats: 
        name = getattr(stats, "player")
        value = getattr(stats, search_stat)
        results.append((value, name))
    print("Top Ten results for: " + str(search_stat))
    for (value, name) in sorted(results, reverse=True)[:10]: 
        print(name, value)  # when you print the results put the name first
    

if __name__ == "__main__":

    main()