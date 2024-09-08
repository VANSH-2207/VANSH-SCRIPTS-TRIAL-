import openai   
openai.api_key = "sk-liWyhdZRbmhsM0QkD9Hm334d0C7xERrpHjJqvfLu2HT3BlbkFJkgzfBtqPmkuyBEQKoUYcLHdnzw8TPiJtu42hsDbJEA"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response['choices'][0]['message']['content'].strip()  # Updated the way to access content

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            break
        
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)
