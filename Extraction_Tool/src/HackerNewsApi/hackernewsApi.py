import json
from typing import List, Dict


hacker_news_url_basis = "http://hn.algolia.com/api/v1/search"


def get_hackernews_posts(
    query: str = "story", post_type: str = "story", maximum_posts: int = 1000
) -> List[Dict]:
    """
    Fetches posts from Hacker News based on type and query, handling timestamp-based pagination to retrieve all available results.

    :param query: Search query (e.g., 'microservices').
    :param post_type: Type of posts to get (story, comment, poll, pollopt, show_hn, ask_hn, job).
    :param maximum_posts: How many posts you want to query maximally
    :return: List of posts as dictionaries.
    """

   # Hackernews has a rate limit 1,000 stories per request.That's why I need pagination.
# the pagination strategy of this function was inspired by https://github.com/santiagobasulto/python-hacker-news/blob/master/hn/api.py

    hits_per_page = 1000  # this is the maximum hits that are allowed in 1 request according to HN Rate Limits

    base_url = "https://hn.algolia.com/api/v1/search_by_date"
    all_hits = []
    oldest_timestamp = None

    while len(all_hits) < maximum_posts:
        params = {
            'query': query,
            'tags': post_type,
            'hitsPerPage': hits_per_page
        }
        if oldest_timestamp:
            params['numericFilters'] = f'created_at_i<{oldest_timestamp}'


        hits = get_hits_from(base_url, params=params)
        
        if not hits:
            break  # Exit loop if no more results are available

        all_hits.extend(hits)
        if len(all_hits) >= maximum_posts:
            all_hits = all_hits[:maximum_posts]  # Trim to maximum_posts if we saved too many posts

        oldest_timestamp = min(hit['created_at_i'] for hit in hits if 'created_at_i' in hit)
   # print(f"All hits contain {len(all_hits)} hits")  

    return all_hits


def get_comments_for_story(story_id: str, hits_per_page: int = 0) -> json:
    """
    Fetches comments from HackerNews for a specific story.

    :param story_id: ID of the story.
    :return: List of comments.
    """
    base_url = "https://hn.algolia.com/api/v1/search_by_date"

  
    params = {
        'tags': f'comment,story_{story_id}',
        'hitsPerPage': hits_per_page
    }

   
    comments = get_hits_from(base_url, params)

    num_comments = len(comments)
    print(
        f"{num_comments} comments fetched for a Hackernews Story."  # Note that num_comments may differ cause of deleted comments.
    )

    return comments



def get_hits_from(base_url: str, params: dict = {}) -> json:
    from src.Utils import request_handling
    """
    Fetches JSON data from HackerNews, constructs the query URL, extracts hits array, and returns those hits as JSON.s
    """
    # Construct the query string and full URL
    query_string = "&".join([f"{key}={value}" for key, value in params.items()])
    url = f"{base_url}?{query_string}"

    return request_handling.get_json_from(url).get("hits", [])

