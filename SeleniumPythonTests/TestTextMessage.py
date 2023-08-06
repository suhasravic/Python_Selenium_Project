import requests

url = "https://www.fast2sms.com/dev/bulkV2"

querystring = {
    "authorization": "tMDNOgfSXGfCrTNqV7rpcqqK2THaklMXMXaYk6FZTeKPHiN6ON1mrfIjAyKW",
    "message": "Hello ",
    "language": "english",
    "route": "q",
    "numbers": "8217223341"}

headers = {
    'cache-control': "no-cache"
}
try:
    response = requests.request("GET", url,
                                headers=headers,
                                params=querystring)
    print(response)

    print("SMS Successfully Sent")
except:
    print("Oops! Something wrong")
