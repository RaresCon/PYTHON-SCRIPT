import csv
import boto3
from boto3.dynamodb.conditions import Key

def addDynamoDB():
    dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
    table = dynamodb.Table("DataCollector") #Specify the table name and store it in a variable

    companies = ["GOOG", "AAPL", "AMZN", "INTC", "META", "NVDA", "AMD"]

    for ticker in companies:
        filepath = "{company}.csv".format(company = ticker)
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            # batch_writer()So, put all the CSV items 25 items at a time
            with table.batch_writer() as batch:
                for row in reader:
                    item = {
                        "Date": row[0],
                        "Open": row[1],
                        "High": row[2],
                        "Low": row[3],
                        "Close": row[4],
                        "Adj Close": row[5],
                        "Volume": row[6],
                    }
                    batch.put_item(Item=item)

if __name__ == "__main__":
    addDynamoDB()