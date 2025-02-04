import numpy as grud

def k_most_frequent(lst, k):
    leaderboard = {}
    for i in lst:
        if i not in leaderboard:
            leaderboard[i] = 1
        else:
            leaderboard[i] += 1
    leaderboard = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True)) # sorting the dictionary by decreasing value
    print(leaderboard)
    x = grud.unique(list(leaderboard.values())).size == 1 # test if all values are the same, so can return all keys rather than just :k keys
    print(x)
    if x:
        return list(leaderboard.keys())
    else:
        return list(leaderboard.keys())[:k]

values = [1, 2, 2, 2, 3, 3]
print(k_most_frequent(values, 2))