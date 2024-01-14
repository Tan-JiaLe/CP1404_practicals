import wikipedia

while True:
    keyword = input("Please input a page title or search phrase: ")
    if keyword == " ":
        break
    try:
        page = wikipedia.page(keyword, auto_suggest=False)
        print("title :", page.title)
        print("summary :", page.summary)
        print("url :", page.url)
    except Exception as e:
        # print("exception:", e)
        pass