def group_anagrams(words):
    anagrams = {}
    for word in words:
        ben = ''.join(sorted(word))
        if ben not in anagrams:
            anagrams[ben] = [word]
        else:
            anagrams[ben].append(word)
        print(anagrams)
    idk = []
    for i in anagrams:
        idk.append(anagrams[i])
    return idk


# sort the letters


words = ["bat", "meta", "tab", "tea", "ate", "tame", "jazz", "eat", "elephant", "phetenal"]
print(group_anagrams(words))
