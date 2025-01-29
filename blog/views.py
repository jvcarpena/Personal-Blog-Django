from django.shortcuts import render
from datetime import date
# Create your views here.

all_posts = [
    {
        "slug": "sakamoto-days",
        "image": "sakamoto.jpg",
        "author": "JV",
        "date": date(2025, 1, 25), 
        "title": "Sakamoto Days: Action Comedy",
        "excerpt": "A legendary hitman retires to run a convenience store, but his past won’t let him go. Sakamoto Days delivers intense action, sharp comedy, and a lovable cast in a thrilling, must-watch anime.",
        "content": """
            Taro Sakamoto, once the world’s deadliest assassin, now lives a peaceful life with his family—until 
            old enemies come knocking. Though out of shape, his combat skills remain unmatched, leading to 
            high-energy battles mixed with absurd humor. From explosive fights to hilarious everyday struggles, 
            Sakamoto Days masterfully blends action and comedy, making it a standout in the genre.
        """
    },
    {
        "slug": "python-for-everyone",
        "image": "coding.jpg",
        "author": "JV",
        "date": date(2025, 1, 27),
        "title": "Python: Simple Yet Powerful",
        "excerpt": "Python is a beginner-friendly yet powerful language used in web development, data science, AI, and automation.",
        "content": """
            With its easy-to-read syntax and vast libraries, Python is perfect for both beginners and experts. 
            Whether building websites, analyzing data, or automating tasks, Python’s versatility and strong community 
            make it a top choice for developers.
        """
    },
    {
        "slug": "kobe-bean-bryant",
        "image": "kobe.jpg",
        "author": "JV",
        "date": date(2025, 1, 29),
        "title": 'Kobe: A Legacy of Greatness',
        "excerpt": 'Kobe Bryant wasn’t just a basketball legend—he was a symbol of hard work, determination, and the “Mamba Mentality.”',
        "content": """
            With five NBA championships, an MVP award, and countless unforgettable moments, 
            Kobe’s impact on the game was unmatched. His relentless work ethic and passion inspired athletes 
            worldwide, proving that success comes from dedication and perseverance. Even beyond basketball, 
            his influence in storytelling and mentoring continues to inspire future generations.
        """
    }
]


def get_date(post):
    return post['date']


def index(request):
    sorted_post = sorted(all_posts, key=get_date)
    latest_post = sorted_post[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_post
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    # list comprehension using next function.
    # post_to_show = next(post for post in all_posts if post['slug'] == slug)
    post_to_show = None
    for item in all_posts:
        if item['slug'] == slug:
            post_to_show = item
    return render(request, "blog/post-detail.html", {
        "post": post_to_show
    })
