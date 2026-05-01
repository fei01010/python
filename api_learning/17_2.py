from operator import itemgetter
import requests
import plotly.express as px

url = "http://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status Code:{r.status_code}")

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    url =  f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id:{submission_id}\tstatus:{r.status_code}")
    response_dict = r.json()

    # 给每一篇文章, 都创建一个字典
    submission_dict = {
        'title':response_dict['title'],
        'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",
        'comments':response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)
submission_links, comments = [], []
for submission_dict in submission_dicts:
    sub_link = f"<a href='{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    submission_links.append(sub_link)
    comments.append(submission_dict['comments'])


title = "Most Comments Article on HackerNews"
labels = {'x': 'Article', 'y': 'Comments'}
fig = px.bar(x=submission_links, y=comments, title=title, labels=labels)
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.show()