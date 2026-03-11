from agents.web_agent import web_search
from agents.summary_agent import summarize

def run_agents(query):

    web_results = web_search(query)

    combined_info = f"""
    Web Results:
    {web_results}
    """

    final_answer = summarize(combined_info)

    return final_answer
