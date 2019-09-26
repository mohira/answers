import time

import requests

"""
[APIドキュメント](https://github.com/HackerNews/API#new-top-and-best-stories)
"""


def main():
    base_url = 'https://hacker-news.firebaseio.com/v0'

    topstories_url = f'{base_url}/topstories.json'
    top_story_ids = requests.get(topstories_url).json()

    fetch_record_num = 5  # デフォルトの500件は多いので減らしている

    articles = []

    for story_id in top_story_ids[:fetch_record_num]:
        story_url = f'{base_url}/item/{story_id}.json'

        print(f'Fetching: {story_url}')

        response = requests.get(story_url)
        story_dict = response.json()

        article = dict(title=story_dict['title'],
                       link=story_dict['url'])

        articles.append(article)

        time.sleep(1)

    for article in articles:
        print(article)


if __name__ == "__main__":
    main()
