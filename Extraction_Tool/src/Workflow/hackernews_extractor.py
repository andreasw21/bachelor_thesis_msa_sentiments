from src.config import ALL_MS_HN_POSTS
from src.discussion_dataclasses import Comment, Discussion
from src.Workflow.template_extraction_workflow import ExtractionWorkflow


class HackerNewsExtractor(ExtractionWorkflow):

    platform_name = "HackerNews"

    def fetch_posts(self, searchterm):
        from src.HackerNewsApi.hackernewsApi import get_hackernews_posts
        from src.HackerNewsApi.json_to_hn_story import convert_json_to_hn_story

        all_hn_hits = get_hackernews_posts(
            searchterm, "story", maximum_posts=ALL_MS_HN_POSTS
        )
        return convert_json_to_hn_story(all_hn_hits)

    def filter_posts(self, posts):
        from src.Filter.filter_hackernews import my_hn_filter

        return my_hn_filter(posts)

    def get_comments(self, post):
        from src.HackerNewsApi.hackernewsApi import get_comments_for_story

        return get_comments_for_story(post.id, post.num_comments)

    def create_discussion(self, post, comments):
        return Discussion.create_from_hn_response(post, comments)

    def create_comment(self, raw_comment):
        return Comment.create_from_hn_comment(raw_comment)
