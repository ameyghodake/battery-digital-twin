import plotly.graph_objects as go
import pandas as pd

df= pd.read_excel("output_df.xlsx")

fig = go.Figure()
fig.add_trace(go.Line(x=df['cycle'].iloc[:30000:20], y=df['soh_pred'].iloc[:30000:20], mode='lines', name='SOH', marker=dict(size=2, color='red')))
# fig.add_trace(go.Line(x=df['cycle'], y=df['soh_pred'], mode='lines', name='SOH', marker=dict(size=2, color='red')))
fig.update_layout(title='State Of Health [SOH] Distribution', xaxis_title='Cycle Index', yaxis_title='SOH', width=1200, height=600 )
plot_json = fig.to_json()
fig_1 = go.Figure()
fig_1.add_trace(go.Scatter(x=df['time'].iloc[:30000], y=df['temp_pred'].iloc[:30000], mode='markers', name='Temperature', marker=dict(size=2, color='green')))
# fig_1.add_trace(go.Line(x=df['time'], y=df['temp_pred'], mode='markers', name='Temperature', marker=dict(size=2, color='green')))
fig_1.update_layout(title='Temperature Distribution with respect to Time', xaxis_title='Time [sec]', yaxis_title='Temperature', width=1200, height=600 )
plot_json_1 = fig_1.to_json()
fig_2 = go.Figure()
fig_2.add_trace(go.Line(x=df['index'].iloc[:3000], y=df['soc_pred'].iloc[:3000], mode='lines', name='SOC'))
# fig_2.add_trace(go.Line(x=df['index'], y=df['soc_pred'], mode='lines', name='SOC'))
fig_2.update_layout(title='State of Charge [SOC]', xaxis_title='time [sec]', yaxis_title='SOC', width=1200, height=600 )
plot_json_2 = fig_2.to_json()