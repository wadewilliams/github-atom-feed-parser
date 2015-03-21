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

        self.feed = feedparser.parse(self.endpoint)

    def _respond(self):
        ''' Always return false for bozos. '''

        if self.feed['bozo'] == 1:
            return False
        else:
            return self.parsed_feed

    def get_html(self):

        self.parsed_feed = u''

        for each in self.feed.entries:
            self.parsed_feed = self.parsed_feed + u'<a href="%s" target="_blank"><img src="%s"> %s</a> <a href="%s" target="_blank">%s</a><br>' % \
                (each['href'], each['media_thumbnail'][0]['url'], each['author'], each['link'], each['title'])

        return self._respond()

    def get_obj(self):

        self.parsed_feed = []

        for each in self.feed.entries:
            self.parsed_feed.append({
                'user_url': each['href'],
                'user_avatar_url': each['media_thumbnail'][0]['url'],
                'user_name': each['author'],
                'commit_url': each['link'],
                'commit_msg': each['title'],
                'timestamp': each['updated']
            })

        return self._respond()

    def get_json(self):

        self.parsed_feed = json.dumps(self.get_obj())
        return self._respond()
