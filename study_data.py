from get_csrf_token import get_csrf_data
import requests

session = requests.session()

filters = {"type.keyword": ["HBO Bachelor"], "establishment.name.keyword": ["Avans Hogeschool"]}
BASE_URL = "https://www.studiekeuze123.nl:443/opleidingen"
csrf_data = get_csrf_data()


headers = {
    "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"92\"",
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.131 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "https://www.studiekeuze123.nl",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.studiekeuze123.nl/opleidingen",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close"
}

json_data = {
    "selectedFilters": filters,
    "sortBy": "",
    "sortOrder": "asc"
}



def get_data_by_page_id(page):
    json_data["pageNumber"] = page
    headers["X-Xsrf-Token"] = csrf_data["XSRF-TOKEN"]
    return session.post(BASE_URL, headers=headers, cookies=csrf_data, json=json_data)


def get_get_data_in_range(r):
    for i in range(r):
        yield get_data_by_page_id(i)


def get_all_programs_gen():
    count = 0
    while True:
        d = get_data_by_page_id(count)
        if d.json()["hasMorePages"]:
            yield d.json()["programs"]
            count += 1
        else:
            break


def get_all_programs_list():
    programs = []
    for _programs in get_all_programs_gen():
        for program in _programs:
            programs.append(program)
    return programs


def get_programs_in_range(r):
    for d in get_get_data_in_range(r):
        yield d.json()["programs"]
