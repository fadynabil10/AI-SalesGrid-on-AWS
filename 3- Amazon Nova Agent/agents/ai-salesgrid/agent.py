from openai import OpenAI
if __name__ == '__main__':
    client = OpenAI(
        base_url="https://api.nova.amazon.com/v1",
        api_key="<API_KEY>",
    )
    response = client.chat.completions.create(
        model="AGENT-1fb10db68a5248509d87af7c848751cb",
        messages=[
            {"role": "user", "content": "hello"}
        ],
    )
    print(response.choices[0].message.content)