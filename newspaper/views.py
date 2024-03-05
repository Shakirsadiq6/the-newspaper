from django.shortcuts import render
from datetime import datetime

from .utils import *
from .models import *
import ast
# Create your views here.
def homepage(request):
    news_title, _, news_image = get_main_news_title_image()
    if not News.objects.filter(news_title=news_title).exists():
        news_content = get_main_news_content()
        news_content = news_content[:-1]
        total_records = News.objects.count()
        today_date = datetime.now()
        formatted_date = today_date.strftime("%A, %d %B, %Y")
        News.objects.create(
            issue=total_records+1,
            date=formatted_date,
            news_title=news_title,
            news_image=news_image,
            news_content=news_content
        )
        return render(request, 'index.html', {"issue": total_records+1, "date": formatted_date, "title": news_title, "image": news_image, "content": news_content})
    else:
        latest_news = News.objects.latest('id')
        news_issue = latest_news.issue
        news_date = latest_news.date
        news_title = latest_news.news_title
        news_image = latest_news.news_image
        news_content = latest_news.news_content
        news_content_list = ast.literal_eval(news_content)
        return render(request, 'index.html', {"issue": news_issue, "date": news_date, "title": news_title, "image": news_image, "content": news_content_list})
