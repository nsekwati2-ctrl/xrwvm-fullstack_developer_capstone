# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
# Add code for get requests to back end
def get_request(endpoint, **kwargs):
    """
    Function to make a GET request to the backend API.
    Arguments:
    - endpoint: The endpoint to which the GET request will be made.
    - kwargs: Additional parameters for query params, headers, etc.
    """
    try:
        # Making the GET request with the provided endpoint and any additional parameters
        response = requests.get(endpoint, **kwargs)

        # Check if the response is successful (HTTP 200)
        if response.status_code == 200:
            # Return the response as JSON
            return response.json()
        else:
            # Handle non-200 responses
            print(f"Request failed with status code {response.status_code}")
            return None  # or some custom error handling logic
    except requests.exceptions.RequestException as e:
        # Handle any network-related errors (timeouts, connection errors, etc.)
        print(f"An error occurred: {e}")
        return None  # or a custom error message as per the requirement

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
# Add code for retrieving sentiments
def analyze_review_sentiments(text):
    # Construct the request URL
    request_url = sentiment_analyzer_url + "analyze/" + text
    
    # Call the get_request function to send the GET request
    sentiment = get_request(request_url)
    
    # Check if the sentiment response is not None
    if sentiment is not None:
        # Assuming the sentiment response has 'sentiment' as a key (adjust as per your actual API response)
        return sentiment
    else:
        # If sentiment is None, return an error message or a default response
        return {"status": "error", "message": "Failed to fetch sentiment"}
# def post_review(data_dict):
# Add code for posting review
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")

