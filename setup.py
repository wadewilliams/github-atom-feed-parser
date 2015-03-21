from setuptools import setup

setup(
    name = 'github_feedparser',
    packages = ['github_feedparser'],
    install_requires = ['feedparser==5.1.3'],
    version = '0.1.1',
    license = 'MIT',
    description = 'Python module to parse a GitHub repository\'s Atom Feed',
    author = 'Wade Williams',
    author_email = 'wade@wadewilliams.com',
    url = 'https://github.com/wadewilliams/github-atom-feed-parser',
    download_url = 'https://github.com/wadewilliams/github-atom-feed-parser/tarball/0.1',
    keywords = ['github', 'rss', 'atom', 'feedparser'],
)
