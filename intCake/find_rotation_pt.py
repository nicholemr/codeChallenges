def find_rotation_point(words):

    # Find the rotation point in the list
    lo = 0
    hi = len(words)-1
    mid = int((hi+lo)/2)
    # check right and left sides then pick one
    while (hi-lo > 1):

        if words[lo] > words[mid]:
            hi = mid
        else:
            lo = mid
        mid = int((hi+lo)/2)

    return lo


find_rotation_point(w)
