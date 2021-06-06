import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import statistics

data = pd.read_csv('medium_data.csv')
data = data['claps'].tolist()

Mean = statistics.mean(data)
Stdev = statistics.stdev(data)

def Sample(Number):
    dataSet = []
    for i in range(0,Number):
        index = random.randint(0,len(data)-1)
        Value = data[index]
        dataSet.append(float(Value))
    dataMean = statistics.mean(dataSet)
    return dataMean

MeanList = []
for i in range(0,30):
    SamplingValue = Sample(100)
    MeanList.append(float(SamplingValue))

SampleMean = statistics.mean(MeanList)
SampleStdev = statistics.stdev(MeanList)

FirstDeviation_Start, FirstDeviation_End = SampleMean + SampleStdev, SampleMean-SampleStdev
SecondDeviation_Start, SecondDeviation_End = SampleMean + 2*SampleStdev, SampleMean - 2*SampleStdev
ThirdDeviation_Start, ThirdDeviation_End = SampleMean + 3*SampleStdev, SampleMean - 3*SampleStdev

graph = ff.create_distplot([MeanList], ['Sampling'], show_hist = False)
graph.add_trace(go.Scatter(x = [SampleMean, SampleMean], y = [0,1], mode = "lines", name = "Mean" ))
graph.add_trace(go.Scatter(x =[FirstDeviation_Start, FirstDeviation_Start], y = [0,1], mode = "lines", name = "First Deviation Start"))
graph.add_trace(go.Scatter(x = [FirstDeviation_End, FirstDeviation_End], y = [0,1], mode = 'lines', name = "First Deviation End"))
graph.add_trace(go.Scatter(x = [SecondDeviation_Start,SecondDeviation_Start], y = [0,1], mode = 'lines', name = "Second Deviation Start"))
graph.add_trace(go.Scatter(x = [SecondDeviation_End, SecondDeviation_End], y = [0,1], mode = 'lines', name = "Second Deviation End"))
graph.add_trace(go.Scatter(x = [ThirdDeviation_Start, ThirdDeviation_Start], y = [0,1], mode = 'lines', name = "Third Deviation Start"))
graph.add_trace(go.Scatter(x = [ThirdDeviation_End, ThirdDeviation_End], y = [0,1], mode = 'lines', name = "Third Deviation End"))
graph.show()
ZScore = (Mean-SampleMean)/SampleStdev
print(ZScore)