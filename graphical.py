import matplotlib.pyplot as plt
import boto3
import pandas as pd
import plotly.graph_objects as go
import os

REQ = input()

BUCKET_NAME = 'redrevoraisebucket'
BUCKET_FILE_NAME = '{request}.csv'.format(request = REQ)
LOCAL_FILE_NAME = '{request}.csv'.format(request = REQ)

def download_s3_file():
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, BUCKET_FILE_NAME, LOCAL_FILE_NAME)

df = pd.read_csv('{request}.csv'.format(request = REQ))

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

