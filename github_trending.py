import requests
import sys

def get_data_from_api(url, payload=None):
    response = requests.get(url, params=payload)
    if response.ok:
        return response.json()

def get_trending_repositories(top_size=20):
    api_url = 'https://api.github.com/search/repositories'
    payload = {'q':'created:>2018-04-11', 'sort': 'stars', 'order': 'desc', 'per_page': top_size}
    repos = get_data_from_api(api_url, payload)["items"]
    return repos

def print_repos_issues(repos):
    for repo in repos:
        print('Repository url:', repo["html_url"])
        print('Open issues count:', repo['open_issues_count'])

if __name__ == '__main__':
    try:
        repos = get_trending_repositories()
    except requests.exceptions.ConnectionError:
        sys.exit('Server is unavailable')
    print_repos_issues(repos)