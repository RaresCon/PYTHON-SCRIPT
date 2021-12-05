import matplotlib.pyplot as plt
import boto3
import pandas as pd
import plotly.graph_objects as go
import os

session = boto3.Session(
    ACCESS_KEY = 'AKIA34C2RRHTKN6AXXV3'
    SECRET_KEY = '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'
)

s3 = session.resource('s3')

REQ = input()
s3.Bucket('redrevoraisebucket').download_file('{request}'.format(request = REQ), '{request}.csv'.format(request = REQ))

df = pd.read_csv('{request}.csv').format(request = REQ)

fig = go.Figure(go.Scatter(x = df['Date'], y = df['High'],
                  name='Share Prices (in USD)'))

fig.update_layout(title='Apple Share Prices over time ({date})'.format(date = 'Date'),
                   plot_bgcolor='rgb(230,230,230)',
                   showlegend=True)

fig.show()

fig.write_image('{request}.jpeg'.format(request = REQ))
ACCESS_KEY = 'AKIA34C2RRHTKN6AXXV3'
SECRET_KEY = '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' 
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3.upload_file('{request}.jpeg'.format(request = REQ), 'redrevoraisebucket', '{request}.jpeg'.format(request = REQ))

os.remove('{request}.csv'.format(request = REQ))
os.remove('{request}.png'.format(request = REQ))

