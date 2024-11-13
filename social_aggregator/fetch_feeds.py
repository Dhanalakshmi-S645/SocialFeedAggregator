import requests
from .models import Feed

def fetch_from_twitter():
    # Example request
    headers = {'Authorization': 'Bearer YOUR_TWITTER_API_BEARER_TOKEN'}
    response = requests.get('https://api.twitter.com/2/tweets', headers=headers)
    # Process and save data to Feed model

def fetch_from_reddit():
    # Example request for Reddit
    headers = {'User-Agent': 'SocialFeedAggregator'}
    response = requests.get('https://www.reddit.com/r/popular.json', headers=headers)
    # Process and save data to Feed model

    useEffect(() => {
    const fetchFeeds = async () => {
        const response = await fetch('http://127.0.0.1:8000/feeds/'); // Replace with your Django endpoint
        const data = await response.json();
        setFeeds(data);
    };

    fetchFeeds();
}, []);

