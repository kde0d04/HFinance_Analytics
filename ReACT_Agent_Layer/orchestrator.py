from ReACT_Agent_Layer.agent_core import run_agent


def orchestrate_agent(query: str):
    reasoning, answer = run_agent(query)

    reasoning.insert(0, "Orchestrator initialized the agent workflow.")
    reasoning.append("Orchestrator finalized the response.")

    return reasoning, answer
