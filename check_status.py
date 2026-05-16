from urllib.request import urlopen

def check_status():
    url = "https://playlostark.com/en-us/support/server-status"
    search_term = "Thaemine is online"

    try:
        response = urlopen(url)
        content = response.read().decode("utf-8")
    except Exception as e:
        print(f"An error occurred: {e}")

    if content.find(search_term) != -1:
        return "online"

if __name__ == "__main__":
    print(check_status())
