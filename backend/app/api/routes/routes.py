from typing import List,Optional
from fastapi import Request,APIRouter, Body,Query, Depends, HTTPException,status 
    
from app.models.core import AccumulatedInfo, PostalCodesInfo
from app.models.login import LoginUsr,UsrSession 
from app.db.repositories.coolgeoapp import CoolGeoAppRepository  
from app.api.dependencies.database import get_repository
# 
from datetime import date  

router = APIRouter()

######## Endpoint

@router.get(
    "/",
    name="Wellcome to the API",
    description="Wellcome endpoint",
    status_code=status.HTTP_200_OK
)
def greetings():
    return "Hi to coolGeoApp API  ;)"

######## Endpoint

@router.get(
    "/turnover/accumulated",
    name="Accumulated Turnover",
    description="Accumulated turnover of the all postal codes between two dates and by gender",
    status_code=status.HTTP_200_OK
)
async def accumulated(
    startdate: Optional[date] = Query(
        ..., 
        title="Start date",
        description="Start date",
        example="2015-01-01"
    ), 
    enddate: Optional[date] = Query(
        ..., 
        title="End date",
        description="End date",
        example="2015-10-07"
    ),
    coolGeoAppRepo: CoolGeoAppRepository = Depends(get_repository(CoolGeoAppRepository))
) -> AccumulatedInfo:    
    
    if startdate > enddate:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail="Startdate parameter cannot be greater than Enddate parameter"
        )  
    data = await coolGeoAppRepo.calculate_accumulated(startdate=startdate,enddate=enddate)    
    return data

######## Endpoint

@router.get(
    "/turnover/timeseries",
    name="Turnover time series between dates (Not implemented)",
    description="",
    status_code=status.HTTP_200_OK
)
async def timeSeries(
    startdate: Optional[date] = Query(
        ..., 
        title="Start date",
        description="Start date",
        example="2015-01-01"
    ), 
    enddate: Optional[date] = Query(
        ..., 
        title="End date",
        description="End date",
        example="2015-10-07"
    ),
    coolGeoAppRepo: CoolGeoAppRepository = Depends(get_repository(CoolGeoAppRepository))
) -> str:
    return "Not implemented"

######## Endpoint

@router.get(
    "/layers/postalcodes", 
    name="Postal codes geometries", 
    description="Get postal code geometries with their accumulated stats between two dates ", 
    status_code=status.HTTP_200_OK
)
async def postalCodes(
    startdate: Optional[date] = Query(
        ..., 
        title="Start date",
        description="Start date",
        example="2015-01-01"
    ), 
    enddate: Optional[date] = Query(
        ..., 
        title="End date",
        description="End date",
        example="2016-10-07"
    ),
    coolGeoAppRepo: CoolGeoAppRepository = Depends(get_repository(CoolGeoAppRepository))
) -> PostalCodesInfo:
    data = await coolGeoAppRepo.get_postal_codes(startdate=startdate,enddate=enddate)    
    return data

######## Endpoint

@router.get(
    "/turnover/postalcode/{postal_id}", 
    name="Postal code info by id (Not implemented)", 
    description="",
    status_code=status.HTTP_200_OK
)
async def postalCodeInfoById() -> str :
    return "Not implemented"

######## Endpoint

@router.get(
    "/layers/region", 
    name="Madrid region geometry (Not implemented)", 
    description="Get the whole region of Madrid with its statistics between dates",
    status_code=status.HTTP_200_OK
)
async def region() -> str:
    return 'Not implemented'

######## Endpoint

@router.post(
    "/login/signin", 
    response_model=UsrSession, 
    name="Sign In",
    description="Get a API session to use the other endpoints",
    status_code=status.HTTP_200_OK
)
async def signin(logi_usr: LoginUsr = Body(..., embed=True)) -> UsrSession:  
    session =   {
        "user":"visancal",
        "name":"Vicent Sanjaime",
        "token":"sgfdsdghdbgvsdkjfdvdfbjkghfddfjksghfdjkgbdfjkbv",
        "lang":"es"
    }
    return session

######## Endpoint

@router.post(
    "/login/signout", 
    name="Sign Out",
    description="Close your active session with the API", 
    status_code=status.HTTP_200_OK
)
async def signout() -> str:
    return "API session closed"