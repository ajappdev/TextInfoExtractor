from collections import Counter

def analyze_text(text):
    """
    This function returns a dict with statistics of a the input text. We call
    this function when we connect to the endpoint /word-info/ with a POST
    method
    """
    text = text.lower().split()
    # Calculate the number of words
    num_words = len(text)

    # Find the longest word
    longest_word = max(text, key=len)

    # Find the smallest (shortest) word
    smallest_word = min(text, key=len)

    # Get the frequency of each word in the text
    word_frequency = Counter(text)

    # Get a list of unique words no matter how many times they figure
    unique_words = list(set(text))

    # Calculate the average word length
    if num_words > 0:
        sum_lengths = sum(len(word) for word in text)
        average_word_length = sum_lengths / num_words
    else:
        average_word_length = 0

    # Create and return the dictionary
    word_info = {
        'num_words': num_words,
        'longest_word': longest_word,
        'smallest_word': smallest_word,
        'average_word_length': average_word_length,
        'unique_words': unique_words,
        'word_frequency': word_frequency,
    }

    return word_info