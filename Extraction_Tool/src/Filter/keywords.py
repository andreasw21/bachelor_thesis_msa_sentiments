from typing import List


big_companies = [  # if they contain companies they are probably news articles
    "Google",
    "Microsoft",
    "Apple",
    "Facebook",
    "IBM",
    "Uber",
    "Airbnb",
    "Salesforce",
    "Twitter",
    "LinkedIn",
    "Spotify",
    "Adobe",
    "Tesla",
    "Oracle",
    "Intel",
    "Alibaba",
    "SAP",
    "Zoom",
    "Slack",
    "Dropbox",
    "Salesforce",
    "Shopify",
    "ByteDance",
    "Snapchat",
    "Palantir",
    "Pinterest",
    "Reddit",
    "Square",
    "NVIDIA",
    "eBay",
]
# Keywords
irrelevant_keywords_tech = [  # I don't want technical discussions, but conceptual ones.
    "spring boot",
    "company",
    "java",
    "spring",
    "hibernate",
    "sql",
    "aws",
    "kafka",
    "tutorial",
    "guide",
    "job",
    "career",
    "resume",
    "interview",
    "learning",
    "course",
    "event",
    "news",
    "update",
    "showhn",  # for hackernews this is a keyword used to signal that the thread shows a user project
    "implement",
]


relevant_keywords_strength_high = (
    [  # if those are contained its very probably that its relevant
        "vs",
        "in contrast to",
        "as opposed to",
        "compared to",
        "compared with",
        "disadvantage",
        "pros",
        "cons" "comparison",
        "comparison",
        "monolith",
        "architecture",
        "design patterns",
        "scalability",
        "msa",
    ]
)


relevant_keywords_strength_low = [
    "don't need",
    "do need",
    "module",
    "reason",
    "advantage",
    "should I",
    "is it worth it",
    "is it a good idea",
    "thoughts on",
    "opinions on",
    "challeng",
    "why you should",
    "why you shouldn’t",
    "what's better",
    "experience",
    "best practices",
    "case studies",
    "lessons learned",
    "impact of",
    "future of",
    "strateg",
    "consider",
    "decision-making",
]

relevant_keywords = relevant_keywords_strength_high + relevant_keywords_strength_low
irrelevant_keywords = irrelevant_keywords_tech + big_companies
