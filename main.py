import openai
import dotenv
import os

dotenv.load_dotenv()

# Set your secret API key
api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = api_key

questions = [
    "Hi there",
    "How are you",
    "Is anyone there?",
    "Hey",
    "Hola",
    "Hello",
    "Good day",
    "Bye",
    "See you later",
    "Goodbye",
    "Nice chatting to you, bye",
    "Till next time",
    "Thanks",
    "Thank you",
    "That's helpful",
    "Awesome, thanks",
    "Thanks for helping me",
    "How you could help me?",
    "What you can do?",
    "What help you provide?",
    "How you can be helpful?",
    "What support is offered?",
    "Open blood pressure module",
    "Task related to blood pressure",
    "Blood pressure data entry",
    "I want to log blood pressure results",
    "Blood pressure data management",
    "I want to search for blood pressure result history",
    "Blood pressure for patient",
    "Load patient blood pressure result",
    "Show blood pressure results for patient",
    "Find blood pressure results by ID",
    "Find me a pharmacy",
    "Find pharmacy",
    "List of pharmacies nearby",
    "Locate pharmacy",
    "Search pharmacy",
    "Anxious",
    "Depressed",
    "Roommate",
    "Job",
    "Crush",
    "life is good",
    "confident",
    "people always like me",
    "Good things happen when you make them happen",
    "not enough",
    "not worthy",
    "worthless",
    "not good",
    "yes",
    "no",
    "god",
    "religion",
    "culture",
    "cultural",
    "study",
    "academics",
    "learning",
]

for word in questions:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": word},
        ],
    )
    print(response['choices'][0]['message']['content'])
    # save response to file
    with open('output.txt', 'a') as f:
        answer = {'question': word, 'answer': response['choices'][0]['message']['content']}
        f.write(str(answer))
        f.write('\n')