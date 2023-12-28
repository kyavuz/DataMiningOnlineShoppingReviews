import nltk
from nltk.corpus import stopwords
"""from textblob import TextBlob
from collections import Counter
import string"""
from textblob import TextBlob
from collections import Counter

def exclude_stopwords(blob):
    # exclude stopwords
    # download NLTK stopwords list
    nltk.download('stopwords')
    # define custom stopwords (which doesn't exist in NLTK stopwords list)
    modal_verbs = ["one", "got", "use", "also", "would", "could", "may", "many", "like", "even", "in", "the"]
    stopwords_for_amazon = ["united", "states", "Reviewed", "helpful", "found", "people", "this", "verified", "purchase", "verify", "yet"]
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    # exclude stopwords and convert all words lowercase
    filtered_words = [word.lower() for word in blob.words if word.lower() not in (stopwords.words('english') + modal_verbs + stopwords_for_amazon + months)]
    # exclude Punctuation marks and numbers
    filtered_words = [word for word in filtered_words if word.isalpha()]
    return filtered_words

def find_top_single_words(filtered_words):
    # count words
    word_counts = Counter(filtered_words)
    # find most common words
    top_keywords = word_counts.most_common(10)
    return top_keywords

def find_top_two_word_phrases(filtered_words):
    # create 2-word phrases
    two_word_phrases = [" ".join(filtered_words[i:i + 2]) for i in range(len(filtered_words) - 1)]
    # count 2-word phrases
    two_word_phrase_counts = Counter(two_word_phrases)
    # find most common 2-word phrases
    top_two_word_phrases = two_word_phrase_counts.most_common(10)
    return top_two_word_phrases

def find_top_three_word_phrases(filtered_words):
    # create 3-word phrases
    three_word_phrases = [" ".join(filtered_words[i:i + 3]) for i in range(len(filtered_words) - 2)]
    # count 3-word phrases
    three_word_phrase_counts = Counter(three_word_phrases)
    # find most common 3-word phrases
    top_three_word_phrases = three_word_phrase_counts.most_common(5)
    return top_three_word_phrases

def print_top_keywords(top_keywords):
    # print the results for single words
    for keyword, count in top_keywords:
        print(f"{keyword}: {count}")

def main():
    # get the text from a txt file (must be English)
    # Select and open user_reviews.txt file
    file_name = 'user_reviews.txt'
    import io
    with io.open(file_name, 'r', encoding='utf-8') as file:
    #with open(file_name, 'r') as file:
        text = file.read()

    # create TextBlob object ######################################################################
    blob = TextBlob(text)

    # exclude stopwords ###########################################################################
    filtered_words = exclude_stopwords(blob)

    # find most common keywords ###################################################################
    top_keywords = find_top_single_words(filtered_words)

    # find most common 2-word phrases #############################################################
    top_two_word_phrases = find_top_two_word_phrases(filtered_words)

    # find most common 3-word phrases #############################################################
    top_three_word_phrases = find_top_three_word_phrases(filtered_words)

    # print the results ###########################################################################
    print("\nTop Keywords:")        ; print_top_keywords(top_keywords)            # print the results for single words
    print("\nTop 2-word Phrases:")  ; print_top_keywords(top_two_word_phrases)    # print the results for 2-word Phrases
    print("\nTop 3-word Phrases:")  ; print_top_keywords(top_three_word_phrases)  # print the results for 3-word Phrases

if __name__ == "__main__":
    main()



