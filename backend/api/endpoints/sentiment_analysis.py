import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from fastapi import FastAPI, APIRouter
import json
from ..modules.data import input_details
router = APIRouter()
app = FastAPI()

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')


@router.post("/check_sentiment/", tags=["NLP"])
def check_sentiment(item: input_details):
    item = json.loads(item.json())
    sentence = item.get("text")
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(sentence)

    # Analyzing the compound score
    if sentiment_score['compound'] >= 0.05:
        return "Positive"
    elif sentiment_score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"


# Example usage
# sentence = input("Enter a sentence: ")
# sentiment = check_sentiment(sentence)
# print("Sentiment of the sentence is:", sentiment)

# if __name__ == "__main__":
#     check_sentiment()