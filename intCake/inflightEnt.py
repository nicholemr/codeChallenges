def can_two_movies_fill_flight(movie_lengths, flight_length):

    mset = set()

    for m in movie_lengths:

        if flight_length - m in mset:
            return True

        mset.add(m)

    return False


movies, flight = [3, 8, 3], 6

print(can_two_movies_fill_flight(movies, flight))
