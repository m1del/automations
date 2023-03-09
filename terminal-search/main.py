import webbrowser
import sys

# To use this yourself, add this line to your /.bashrc file:
# alias s='python <absolute-path-to-this-file>/main.py'

# Filter results
validWebsites = [
    'reddit.com',
    'stackoverflow.com',
    'stackexchange.com',
    'quora.com',
    'medium.com'
]

url = "https://www.google.com/search?client=firefox-b-1-d&q="


def createFilter():
    resFilter = '('
    for i, website in enumerate(validWebsites):
        resFilter += 'site: ' + website
        if i == len(validWebsites) - 1:
            resFilter += ')'
        else:
            resFilter += ' OR '
    return resFilter


def createQuery():
    query = sys.argv[1:]
    return ' '.join(query)


def createUrl():
    if len(sys.argv[1:]) == 0:
        print("Invalid Query")
    else:
        finalUrl = url + createQuery() + createFilter()
        return finalUrl


webbrowser.open_new_tab(createUrl())
