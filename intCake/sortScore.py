def sort_scores(unsorted_scores, highest_possible_score):

    if check_if_sorted(unsorted_scores):
        return unsorted_scores

    # Sort the scores in O(n) time
    if len(unsorted_scores) == 1:
        return unsorted_scores

    mid = int(len(unsorted_scores)/2)

    return merge(sort_scores(unsorted_scores[:mid], highest_possible_score), sort_scores(unsorted_scores[mid:], highest_possible_score))


def merge(sorted_a, sorted_b):

    merged = []

    while sorted_a and sorted_b:
        if sorted_a[0] > sorted_b[0]:
            merged.append(sorted_a[0])
            sorted_a.pop(0)
        else:
            merged.append(sorted_b[0])
            sorted_b.pop(0)

    return merged + sorted_a + sorted_b


def check_if_sorted(scores):
    i = 0
    while i < len(scores)-1:
        if scores[i] < scores[i+1]:
            return False
        i += 1
    return True


unsorted_scores = [37, 89, 41, 65, 91, 53]
# unsorted_scores = [30, 60]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
