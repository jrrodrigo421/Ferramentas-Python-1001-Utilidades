from chatgptonic import ChatGPT


if __name__ == '__main__':
    chat = ChatGPT('###')
    # response = chat.just_chat("Ola")
    # response = chat.send("quantas vezes o vasco caiu pra segunda divisão")
    # print(response)
    chat.start_interactive_chat()
