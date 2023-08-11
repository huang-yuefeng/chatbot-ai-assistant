from langchain.llms import OpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents import (AgentType, )#ZERO_SHOT_REACT_DESCRIPTION default value
import pandas as pd

def load_csv_file():
    """Loads a CSV file into a Pandas dataframe."""
    file_path = "./titanic.csv"
    #file_path = "climate_change_data.csv"
    document = pd.read_csv(file_path)
    return document

document = load_csv_file()
litte_ds = create_pandas_dataframe_agent(OpenAI(temperature=0), document, verbose=True)
litte_ds.run("Analyze this data, and tell me if you see any trends. give me a conclussion with the principal trend")
litte_ds.run("Do you see any correlations in the data? If yes tell me the principal. create a heat map for correlations, and save it as a jpeg file")
litte_ds.run("First clean the data, no null values and prepare to use it in a Machine Leaninrg Model. \
        Then decide which model is better to forecast the temperature \
        Tell me the decision and use this kind of model to forecast the temperature for the next 15 years \
        create a bar graph with the 15 temperatures forecasted, and save the bar graph as a jpeg file.")
