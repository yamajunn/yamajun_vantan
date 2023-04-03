# import textwrap

# def ascii_art(text: str, font: str = "big"):
#     font_dict = {"big": [" # ", "###", "# #", "# #", "###"],
#                 "small": [".", "#", "#", "#", "."]}
#     art = ['big']
#     for c in text:
#         if c.isalnum():
#             for i, line in enumerate(font_dict[font]):
#                 if i >= len(art):
#                     art.append(line + "  ")
#                 else:
#                     art[i] = art[i] + line + "  "
#     return art



# print(ascii_art("Hello World"))
# from ascii_art_module import ascii_art

# text = "HELLO"
# result = ascii_art(text, font="big")

# for i in result:
#     print(i)
# import msvcrt

# while True:
#     key = msvcrt.getch()
#     if key == b'w':
#         print("Moving Forward")
#     elif key == b's':
#         print("Moving Backward")
#     elif key == b'a':
#         print("Moving Left")
#     elif key == b'd':
#         print("Moving Right")
# board = [['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', 'B', 'W', '.', '.', '.'],
#          ['.', '.', '.', 'W', 'B', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.']]

# def display_board(board):
#     for row in board:
#         print(row)
        
# def game_over(board):
#     if not any('.' in row for row in board):
#         return True
#     if not any('B' in row for row in board) or not any('W' in row for row in board):
#         return True
#     return False

# def legal_move(x, y, color, board):
#     if x < 0 or x > 7 or y < 0 or y > 7:
#         return False
#     if board[x][y] != '.':
#         return False
#     for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
#         if check_capture(x, y, dx, dy, color, board):
#             return True
#     return False

# def check_capture(x, y, dx, dy, color, board):
#     x += dx
#     y += dy
#     if x < 0 or x > 7 or y < 0 or y > 7:
#         return False
#     if board[x][y] == '.':
#         return False
#     if board[x][y] == color:
#         return False
#     while True:
#         x += dx
#         y += dy
#         if x < 0 or x > 7 or y < 0 or y > 7:
#             return False
#         if board[x][y] == '.':
#             return False

# board = [['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', 'B', 'W', '.', '.', '.'],
#          ['.', '.', '.', 'W', 'B', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.'],
#          ['.', '.', '.', '.', '.', '.', '.', '.']]


# def display_board(board):
#     for row in board:
#         print(row)

# board[4][2] = 'B'
# board[4][3] = 'W'
# display_board(board)

# from openai import openai_secret_manager

# # Let's check the credentials
# secret = openai_secret_manager.get_secret("openai")
# print(secret)

# # Let's install the library


# # Let's list the models available
# import openai
# models = openai.Model.list()
# for model in models['data']:
#     print(model.id)

# # Let's use the text-davinci-002
# model_engine = "text-davinci-002"

# # Let's use the model
# prompt = (f"Talk to me")

# completions = openai.Completion.create(
#     engine=model_engine,
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# message = completions.choices[0].text
# print(message)

# import openai

# # API keyを設定
# openai.api_key = "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"

# # AIに話しかける
# response = openai.Completion.create(engine="text-davinci-002", prompt='Hello, How are you?')
# print(response["choices"][0]["text"])

# import openai

# openai.api_key = "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"

# while True:
#     user_input = input("You: ")
#     response = openai.Completion.create(engine="text-davinci-002", prompt=user_input)
#     print("AI: ",response["choices"][0]["text"])

# import openai

# # APIキーを設定
# openai.api_key = "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"

# # モデルを指定
# model_engine = "text-davinci-002"

# while True:
#     message = input("You: ")
#     if message.strip().lower() == "bye":
#         print("AI: Goodbye, have a nice day!")
#         break
#     else:
#         # テキストを生成
#         response = openai.Completion.create(
#             engine=model_engine,
#             prompt= message,
#             max_tokens=1024,
#             n=1,
#             stop=None,
#             temperature=0.5,
#         )
#         # 生成されたテキストを表示
#         print("AI: " + response["choices"][0]["text"])
# import requests
# import json

# # OpenAI API endpoint
# endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

# # Replace YOUR_API_KEY with your actual API key
# api_key = "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"

# # Define the prompt
# prompt = 'What is the meaning of life?'

# # Define the headers
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {api_key}"
# }

# # Define the payload
# payload = {
#     "prompt": prompt,
#     "temperature": 0.5
# }

# # Send the request
# response = requests.post(endpoint, json=payload, headers=headers)

# # Print the response
# if response.status_code == 200:
#     json_response = json.loads(response.text)
#     print(json_response["choices"][0]["text"])
# else:
#     print("Error")
# from transformers import pipeline

# # Initialize the conversational model
# conversational_model = pipeline("text-generation")

# # Define the prompt
# prompt = 'What is the meaning of life?'

# # Generate a response
# response = conversational_model(prompt, max_length=50)[0]["generated_text"]

# # Print the response
# print(response)

# import pygame

# # Initialize pygame
# pygame.init()

# # Set screen size
# screen = pygame.display.set_mode((400, 300))

# # Set title
# pygame.display.set_caption("My Game")

# # Run the game loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Fill the screen with white color
#     screen.fill((255, 255, 255))

#     # Update the screen
#     pygame.display.flip()

# # Quit pygame
# pygame.quit()

# import openai

# # APIキーを設定します
# openai.api_key = "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"
# while True:
#     # 私と会話するためにpromptを設定します
#     prompt = input("you: ")

#     # 私に対してpromptを送信します
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=prompt
#     )

#     # 私からの返答を受け取ります
#     print(response["choices"][0]["text"])
# from tqdm import tqdm
# import time

# for i in tqdm(range(1000)):
#     # do something
#     print(i)
#     time.sleep(1)
# import time

# for i in range(3):
#     print(f"{i+1}回目の文字列")
#     time.sleep(1)
#     print("\033c", end="")
# import time

# for i in range(3):
#     print('\r' + '文字列' + str(i+1), end='')
#     time.sleep(1)

# import time

# for i in range(3):
#     print("Line {}".format(i+1), end="\r")
#     print("Line {}".format(i+1), end="\r")
#     time.sleep(1)

# import sys
# import time

# lines = ["line 1", "line 2", "line 3"]

# for i in range(10):
#     for line in lines:
#         sys.stdout.write("\r" + line)
#         sys.stdout.flush()
#         time.sleep(1)
import time

# 3つの文字列
lines = ["Line 1", "Line 2", "Line 3"]

while True:
    for line in lines:
        # カーソルを一番上に戻す
        print("\033[F", end="")
        # 現在の行を上書き
        print(line)
        # 1秒待つ
        time.sleep(1)
