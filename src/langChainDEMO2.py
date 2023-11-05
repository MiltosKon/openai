from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name():
    llm=OpenAI(temperature=0.4)
    name = llm("give me a list with 5 dog names.")

    return name

if __name__ == "__main__":
    print(generate_pet_name())