import boto3
from datetime import datetime, timedelta

def get_monthly_cost():
    client = boto3.client('ce')  # Cost Explorer
    end = datetime.today().replace(day=1)
    start = (end - timedelta(days=30)).replace(day=1)
    
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': start.strftime('%Y-%m-%d'),
            'End': end.strftime('%Y-%m-%d')
        },
        Granularity='MONTHLY',
        Metrics=['UnblendedCost'],
    )
    
    amount = response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    print(f"AWS cost from {start.date()} to {end.date()}: ${float(amount):.2f}")

if __name__ == "__main__":
    get_monthly_cost()
