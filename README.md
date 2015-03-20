### Installation

```
pip install github_feedparser
```

### Usage

```
from github_feedparser import GitHubFeedParser

my_feed = GitHubFeedParser('wadewilliams', 'github-atom-feed-parser')

my_feed.get_obj()  # Returns a python object
my_feed.get_html() # Returns HTML payload
my_feed.get_json() # Returns a json object
```