from langgraph.graph import StateGraph,START,END
from src.llms.groqllm import GroqLLM



class GraphBuilder:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph()
