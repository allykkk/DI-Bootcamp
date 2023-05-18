import requests, time


# instruction: Using the requests and time modules, create a function which returns the amount of time
# it takes a webpage to load (how long it takes for a complete response to a request).
def measure_loading_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        if response.status_code == 200:
            loading_time = end_time - start_time
            return loading_time
        else:
            return None
    except requests.exceptions.RequestException:
        return None


# instruction: Test your code with multiple sites such as google, ynet, imdb, etc.
websites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for website in websites:
    loading_time = measure_loading_time(website)
    if loading_time is not None:
        print(f"Loading time for {website}: {loading_time:.2f} seconds")
    else:
        print(f"Failed to measure load time for {website}")