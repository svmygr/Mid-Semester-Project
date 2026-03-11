from langchain_openai import ChatOpenAI

def summarize(text):
    llm = ChatOpenAI(
        model="llama3",
        base_url="http://localhost:11434/v1",
        api_key="not-needed"
    )
    prompt = f"Summarize the following information:\n{text}"
    return llm.invoke(prompt).content
