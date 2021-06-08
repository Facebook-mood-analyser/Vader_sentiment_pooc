# Version Anglaise
print("############### Version Anglaise ###############")


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentences = ["VADER is smart, handsome, and funny.",  # positive sentence example
             "VADER is smart, handsome, and funny!",  # punctuation emphasis handled correctly (sentiment intensity adjusted)
             "VADER is very smart, handsome, and funny.", # booster words handled correctly (sentiment intensity adjusted)
             "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
             "VADER is VERY SMART, handsome, and FUNNY!!!", # combination of signals - VADER appropriately adjusts intensity
             "VADER is VERY SMART, uber handsome, and FRIGGIN FUNNY!!!", # booster words & punctuation make this close to ceiling for score
             "VADER is not smart, handsome, nor funny.",  # negation sentence example
             "The book was good.",  # positive sentence
             "At least it isn't a horrible book.",  # negated negative sentence with contraction
             "The book was only kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
             "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
             "Today SUX!",  # negative slang with capitalization emphasis
             "Today only kinda sux! But I'll get by, lol", # mixed sentiment example with slang and constrastive conjunction "but"
             "Make sure you :) or :D today!",  # emoticons handled
             "Catch utf-8 emoji such as such as 💘 and 💋 and 😁",  # emojis handled
             "Not bad at all"  # Capitalized negation
             ]

analyzer = SentimentIntensityAnalyzer()
for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print("{:-<65} {}".format(sentence, str(vs)))




# Version Française
print("############### Version Française ###############")
#https://pypi.org/project/vaderSentiment-fr/
from vaderSentiment_fr.vaderSentiment import SentimentIntensityAnalyzer

SIA = SentimentIntensityAnalyzer()

phrases = ["Rodrigo le pd",
          "Tchoow le plus beau",
          "Les drones c'est trop bien"
          "Elon musk aime le dodje coin",
          "Studio sport c'est cool :)",
          "Le css c'est comme stylé :p",
          "Espèce d'enflure",
          "Imagine ton produit il marche trop bien :3",
          "Je trouve ça super comme produit !!!!!",
          "Très décevant !!! remboursé !!!!",
          "C'est vraiment de la merde !",
          ]



for phrase in phrases:
    score  = SIA.polarity_scores(phrase)
    score2 = SIA.polarity_scores_max(phrase) # Permet d'analyser en plus chaque mot.
    print("{:-<65} {}".format(phrase, str(score)))
    print("{:-<65} {}".format(phrase, str(score2)))


print(type(score)) # dictionnaire

# neg négativité sur 1
# neu neutralité sur 1
# pos positivité sur 1

# compound
"""
The compound score is computed by summing the valence scores of each word in the lexicon,
adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive).
This is the most useful metric if you want a single unidimensional measure of sentiment for a given sentence.
Calling it a 'normalized, weighted composite score' is accurate.

It is also useful for researchers who would like to set standardized thresholds for classifying sentences as either positive, neutral, or negative.
Typical threshold values (used in the literature cited on this page) are:

positive sentiment: compound score >= 0.05
neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
negative sentiment: compound score <= -0.05

"""