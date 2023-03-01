#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(rgdal)
library(leaflet)
library(jsonlite)
library(sf)
library(tibble)
library(geojsonsf)
library(shinydashboard)
library(leaflet)
library(leaflet.extras)
library(tidyverse)
library(plotly)
library(scales)
library(sf)
library(dashboardthemes)

# gather data

election <- fromJSON("http://127.0.0.1:5000/votes_geojson")

###Party Colors

partyColours <- data.frame(Party = c('AKP_per', 'CHP_per', 'HDP_per', 'MHP_per', 'IYIP_per', 'SP_per', 'Y_18', 'Hedu'),
                           colours = c('#D71920', '#1A4782', '#F58220', '#008080', "#3D9B35", "#4E5180", "#808080", "#808080"), 
                           stringsAsFactors = FALSE)


# Define UI for application that draws a histogram
ui <- dashboardPage(

    # Application title
    #titlePanel("Electoral Map for Turkey"),
    # Dashboard title
    dashboardHeader(title = "Turkish Elections Dashboard",
                    titleWidth = 350),
    # Sidebar Layout
    dashboardSidebar(width = 350,
                     sidebarMenu(menuItem("Country-Wide Analysis", tabName = "Turkey", icon = icon("canadian-maple-leaf")))),
    
    dashboardBody(
        
        # Change the theme
        shinyDashboardThemes(
            theme = "flat_red"
        ),
        
        tabItems(
            tabItem("turkey",
                    fluidRow(box(status = 'info', width = 12,
                                 title = strong("View Elections Across Turkey!"),
                                 splitLayout(cellWidths = c('25%', '25%', '48%'),
                                             tagList(HTML(paste("Please select the party <br/> you want to map"))),
                                             #radioButtons(inputId = 'parties', 'Election Year:', c('2015', '2019')),
                                             tagList(HTML(paste("Feel free to scroll the map to view individual ridings. When you <br/> 
                                             hover above a riding, the winning party's name will appear. Below <br/> 
                                             the map you will see the turkey-wide voting statistics in <br/> 
                                             your selected election.")))))))),     
    
    # Show Map
    
    mainPanel(
        leafletOutput("party")
        )
))

# Define server logic required to draw a histogram
server <- function(input, output) {

    output$party <- renderLeaflet({
        
        party <- leaflet()
        party <- addTiles(party)
        party <- addPolygons(party, data = map1, 
                             color = "red", 
            #label = c("ADMIN_NAME","AKP_per", "CHP_per"), 
            weight = 2,
            highlightOptions = 
     highlightOptions(color = "blue", bringToFront = TRUE, weight = 1,
                      ))
        
        
        
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
