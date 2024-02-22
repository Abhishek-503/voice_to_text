from newsapi import NewsApiClient
from fastapi import FastAPI, APIRouter

router = APIRouter()
app = FastAPI()


@router.post("/def get_news/", tags=["NLP"])
def get_news():
    # Initialize News API client
    newsapi = NewsApiClient(api_key='3d266fc0aaf943f7bf7aae832039a2ab')

    # Get top headlines
    top_headlines = newsapi.get_top_headlines(language='en')

    # Extract headlines
    headlines = [article['title'] for article in top_headlines['articles']]
    return headlines


# def main():
#     while True:
#         user_input = input("What do you want to hear? (joke/news/quit): ").lower()
#
#         if user_input == 'news':
#             headlines = get_news()
#             for i, headline in enumerate(headlines, start=1):
#                 print(f"{i}. {headline}")
#         elif user_input == 'quit':
#             print("Quitting...")
#             break
#         else:
#             print("Invalid input. Please try again.")
#
#
# if __name__ == "__main__":
#     main()
