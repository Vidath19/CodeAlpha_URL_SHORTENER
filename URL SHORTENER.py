import string
import random

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))
        self.url_mapping[short_url] = long_url
        return short_url

    def redirect_url(self, short_url):
        if short_url in self.url_mapping:
            return self.url_mapping[short_url]
        else:
            return None

# Example usage
shortener = URLShortener()
long_url = "https://www.example.com/this-is-a-very-long-url"
short_url = shortener.shorten_url(long_url)
print(f"Short URL: {short_url}")
redirected_url = shortener.redirect_url(short_url)
print(f"Redirected URL: {redirected_url}")
