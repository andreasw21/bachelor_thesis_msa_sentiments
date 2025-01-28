from urllib.parse import urlparse


def get_domain(url: str) -> str:
    """
    Extracts and normalizes the domain from a given URL, f.e.removing 'www'.
    """
    domain = urlparse(url).netloc.lower()
    return domain[4:] if domain.startswith("www.") else domain
