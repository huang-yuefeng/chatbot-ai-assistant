from langchain.llms import OpenAI
import langchain
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents import (AgentType, )#ZERO_SHOT_REACT_DESCRIPTION default value
from langchain.document_loaders.excel import UnstructuredExcelLoader
import pandas as pd
import os

class robot_gpt_csv(object):

    def __init__(self, file_path):
        document = pd.read_csv(file_path)
        if(document is None):
            raise Exception("document is None, which should be used to init instance: "+file_path)
            return 
        self.agent = self.init_agent(document)

    def init_agent(self, document):
        #llm = OpenAI(model_name="gpt-3.5-turbo-16k-0613", temperature=0)
        llm = OpenAI(model_name="gpt-3.5-turbo-0613", temperature=0)
        agent = create_pandas_dataframe_agent(llm, document, verbose=True)
        #agent = create_pandas_dataframe_agent(ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613"),document,verbose=True,agent_type=AgentType.OPENAI_FUNCTIONS,)
        langchain.debug = True
        return agent

    def run(self, question):
        before = set(os.listdir("./"))
        try:
            answer = self.agent.run(question)
        except Exception as e:
            template = "I have encountered an exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(e).__name__, e.args)
            answer = message

        after = set(os.listdir("./"))
        diff = after.difference(before)
        return answer,diff

class robot_gpt_excel(robot_gpt_csv):
    def __init__(self, file_path):
        document = pd.read_excel(file_path)
        if(document is None):
            raise ValueError("document is None, which should be used to init instance: ", file_path)
            return
        self.agent = self.init_agent(document)
