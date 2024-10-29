import feedparser
from datetime import datetime

def get_medium_blogs_rss(tag, start_date=None, end_date=None, num_blogs=5):
    # Replace spaces with hyphens for Medium's tag format
    tag = tag.replace(" ", "-")
    feed_url = f"https://medium.com/feed/tag/{tag}"
    feed = feedparser.parse(feed_url)

    # Parse the provided dates
    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    if end_date:
        end_date = datetime.strptime(end_date, "%Y-%m-%d")

    blogs = []
    for entry in feed.entries:
        # Parse the entry's published date
        published_date = datetime(*entry.published_parsed[:6])

        # Check if the entry is within the date range
        if start_date and published_date < start_date:
            continue
        if end_date and published_date > end_date:
            continue

        blogs.append({
            "title": entry.title,
            "link": entry.link,
            "published": published_date.strftime("%Y-%m-%d")
        })

        # Stop once we reach the desired number of blogs
        if len(blogs) >= num_blogs:
            break

    return blogs

# Take tag and date input from the user
tag = input("Enter the topic/tag you want to search blogs for: ")
start_date = input("Enter the start date (YYYY-MM-DD) or press Enter to skip: ")
end_date = input("Enter the end date (YYYY-MM-DD) or press Enter to skip: ")
