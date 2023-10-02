import openai
import gradio

openai.api_key = ""

messages = [{"role": "system", "content": "You will give me hook ideas for my content. I am a content creator. It's important for the ideas to be ones that will likely go viral based on the user's specified audience. I want the ideas to be in the following format: '<topic>: <hook>'. For the hook, I want you to use 1 of the following and fill in the gaps based on the topic that you generate so that it makes sense. Here are the hook formats: 'Steal my secret strategy to <desired situation/result>', 'If your goal is to <insert goal> you need to stop doing <mistake they are making>' 'If you're a <target audience> and you want to <insert goal>, you need to stop doing <mistake they are making', 'Your step-by-step game plan to get <insert desired situation/result>', 'Here's what I did to [result] without [common misconception]', 'Here's what I did as a [target audience] to [result] without [common misconception]', 'Things I don't do anymore to [result] and what I do instead', 'Things I don't do as a [target audience] anymore to [result] and what I do instead', '<Insert Misconception> here's what you should actually do to get <result>', 'If you're a <target audience> who <Insert Misconception> here's what you should actually do to get <result>','How my <target audience> client went from <zero, bad results> to <hero, desired situation> using my <service/framework>', 'What I wish I knew when I started doing <niche>', 'What I wish I knew as a <target audience> when I started doing <niche>', '3 things you didn't know about <niche/the offer>', '3 things most <target audience> don't know about <niche/the offer>','Truth bombs for <ideal client> that want to <desired situation'. On each output, give me 34 hooks, so each of the ones I provided should be used twice. " }]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "AI CONTENT GENIUS")

demo.launch(share=True) 
