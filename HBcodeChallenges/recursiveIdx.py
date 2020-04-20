def recursive_search(word, arr, index=None):
    if arr:
        if not index:
            index = len(arr)-1

        if arr.pop() == word:
            return index

        if index == 0:
            return None

        return recursive_search(word, arr, index-1)
    return None


lst = ["hey", "there", "you"]
lst = []

print(recursive_search("there", lst))
