# Implement a function that takes a 2D N x N input (e.g matrix / image data) and rotates the content by 90 degrees clockwise. Candidate should come up with an algorithm that is efficient both in use of space and time.
# Example:
#         a b c d          n i e a
#         e f g h     ->   o j f b
#         i j l m          p l g c
#         n o p q          q m h d
# https://www.youtube.com/watch?v=fMSJSS7eO1w

def rotate(matrix):
    # YOUR CODE GOES HERE
    return


def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    TEST_MATRIX = [
        ['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'l', 'm'],
        ['n', 'o', 'p', 'q'],
    ]
    print("Test matrix:")
    print_matrix(TEST_MATRIX)
    rotate(TEST_MATRIX)

    print("\n\nRotated matrix:")
    print_matrix(TEST_MATRIX)


# run main
main()

# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dots menu on the tab, or add a new language
# tab using the Languages button on the left.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

# Enjoy your interview!



