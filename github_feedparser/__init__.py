import feedparser
import json


class GitHubFeedParser:

    def __init__(self, *args, **kwargs):
        '''
        param string owner required
        param string repo required
        '''

        try:
            self.owner = args[0]
            self.repo = args[1]
        except IndexError:
            raise ValueError("Two parameters are required: owner and repository")

        self.endpoint = 'http://github.com/%s/%s/commits/master.atom' % (self.owner, self.repo)

        # Parse the feed and die here if we need to.
        self._parse()

    def _parse(self):
        self.feed = feedparser.parse(self.endpoint)

        if self.feed['bozo'] == 1:
            return False

    def get_html(self):

        parsed_feed = u''

        for each in self.feed.entries:
            parsed_feed = parsed_feed + u'<a href="%s" target="_blank"><img src="%s"> %s</a> <a href="%s" target="_blank">%s</a><br>' % \
                (each['href'], each['media_thumbnail'][0]['url'], each['author'], each['link'], each['title'])

        return parsed_feed

    def get_obj(self):

        parsed_feed = []

        for each in self.feed.entries:
            parsed_feed.append({
                'user_url': each['href'],
                'user_avatar_url': each['media_thumbnail'][0]['url'],
                'user_name': each['author'],
                'commit_url': each['link'],
                'commit_msg': each['title'],
                'timestamp': each['updated']
            })

        return parsed_feed

    def get_json(self):
        return json.dumps(self.get_obj())

