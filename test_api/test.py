import requests
import json
# 使用中转链接可以和特定的API可以不必向openai/anthropic发起请求，且请求无须魔法
# 支持其他模型，已接入Claude,
# 调用方式与openai官网一致，仅需修改baseurl
Baseurl = "https://api.claude-Plus.top"
Skey = "sk-4ZGZU3uyi3oAtdqkFeF815407d4249E1BaCc7057Bb438fFd"
payload = json.dumps({
    "model": "claude-3-5-sonnet-20240620",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "hello"
        }
    ]
})
url = Baseurl + "/v1/chat/completions"
headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {Skey}',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# 解析 JSON 数据为 Python 字典
data = response.json()

# 获取 content 字段的值
content = data

print(content['choices'][0]['message']['content'])
