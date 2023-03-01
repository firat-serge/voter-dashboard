library(jsonlite)

#######data

election <- fromJSON("http://127.0.0.1:5000/votes_geojson")

election[["geojson"]] <- st_as_sf(election[["geojson"]], GeoJSON = TRUE, crs = 4326)

election[["geojson"]] <- as.numeric(election[["geojson"]])

head(election[["geojson"]], n =1)

election$geojson <- st_as_sfc(election$geojson)

st_as_sfc(election, GeoJSON=TRUE)

st_read(election[["geojson"]])

geos_polygons <- sapply(election$geojson, function(x) st_multipolygon(matrix(eval(str2lang(x)), ncol = 2)), USE.NAMES = FALSE)


election2 <- unlist(election1)

readOGR(election[["geojson"]])

library(jsonlite)

# url with some information about project in Andalussia
url <- 'http://127.0.0.1:5000/votes_geojson'

# read url and convert to data.frame
document <- fromJSON(txt=url)


map <- readOGR("C:/Users/firat/Downloads/demo/data/static/data.shp")

data <- read.csv("C:/Users/firat/Downloads/demo/data/original/data.csv")

library(dplyr)

data <- data %>% 
  rename("Nr_of_Votes" = "Valid_Votes",
         "Valid_Vote" = "Voters")


data <- data %>% 
  mutate(AKP_per = (AKP/Valid_Vote)*100,
         MHP_per = (MHP / Valid_Vote)*100,
         HUDA_PAR_per = (MHP / Valid_Vote)*100,
         VP_per = (VP / Valid_Vote) *100,
         HDP_per = (HDP / Valid_Vote)*100,
         CHP_per = (CHP / Valid_Vote) *100,
         SP_per = (SP / Valid_Vote) *100,
         IYIP_per = (IYIP / Valid_Vote) *100,
         INDP_per = (INDP / Valid_Vote) *100)


data <- map %>% 
  rename("Nr_of_Votes" = "Valid_Votes",
         "Valid_Vote" = "Voters")





