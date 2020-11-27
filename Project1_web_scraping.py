import requests
from bs4 import BeautifulSoup
import pprint
import datetime


def data_handling():
    user_input = input("From which website would you like to scrape?: ")
    response = requests.get(user_input)  # via cmd
    soup = BeautifulSoup(response.text, 'html.parser')  # parse to HTML file instead of text --> CSS selectors
    # print(soup.select('.storylink')) # checking whether I selected the right class
    # print(soup.select('.subtext'))
    url = soup.select('.storylink')  # CSS selector (via class) to grab data from HTML parsed file
    subtext = soup.select('.subtext')
    return url, subtext


def sort_by_vote(hackernews_list):
    return sorted(hackernews_list, key=lambda k: k['votes'], reverse=True)  # Article with highest amount of votes first


def my_hackernews():
    url, subtext = data_handling()
    hacker_news = []
    for index, item in enumerate(url):
        title = url[index].getText()
        href = url[index].get('href', None)  # None as default in case of missing/broken link
        vote = subtext[index].select('.score')
        if len(vote):  # Some articles possibly do not have any votes
            points = int(vote[0].getText().replace(' points', ''))
            # We need to work with integers on the next line, so: access the text and replace with empty string
            if points > 499:
                hacker_news.append({'title': title, 'url': href, 'votes': points})
    return sort_by_vote(hacker_news)


pprint.pprint(my_hackernews())
print(datetime.date.today())

# (Windows) Command prompt --> execute file + input website (https://news.ycombinator.com/)
# Output: From which website would you like to scrape?: https://news.ycombinator.com/
# [{'title': 'Tell HN: Thank You Dang', 'url': 'item?id=25225775', 'votes': 1787},
#  {'title': 'How io_uring and eBPF Will Revolutionize Programming in Linux',
#   'url': 'https://www.scylladb.com/2020/05/05/how-io_uring-and-ebpf-will-revolutionize-programming-in-linux/',
#   'votes': 640},
#  {'title': 'CAPTCHAs don’t prove you’re human – they prove you’re American '
#            '(2017)',
#   'url': 'https://shkspr.mobi/blog/2017/11/captchas-dont-prove-youre-human-they-prove-youre-american/',
#   'votes': 502}]
# 2020-11-27
