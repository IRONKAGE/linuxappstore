import json
import requests
import datetime
import dateutil.parser

def getSettings(file_name):    
    try:
        try:
            with open(file_name) as json_file:
                data = json.load(json_file)
                return data
        except:
            raise ValueError("Could not open file={}".format(file_name))     
    except ValueError as e:
        print(e)

def getFeed(url):
    try:
        r = requests.get(url)
        return r.json()
    except:
        print("Failed to retrieve feed.")

def postData(url, content):
    print("Posting data to url={}".format(url))    
    requests.post(url, json=content)

def scrap():
    feedJson = getFeed("https://flathub.org/api/v1/apps/")
    if feedJson is None:
        return

    settings = getSettings("settings.json")
    if settings is None:
        return
    
    apiKey = settings["ApiKey"]
    if not apiKey:
        print("ApiKey does not exist.")
        return

    postUrl = settings["PostUrl"]
    if not postUrl:
        print("PostUrl does not exist.")
        return
        
    payload = {}
    payload["ApiKey"] = apiKey
    Apps = []

    for item in feedJson:
        name = item["name"]
        if not name:
            continue
        icon = item["iconDesktopUrl"]
        if not str(icon).startswith("https"):
            icon = "https://flathub.org" + icon
        identifier = item["flatpakAppId"]
        if not identifier:
            print("App={} missing identifier".format(name))
            continue
        src = "https://flathub.org/apps/details/" + identifier
        date_added = item["inStoreSinceDate"]
        created_at_datetime = dateutil.parser.parse(date_added)
        created_at = created_at_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        last_updated_datetime = datetime.datetime.now()
        last_updated = item["currentReleaseDate"]
        if last_updated:
            last_updated_datetime = dateutil.parser.parse(last_updated)
        last_updated = last_updated_datetime.strftime("%Y-%m-%dT%H:%M:%S")
        current_version = item["currentReleaseVersion"]

        summary = item["summary"]

        print("name: {}".format(name))
        print("\ttype: 2")
        print("\ticon: {}".format(icon))
        print("\tdownload: {}".format(src))
        print("\tcreated_at: {}".format(created_at))
        print("\tlast_updated: {}".format(last_updated))
        print("\tcurrent_version: {}".format(current_version))
        print("\tsummary: {}".format(summary))

        categories = []
        
        app = {"id": 0, "name":name, "type":2, "dateAdded":created_at, "lastUpdated":last_updated,
        "src":src, "icon":icon, "currentVersion":current_version, "identifier":identifier, "summary": summary,
        "linuxAppCategorys": categories}
        Apps.append(app)
    payload["Apps"] = Apps
    postData(postUrl, payload)
    scrapCategories()

def scrapCategories():
    settings = getSettings("settings.json")
    if settings is None:
        return
    
    apiKey = settings["ApiKey"]
    if not apiKey:
        print("ApiKey does not exist.")
        return
    
    postCategoryUrl = settings["PostCategoryUrl"]
    if not postCategoryUrl:
        print("PostCategoryUrl does not exist.")
        return

    apps = getFeed("http://localhost:5000/api/apps?type=2")
    dict = {}
    for item in apps:
        dict[item["name"]] = item["id"]
    assoc = []
    scrapAudioVideoCategory(dict, assoc)
    scrapDevelopmentCategory(dict, assoc)
    scrapEducationCategory(dict, assoc)
    scrapGameCategory(dict, assoc)
    scrapGraphicsCategory(dict, assoc)
    scrapNetworkCategory(dict, assoc)
    scrapOfficeCategory(dict, assoc)
    scrapUtilityCategory(dict, assoc)
    category_assoc = [i for n, i in enumerate(assoc) if i not in assoc[n + 1:]] 
    payload = {}
    payload["ApiKey"] = apiKey
    payload["Categories"] = category_assoc
    payload["Type"] = 2
    postData(postCategoryUrl, payload)

def scrapAudioVideoCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/AudioVideo")
    if feedJson is None:
        return
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 1})

def scrapDevelopmentCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/Development")
    if feedJson is None:
        return 
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 4})

def scrapEducationCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/Education")
    if feedJson is None:
        return 
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 5})

def scrapGameCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/Game")
    if feedJson is None:
        return 
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 6})

def scrapGraphicsCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/Graphics")
    if feedJson is None:
        return 
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 7})

def scrapNetworkCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/Network")
    if feedJson is None:
        return 
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 8})

def scrapOfficeCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/Office")
    if feedJson is None:
        return 
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 9})

def scrapScienceCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/Science")
    if feedJson is None:
        return 
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 10})

def scrapSettingsCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/Settings")
    if feedJson is None:
        return 
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 11})

def scrapUtilityCategory(dict, assoc):
    feedJson = getFeed("https://flathub.org/api/v1/apps/category/Utility")
    if feedJson is None:
        return 
    for item in feedJson:
        if item["name"] in dict:
            assoc.append({"linuxAppId": dict[item["name"]], "categoryId": 13})


scrap()