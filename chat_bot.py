from settings import model
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

def get_workflow():
    workflow = StateGraph(state_schema=MessagesState)
    workflow.add_edge(START, "model_call")
    workflow.add_node("model_call", call_model)

    memory = MemorySaver()
    return workflow.compile(checkpointer=memory)