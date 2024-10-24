from zhipuai import ZhipuAI
client = ZhipuAI(api_key="08125206889b7c5a4ff9bf49cefddf5a.0ITnfgHKTEwzukTZ") # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4",
    messages=[
        {"role": "user", "content": "生成两百行代码的shell脚本，实现和k8s有关的功能"},
    ],
)
print(response.choices[0].message)
    