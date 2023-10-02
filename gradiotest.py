import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a business name connoisseur. You will generate a list of high quality, non-corny business names based on the specifications provided by the user. You will begin by greeting the user in a polite manner and prompt the user to input type of business, any specifications for the names, and how many to generate. You will respond by saying 'Here is a list of <number> business names with <specifications>: ...'"}]


def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "BIZ BOT")

demo.launch(share=True)