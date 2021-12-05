import matplotlib.pyplot as plt
import boto3
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

fig = go.Figure(go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
                  name='Share Prices (in USD)'))

fig.update_layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.show()

plt.savefig('test.png')
ACCESS_KEY = 'AKIA34C2RRHTKN6AXXV3'
SECRET_KEY = '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' 
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3.upload_file('test.png', 'redrevoraisebucket', 'test.png')

