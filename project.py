import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics 
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
#graph = ff.create_distplot([data],["temp"],show_hist=False)
#graph.show()
Pmean = statistics.mean(data)
pstd = statistics.stdev(data)
print("mean of the population is ",Pmean)
print("standard deviation of the population is ",pstd)
"""dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
samplemean = statistics.mean(dataset)
samplestd = statistics.stdev(dataset)
print("mean of the sample is ",samplemean)
print("standard deviation of the sample is ",samplestd)
graph = ff.create_distplot([dataset],["temp"],show_hist=False)
graph.show()"""
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    samplemean = statistics.mean(dataset)
    return samplemean
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    graph = ff.create_distplot([df],["reading_time"],show_hist=False)
    graph.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode="lines",name="MEAN"))
    graph.show()
def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    std = statistics.stdev(mean_list)
    print("mean of the sample distribution is ",mean)
    print("standard Deviation of sample distribution is ",std)
setup()


