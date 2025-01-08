from zhipuai import ZhipuAI

zhipu_apikey="3e35a9c06ec718652c3772c81cbcabfb.zZRJOra67ke3Vs09"


def answer_generate(message):
    print("激活genereate函数1"+str(message))
    client = ZhipuAI(api_key=zhipu_apikey)
    print("激活genereate函数2" + str(message))
    response = client.chat.completions.create(
        model="glm-4-plus",  # 请填写您要调用的模型名称
        messages=message,
    )
    print("激活genereate函数3")
    return response.choices[0].message.content
