import pandas as pd
import numpy as np
import plotly_express as px
import plotly.figure_factory as ff
import seaborn as sns
import statistics as st
data_file = pd.read_csv("c112-c113/savings.csv")

data_file_quant_saved = data_file["quant_saved"].tolist()
data_file_age = data_file["age"].tolist()


correlation = np.corrcoef(data_file_quant_saved, data_file_age)
print(correlation[0, 1])

data_file_plot_graph = px.scatter(data_file, x=data_file_age, y=data_file_quant_saved)
# data_file_plot_graph.show()

fig = ff.create_distplot([data_file_quant_saved], ["quantitysaved"], show_hist=False)
# fig.show()

# to draw a boxplot to check the outliers
ax = sns.boxplot(data=data_file, x= data_file["quant_saved"])

q1 = data_file["quant_saved"].quantile(0.25)
q3 = data_file["quant_saved"].quantile(0.75)
iqr = q3 -q1

lw  = q1-1.5*iqr
uw  = q3+1.5*iqr

print(lw ,uw)

new_data = data_file[data_file["quant_saved"]<uw]

new_savings = new_data["quant_saved"].tolist()

new_savings_mean = st.mean(new_savings)

new_savings_std = st.stdev(new_savings)

print("mean = "+str(new_savings_mean) + "  stdev = "+ str(new_savings_std))

# new_savings_displot = ff.create_distplot([new_savings], ["quantitysaved"], show_hist=False)
# new_savings_displot.show()

# temp_age = new_data[new_data.age != 0]

# new_age = temp_age["age"].tolist()

# temp_savings = temp_age["quant_saved"].tolist()