import requests

def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token, # 權杖，Bearer 的空格不要刪掉呦
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    
    # Post 封包出去給 Line Notify
    r = requests.post(
        "https://notify-api.line.me/api/notify",
        headers=headers, 
        params=payload)
    return r.status_code