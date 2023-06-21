import os
import socket 

import openai
from flask import Flask, redirect, render_template, request, url_for, g
import redis
import json

app = Flask(__name__)



def get_secret():
    secret_path = "/mnt/secrets-store/openAIKey"
    print("this is a message inside the thing with the thing")
    try:
        with open(secret_path, 'r') as secret_file:
            print("Inside the try block, under me is secret :)")

            mountedSecret = secret_file.read().strip()
            secret = json.loads(mountedSecret)
            print(secret)
            print("the type of the secret is", type(secret))
            print(type(secret["openai-key"]))
        return secret["openai-key"]
    except FileNotFoundError:
        print(f"Secret file not found at {secret_path}")
        return None

# Comment out one 
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = get_secret()



def get_redis():
    return redis.Redis(host='redis-service', port=6379, decode_responses=True)
    # might be useful with docker 
    # if not hasattr(g, 'redis'):
    #     g.redis = redis.Redis(host="redis", db=0, socket_timeout=5)
    # return g.redis


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        redis = get_redis()
        redis.incr('count')        
        if int(redis.get('count')) > 10:
            redis.set('count', 1)

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt("Micheal Jackson", redis.get('count')),
            temperature=0.6,
            max_tokens=200
        )  

        

        if int(redis.get('count')) == 0:
            return redirect(url_for("index", result=''))


        return redirect(url_for("index", result=(response.choices[0].text)))

    result = "Current level: ${redis.get('count')}." + request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(currentCharacter, currentLevel):
    return """ You will roleplay as {}, on a scale of 1 to 10, 
        you will reply passive aggresively to my clicking on a cookie. 
        for example, level 0 is 'Haha good job clicking on that cookie, very impressive'.
        And you work your way up. On level ten you'll act completely annoyed by my clicking
        on the cookie. the current level is {}. 
        Do not break character and make it very funny. Remember that you are {}. Try to act like this person as much as possible. Start your statement with 'This is' and then your name.""".format( currentCharacter, 
                                                                  currentLevel, currentCharacter) 
