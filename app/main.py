# __author__ = 'Ravi Bhavsar'
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import boto3
import json

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_active: bool

@app.get("/")
def index():
    try:
        acct_id = 576202454
        lambda_region = "us-west-2"
        get_license_capabilities_arn = "arn:aws:lambda:us-west-2:833926522372:function:customer_provisioning_service_get_license_aggr_ctxt"
        payload = {
                "body": {
                    "tenant_id": 576202454
                }
            }
        client = boto3.client('lambda', region_name=lambda_region)
        response = client.invoke(
                FunctionName=get_license_capabilities_arn,
                InvocationType="RequestResponse",
                LogType='None',
                Payload=json.dumps(payload).encode('utf-8')
            )
        response_payload = json.loads(response['Payload'].read())
        print(f"get license capabilities response {response_payload} for acct_id = {acct_id}")
    except Exception as ex:
        print(f"ex = {str(ex)}")
    return {"title" : "Hello coder follower, please like this video!" , "error" : str(ex)}

@app.post("/items/")
async def create_item(item: Item):
    if item.name is None or item.name == '':
        raise HTTPException(status_code=400, detail="Invalid item data")
    return {"message": "Item created successfully", "item": item}
