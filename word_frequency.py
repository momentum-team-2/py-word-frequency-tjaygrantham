import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    f = open(file, "r") # Open txt file
    words = [word.lower() for word in f.read().strip(string.punctuation).split() if word not in STOP_WORDS] # Read txt file, strip punctuation, split into words excluding stop words
    wordCounts = {word:words.count(word) for word in words} # Get a count for each word in the words list
    sortedWords = sorted(wordCounts, key=wordCounts.get, reverse=True) # Sort words by their count
    for i in range(10):
        word = sortedWords[i]
        count = wordCounts[word]
        print(word.rjust(6), "|", count, "*" * count) # Print the 10 most common words
    f.close() # Close txt file


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
