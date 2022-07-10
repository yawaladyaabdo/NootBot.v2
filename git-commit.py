import os

MESSAGE = input("What is your message: ")

os.system("git add :")
os.system(f'git commit -m "{MESSAGE}"')
os.system('git push')
os.system('git push --mirror https://github.com/yawaladyaabdo/NootBot.v2.git')
