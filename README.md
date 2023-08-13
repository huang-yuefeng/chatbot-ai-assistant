# chatbot-ai-assistant
A chatbot based on GPT to use AI tools by natural language instead of Python
# Installation
- Run a docker container by mapping the port for Flask service. The web service can be called in your browser while running inside the docker.
```docker run --name=LLM -p 127.0.0.1:5003:5003 -it  -v /Users/work/:/home/work/ vd:2.0 bin/bash```
- Prepare the Python environment with the version of 3.9. This is very important. If the version is lower, the installation will not be completed. The installation will not throw an error, but when running the application, there will be a module missing error, which is not easy to fix. 
- Get the latest Releases https://github.com/langchain-ai/langchain/releases/tag/v0.0.261
- Install by source code
```pip install -e .```
- To use LLM, install LLMs support
```pip install langchain[llms]```
- To use OpenAI API, you must have a key and set the environment variable
```export OPENAI_API_KEY=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```
If you use a "free trial" key, you will be limited requests per day at most 200 and per minute at most 3. This will not be enough for this demo because, inside some API calls, there will be dozens of times internal API calls, which will overflow out of 200 in very little time. And of course, the robot responds very slowly. I suggest a "pay as you go" key.
# Run the demo
- This is a typical Flask web service, with the front end "index.html" in the template folder and service entrance in "app.py". The verbose switch is default open, so in the console, there will be the processing process of the robot.
- Start the application by ```python app.py``` in the home folder on the server side.
- Start the front end in your docker host browser address ```http://localhost:5003/```.
- Upload a "xls", "xlsx", or "csv" file data from the button at the bottom of the page. You can find sample data at ```https://www.kaggle.com/datasets/jancui/titannic?resource=download```. If you don't upload the data file first, the chatbot doesn't know what to deal with.
# Analyze data
If you are using a "free trial" key, you will get the response of "Agent stopped due to iteration limit or time limit.". This is because of the limitation of 3 times calls per minute, the agent fails. Change into a "pay as you go" key to fix it.
This is some samples result on Titanic data from my web service, just FYI. Although it seems good enough, but actually the API responds slow, and sometimes will throw exceptions. This is just a GPT3.5 model in 2021 with many issues. 
- data basic infomation
![data_info](./sample_result/data_info.png)
- statistical analysis
![statistical_info](./sample_result/statistical_info.png)
- pie plot
![pie_plot](./sample_result/pie_graph.png)
- scatter plot
![scatter_plot](./sample_result/scatter_plot.png)
- polyline plot
![polyline plot](./sample_result/poly_line_graph.png)
- scatter plot over two columns
![scatter plot over two columns](./sample_result/scatter_point_2column.png)
- correlation matrix
![correlation matrix](./sample_result/correlation_matrix.png)
- linear regression
![linear regression](./sample_result/linear_regression.png)
- logistic regression
![linear regression](./sample_result/logistic_regression.png)
- factorization analysis
![factorization analysis](./sample_result/factorization_analysis.png)
# Great acknowlegement 
- to wechat ID ZZ2222rk
I don't know who he is or anything about him, but he provides his OpanAI API key for me multiple times. When a key is out of date, I will contact him for a new one. This guy is very helpful with a true free spirit, so I can do this evaluation work.
- to my little daughter
While I was working in weekend, she just keep quiet with a comic book for hours.
  


