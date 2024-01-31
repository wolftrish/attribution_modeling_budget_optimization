# function for plotting the graphs

def plotter(data, name):
    import matplotlib.pyplot as plt
    import seaborn as sns
    #Plotting the weightage with respect to channels
    plt.subplots(figsize=(18, 6))
    p=sns.barplot(y='Weightage(%)', x=data.index, data=data)
    p.set_title(name)
    p.figure.savefig(f"../output/{name}.png")    