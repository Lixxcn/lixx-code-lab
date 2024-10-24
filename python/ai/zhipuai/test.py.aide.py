# 导入zhipuai模块中的ZhipuAI类，这个类用于与智谱AI的API进行交互
from zhipuai import ZhipuAI

# 实例化ZhipuAI类，创建一个客户端对象，传入API密钥，这个密钥是用于身份验证的
# 请将"08125206889b7c5a4ff9bf49cefddf5a.0ITnfgHKTEwzukTZ"替换成您自己的APIKey
client = ZhipuAI(api_key="08125206889b7c5a4ff9bf49cefddf5a.0ITnfgHKTEwzukTZ")

# 调用客户端对象的chat属性中的completions属性，并使用create方法发起一个请求
# 请求中指定了模型为"glm-4"，并且在messages参数中提供了一条用户信息"你好"
response = client.chat.completions.create(
    model="glm-4",  # 指定使用的模型
    messages=[
        {"role": "user", "content": "你好"},  # 用户发送的信息
    ],
)

# 打印出响应对象中的choices列表的第一个元素的message属性
# 这个message属性包含了由智谱AI生成的回复内容
print(response.choices[0].message)
