import requests
import plotly.express as px

url = "https://api.github.com/search/repositories"
url += "?q=language:JavaScript+sort:star+star>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status Code:{r.status_code}")
response_dict = r.json()
print(f"Comlpete Results:{not response_dict['incomplete_results']}")

repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # 设置悬停文本
    repo_owner = repo_dict['owner']['login']
    repo_description = repo_dict['description']
    hover_text = f"{repo_owner}<br />{repo_description}"
    hover_texts.append(hover_text)

title = "Most Starred JavaScript Projects on Github"
labels = {'x': 'repository', 'y': 'stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()