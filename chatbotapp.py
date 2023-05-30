import gradio
import openai

openai.api_key = "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"

messages = [{"role":  "system", "content": "You are a Educator Assistant"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


demo = gradio.Interface(fn= CustomChatGPT,inputs = "text",outputs= "text", title = "Chatbot App")

demo.launch(share=True)




