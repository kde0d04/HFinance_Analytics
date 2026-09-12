from ReACT_Agent_Layer.tools import retrieve_context, calculate_metrics, visualize_data


def run_agent(query: str):
    reasoning_steps = []
    answer = ""

    reasoning_steps.append("Parsed the query.")

    if "liquidity" in query.lower():
        reasoning_steps.append("Decided to use Processing Layer for liquidity ratio.")
        answer = calculate_metrics("liquidity")
    elif "profit" in query.lower():
        reasoning_steps.append("Decided to use Processing Layer for profit margin.")
        answer = calculate_metrics("profit")
    elif "chart" in query.lower() or "trend" in query.lower():
        reasoning_steps.append("Decided to use Visualization Layer for chart/trend.")
        answer = visualize_data()
    else:
        reasoning_steps.append("Decided to use Retrieval Layer for context.")
        answer = retrieve_context(query)

    return reasoning_steps, answer
