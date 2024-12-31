from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - student-collection2-coll-f51a81ee16f548378ba3f61ed5b32d84',debug=False,docs_url='/vibrant-fermi-ac4e14dcc6b111efa78e0242ac12000231/docs',openapi_url='/vibrant-fermi-ac4e14dcc6b111efa78e0242ac12000231/openapi.json')

app.include_router(router, prefix='/vibrant-fermi-ac4e14dcc6b111efa78e0242ac12000231/api', tags=['APIs v1'])

def main():
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True)

if __name__ == '__main__':
    main()