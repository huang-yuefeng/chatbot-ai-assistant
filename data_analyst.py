from langchain.llms import OpenAI
import langchain
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents import (AgentType, )#ZERO_SHOT_REACT_DESCRIPTION default value
import pandas as pd
import os

class robot_gpt(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.document = pd.read_csv(file_path)
        #loader = UnstructuredExcelLoader("example_data/stanley-cups.xlsx", mode="elements")
        #docs = loader.load()
        #llm = ChatOpenAI(model_name='gpt-3.5-turbo-0613', temperature=0.2)
        #self.agent = create_pandas_dataframe_agent(llm, self.document, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)
        llm = OpenAI(model_name='gpt-3.5-turbo-0613', temperature=0)
        self.agent = create_pandas_dataframe_agent(llm, self.document, verbose=True)
        langchain.debug = True

    def run(self, question):
        before = set(os.listdir("./"))
        try:
            answer = self.agent.run(question+" If the result can be shown in image, please save the result as a jpg file.")
        except Exception as e:
            template = "I have encountered an exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            answer = message

        after = set(os.listdir("./"))
        diff = after.difference(before)
        return answer,diff
