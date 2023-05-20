def permutationList(lst):
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    result = []  # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
        index = lst[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remainingLst = lst[:i] + lst[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutationList(remainingLst):
            result.append([index] + p)
    return result


# Driver program to test above function
givenList = [1, 2, 3]
print(permutationList(givenList))