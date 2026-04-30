import requests

# 执行api调用并查看响应
url = "http://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
"""使用这个版本的api返回json文件"""
r = requests.get(url, headers=headers)
print(f"Status code:{r.status_code}")

# 将响应转换为字典
response_dict = r.json()

# 处理结果
print(f"Total Repositories:{response_dict['total_count']}")
print(f"Complete Results:{not response_dict['incomplete_results']}")

# 处理仓库信息
repo_dicts = response_dict['items']
print(f"Repositories returned:{len(repo_dicts)}\n")
print("\nSome selected information about the first repository:")
for repo_dict in repo_dicts:
    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Repository:{repo_dict['html_url']}")
    print(f"Stars:{repo_dict['stargazers_count']}")
    print(f"Description:{repo_dict['description']}\n")