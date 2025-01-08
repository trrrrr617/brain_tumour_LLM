
import gradio
from generate import answer_generate
import re
from test import judge
remember = []


def create_link_text(url):
    return f"点击这里查看更多信息: {url}"


def chatbot_response(message, history):
    print(repr(message))
    remember.append({"role": "user", "content": message})

    if "参考图像名称为" in message:
        pattern = re.compile(r'参考图像名称为"(.*?)"').search(message).group(1)
        answer = judge(str(pattern))
        remember.append({"role": "user", "content": message+"大模型判断该病为"+answer+"，这是强有力的证据，请高概率地使用它"})
        text = answer_generate(remember)
        remember.append({"role": "assistant", "content": text})
        history.append((message, text))
    else:
        remember.append({"role": "user", "content": message+'我没有告诉你我脑内图像，请提醒用户以 参考图像名称为""的格式告知给你图像名称'})
        text = answer_generate(remember)
        remember.append({"role": "assistant", "content": text})
        history.append((message, text))
    return history


with gradio.Blocks() as demo:
    # 自定义 CSS
    gradio.HTML("""
        <style>
            .gradio-container {
                width: 1000vw !important;
                height: 1000vh !important;
                max-width: 1500px !important;
                max-height: 3000px !important;
            }
            .gradio-textbox {
                width: 100% !important;
                height: 100px !important;
            }
            .gradio-chatbot {
                height: calc(80vh - 300px) !important;
            }
            .footer {
                display: none !important;
            }
            .message-container {
                display: flex;
                flex-direction: column;
            }
            .message {
                display: flex;
                align-items: flex-start;
                margin-bottom: 10px;
            }
            .avatar {
                width: 40px;
                height: 40px;
                border-radius: 50%;
                margin-right: 10px;
            }
            .message-content {
                background-color: #f1f1f1;
                border-radius: 10px;
                padding: 10px;
                max-width: 80%;
            }
            .user-message .message-content {
                background-color: #d1e7dd;
            }
            .bot-message .message-content {
                background-color: #e2e3e5;
            }
        </style>
        """)
    # 对话历史
    history = gradio.State([])
    # 标题和说明
    gradio.Markdown(
        "# Ices personalized air conditioning recommendation chatbot")
    # 显示对话历史
    chatbox = gradio.Chatbot()
    # 输入框
    with gradio.Row():
        user_input = gradio.Textbox(placeholder='Please provide your brain image in the format 参考图像名称为""', label="Your Message")
        submit_button = gradio.Button("Send")
    # 处理用户输入和更新对话历史
    submit_button.click(chatbot_response, inputs=[user_input, history], outputs=chatbox)

# 启动界面
if __name__ == "__main__":
    demo.launch()