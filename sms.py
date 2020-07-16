import requests

r=requests.get('https://www.fast2sms.com/dev/bulk?authorization=zwZq28OeSHT4Nr19VdC5jKtYalB3fxRXWFLEpui6QUbvnGJPDAvOUEwngFqVxsB95N8lTkH2oSXticYZ&sender_id=FSTSMS&message=This%20is%20test%20message&language=english&route=p&numbers=9398911069')

print(r.status_code)
