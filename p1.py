def group_anagrams(words):
    anagrams = {}
    for word in words:
        str = ''.join(sorted(word))
        anagrams[str] = word


# sort the letters

words = ["bat", "meta", "tab", "tea", "ate", "tame", "jazz", "eat", "elephant", "phetenal"]
group_anagrams(words)
