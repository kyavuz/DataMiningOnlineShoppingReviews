from textblob import TextBlob

"""
# Example text (must be English)
#text = "TextBlob kütüphanesi oldukça kullanışlı ve kolaydır. Harika bir deneyim!"
#text = "TextBlob library is incredible! I love it!"
text = ("What I didn't like is that I couldn't figure out how to change the language and "
        "I kept trying until I was able to, once I was able to sign in to my Google account, "
        "witch gave me a problem also signing in, but I finally got it, I have it connected to"
        " my phone so my apps automatically download, that was the easiest, I got the very next"
        " day also,I ordered it last night 7,8 pm and it was here about 12 pm ,it didn't take long,"
        " I'm truly happy for that, I'll give it a couple of days and see how it works, and I'll"
        " give you more reviews, Thank you Amazon")
"""

# get the text from a txt file (must be English)
# Select and open user_reviews.txt file
file_name = 'user_reviews.txt'
import io
with io.open(file_name, 'r', encoding='utf-8') as file:
#with open(file_name, 'r') as file:
    content = file.read()
    #print(content)

text=content # edit this line (or delete)

# create TextBlob object
blob = TextBlob(text)

# sentiment analysis
sentiment = blob.sentiment

# Duygu skoru ve duygu etiketi
polarity = sentiment.polarity
subjectivity = sentiment.subjectivity

# print the results
#print(f"Metin: {text}")
#print(f"Sentiment: {sentiment}")
print(f"Duygu Skoru polarity: {polarity}")
print(f"Duygu Etiketi: {'Pozitif' if polarity > 0 else 'Negatif' if polarity < 0 else 'Nötr'}")
print(f"Konu Duyarlılık: {subjectivity}")




