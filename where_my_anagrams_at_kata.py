def anagrams(word, words):
    result = []
    for w in words:
        if sum([ord(ch) for ch in w]) == sum([ord(ch) for ch in word]):
            result.append(w)
    return result
