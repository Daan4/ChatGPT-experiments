import os
import openai
import functools
openai.api_key = os.getenv("OPENAI_API_KEY")


def display(func):
    @functools.wraps(func)
    def wrapper_display_stats(*args, **kwargs):
        response = func(*args, **kwargs)
        print(f"Time Taken: {response.response_ms / 1000.0}s")
        print(f"Token Usage: {response.usage['total_tokens']} total, {response.usage['completion_tokens']} completion, {response.usage['prompt_tokens']} prompt")
        print(f"Response:\n{response.choices[0].message['content']}")
        return response.choices[0].message["content"]
    return wrapper_display_stats


@display
def get_completion_from_prompt(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response


@display
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response
