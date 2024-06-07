import pandas as pd
import openai
import argparse
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain


# Define a function to initialize the agent
def initialize_agent(df, openai_api_key):
    template = """You are a chatbot having a conversation with a human include chat history refer to the csv when needed.
    Human: {human_input},
    {chat_history}
    Chatbot:"""

    prompt = PromptTemplate(
        input_variables=["chat_history", "human_input"], template=template
    )
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)


    llm = OpenAI(temperature=0, openai_api_key=openai_api_key)

    p_agent = create_pandas_dataframe_agent(llm=llm, 
        df=df, 
        max_iterations=10,
        verbose=True,
        memory=memory)

    conv_agent = LLMChain(llm=llm, prompt=prompt, memory=memory)
    
    return p_agent, conv_agent

# Main function to run the script
def main():
    parser = argparse.ArgumentParser(description="Chat with GPT about a CSV file in real-time")
    parser.add_argument('--api-key', type=str, required=True, help="OpenAI API key")
    parser.add_argument('--csv-path', type=str, required=True, help="Path to the CSV file")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_path, index_col=0)
    # df = df[["name","artist","release_date","length","popularity"]]

    csv_agent, conv_agent = initialize_agent(df, args.api_key)

    print("Chat with GPT about the CSV file. Type 'exit' to quit.")
    while True:
        question = input("You: ")
        if question.lower() == 'exit':
            break
        if "csv" in question.lower() or any(keyword in question.lower() for keyword in list(df.columns)):
            answer = csv_agent.run(question)
        else:
            answer = conv_agent.run({"human_input": question})
        print(f"GPT: {answer}")

if __name__ == "__main__":
    main()
