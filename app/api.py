from fastapi import FastAPI #importing FastAPI class
from routers import metrics, aws
app = FastAPI(
    title="Internal DevOps Utilities API",
    description="This is an Internal API Utilities App for Monitoring metrics, AWS usage",
    version="1.1.0",
    doc_url='/docs',
    redoc_url='/redoc' #readme attached
)

@app.get("/")
def hello():
    """
    This is a Hello API, just for testing
  
    """
    return {"message":"Hello everyone, This is DevOps Utilities API"}

app.include_router(metrics.router)

app.include_router(aws.router, prefix="/aws") #to use APi Group adding prefix = "/aws/s3"