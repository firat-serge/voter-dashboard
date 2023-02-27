
import pandas as pd
import geopandas as gpd

DB_SCHEMA = "sa"
TABLE = "votes"
DOWNLOAD_DIR = "data/original"
PROCESSED_DIR = "data/processed"
STATIC_DIR = "data/static"


# Rename columns to match the database model

gdf = gpd.read_file('data/static/data.shp')

gdf = gdf.rename(columns={
    "Valid_Vote":"Voter",
    "Voters":"Valid_Votes",
    })

# Necessary calculations for percentage presentation of votes

gdf["AKP_per"] = (gdf["AKP"] / gdf["Valid_Votes"])*100
gdf["MHP_per"] = (gdf["MHP"] / gdf["Valid_Votes"])*100
gdf["HUDA_PAR_per"] = (gdf["HUDA_PAR"] / gdf["Valid_Votes"])*100
gdf["VP_per"] = (gdf["VP"] / gdf["Valid_Votes"])*100
gdf["HDP_per"] = (gdf["HDP"] / gdf["Valid_Votes"])*100
gdf["CHP_per"] = (gdf["CHP"] / gdf["Valid_Votes"])*100
gdf["SP_per"] = (gdf["SP"] / gdf["Valid_Votes"])*100
gdf["IYIP_per"] = (gdf["IYIP"] / gdf["Valid_Votes"])*100
gdf["INDP_per"] = (gdf["INDP"] / gdf["Valid_Votes"])*100



if __name__ == "__main__":
    config_file = parse_args()
    main(config_file)