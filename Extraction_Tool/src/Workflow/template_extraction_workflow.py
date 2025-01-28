from abc import ABC, abstractmethod


class ExtractionWorkflow(ABC):
    platform_name: str

    def extract_relevant_discussions(self, searchterm, result_holder):
        """Template method defining the workflow for extracting relevant discussions."""
        all_posts = self.fetch_posts(searchterm)
        print(f"Number of {self.platform_name} threads found: {len(all_posts)}")

        filtered_posts = self.filter_posts(all_posts)
        print(
            f"Number of {self.platform_name} threads after filtering: {len(filtered_posts)}"
        )

        discussions = self.get_full_discussions(filtered_posts)
        result_holder.put(discussions)

    @abstractmethod
    def fetch_posts(self, searchterm):
        """Fetches posts from the platform."""
        pass

    @abstractmethod
    def filter_posts(self, posts):
        """Filters the fetched posts."""
        pass

    def get_full_discussions(self, posts):
        """Uses the template pattern to get full discussions."""
        discussions = []
        for post in posts:
            comments = self.get_comments(post)
            normalized_comments = [self.create_comment(comment) for comment in comments]
            discussion = self.create_discussion(post, normalized_comments)
            discussions.append(discussion)
        return discussions

    @abstractmethod
    def get_comments(self, post):
        """Fetches comments for a post."""
        pass

    @abstractmethod
    def create_discussion(self, post, comments):
        """Creates a Discussion object from a post and its comments."""
        pass

    @abstractmethod
    def create_comment(self, raw_comment):
        """Creates a Comment object from raw comment data."""
        pass
