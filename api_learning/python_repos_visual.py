import requests
import plotly.express as px

# 执行api调用并查看响应
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status Code:{r.status_code}")

# 处理结果
response_dict = r.json()
print(f"Complete Results:{not response_dict['incomplete_results']}")

# 处理有关仓库的信息
repo_dicts = response_dict['items']
repo_names, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # 创建悬停文本
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 可视化
title = "Most Starred Python Projects on Github"
labels = {'x': 'Repository', 'y': 'stars'}
fig = px.bar(x=repo_names, y=stars, title=title,
            labels=labels, hover_name=hover_texts)
fig.update_layout(title_font_size=28, 
            xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()