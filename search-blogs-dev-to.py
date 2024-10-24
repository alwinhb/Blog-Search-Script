import requests

def get_dev_to_blog_links(topic, num_links=10):
    # API endpoint for querying articles
    api_url = f"https://dev.to/api/articles?tag={topic}&per_page={num_links}"

    # Send GET request to fetch the articles
    response = requests.get(api_url)

    if response.status_code != 200:
        print(f"Failed to fetch articles, status code: {response.status_code}")
        return []

    # Parse the JSON response
    articles = response.json()

    # Extract and return the blog post URLs
    links = [article['url'] for article in articles]

    return links

if __name__ == "__main__":
    topic = input("Enter a topic to search blogs on dev.to: ")
    blog_links = get_dev_to_blog_links(topic)

    if blog_links:
        print("\nFound dev.to blog links:")
        for i, link in enumerate(blog_links, 1):
            print(f"{i}. {link}")
    else:
        print("No blogs found.")
