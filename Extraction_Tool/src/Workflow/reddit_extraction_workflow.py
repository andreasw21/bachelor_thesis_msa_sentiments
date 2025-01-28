from src.config import ALL_MS_REDDIT_POSTS
from src.Workflow.template_extraction_workflow import ExtractionWorkflow


from src.RedditApi.reddit_post_type import RedditPost
from src.discussion_dataclasses import Comment, Discussion


class RedditExtractor(ExtractionWorkflow):

    platform_name = "Reddit"

    def fetch_posts(self, searchterm):
        from src.RedditApi.redditApi import reddit_get_submissions
        from src.RedditApi.reddit_post_type import RedditPost

        all_reddit_submissions = reddit_get_submissions(
            searchterm, num_posts=ALL_MS_REDDIT_POSTS
        )
        return [
            RedditPost.create_reddit_post_from_submission(submission)
            for submission in all_reddit_submissions
        ]

    def filter_posts(self, posts):
        from src.Filter.filter_reddit import my_reddit_filter

        return my_reddit_filter(posts)

    def get_comments(self, post):
        from src.RedditApi.praw_access import RedditAccess
        from src.RedditApi.redditApi import reddit_get_comments

        return reddit_get_comments(RedditAccess.accessor.submission(post.id))

    def create_discussion(self, post, comments):
        return Discussion.create_from_reddit_post(post, comments)

    def create_comment(self, raw_comment):
        return Comment.create_from_reddit_comment(raw_comment)
