from typing import List,Optional

from app.db.repositories.base import BaseRepository
from app.models.core import AccumulatedInfo,  PostalCodesInfo

from datetime import date  

import json

CALCULATE_ACCUMULATED_QUERY = """
    SELECT sum(ranges_info.amount) as total, json_agg(ranges_info)::text as ranges
    FROM (
        SELECT p_age as range, p_gender as gender, sum(amount) as amount         
        FROM paystats       
        WHERE p_month >= :startdate and p_month <= :enddate       
        GROUP BY (p_age,p_gender)
    ) as ranges_info;
"""

CALCULATE_TIMESERIES_QUERY = """
    SELECT sum(ranges_info.amount) as total, json_agg(ranges_info)::text as ranges
    FROM (
        SELECT p_age as range, p_gender as gender, sum(amount) as amount         
        FROM paystats       
        WHERE p_month >= :startdate and p_month <= :enddate       
        GROUP BY (p_age,p_gender)
    ) as ranges_info;
"""

GET_POSTAL_CODES_GEOM_QUERY = """
    select pc.id,pc.code,ST_AsWKB(pc.the_geom) as geom, coalesce(stats.total,0) as total
    from postal_codes pc
    left join (
        SELECT ps.postal_code_id as codeid, sum(ps.amount) as total 
        from paystats ps 
        where ps.p_month >= :startdate and ps.p_month <= :enddate
        group by ps.postal_code_id
    ) stats ON pc.id = stats.codeid
"""


class CoolGeoAppRepository(BaseRepository):

    async def calculate_accumulated(self, *, startdate: date, enddate: date) -> AccumulatedInfo:
        query_values = {"startdate":startdate, "enddate":enddate}
        total = 0
        ranges = []
        try:
            row = await self.db.fetch_one(query=CALCULATE_ACCUMULATED_QUERY, values=query_values)        
            total = row[0]
            ranges = json.loads(row[1])
        except ConnectionError as exc:
            raise RuntimeError("Failed to connect with the database") from exc
         
        return AccumulatedInfo(total=total,ranges=ranges)
 

    async def get_postal_codes(self, *, startdate: date, enddate: date) -> PostalCodesInfo:
        query_values = {"startdate":startdate, "enddate":enddate}
        postalcodes = []
        try:
            records = await self.db.fetch_all(query=GET_POSTAL_CODES_GEOM_QUERY, values=query_values)

            for row in records:
                element = {
                    "id": row[0],
                    "code": row[1],
                    "geom": row[2],
                    "total": row[3]
                }
                postalcodes.append(element)
            
        except ConnectionError as exc:
            raise RuntimeError("Failed to connect with the database") from exc

        return PostalCodesInfo(postalcodes=postalcodes)

