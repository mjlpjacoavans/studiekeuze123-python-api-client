from urllib.parse import unquote
import urllib.request

csrf_data = {}
csrf_url = "https://www.studiekeuze123.nl:443/opleidingen"
get_headers = {
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"92\"",
    "Sec-Ch-Ua-Mobile": "?0", "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.131 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "close"
}

def get_csrf_data():
    req = urllib.request.Request(csrf_url, headers=get_headers)
    r = urllib.request.urlopen(req)
    headers = r.headers.items()
    for header in headers:
        if header[0] == "Set-Cookie":
            header_val = header[1]
            header_vals = header_val.split(";")
            header_real = header_vals[0]
            header_real_name, header_real_value = header_real.split("=")
            if header_real_name == "XSRF-TOKEN":
                csrf_data["XSRF-TOKEN"] = unquote(header_real_value)
            elif header_real_name == "laravel_session":
                csrf_data["laravel_session"] = unquote(header_real_value)
            elif len(header_real_name) == 40:
                csrf_data[header_real_name] = unquote(header_real_value)
    return csrf_data
