library(shiny)

plots <- function(id, label='plots') {
ns = NS(id)
tabsetPanel(
    type = "tabs",
    id = "tabset",
    tabPanel(
        "Main Plot",
        h3(textOutput("caption")),
        plotlyOutput(ns("plot"), height="550px"),
    ),

    tabPanel(
        "Updated Plot",
        verbatimTextOutput("brush"),
        plotlyOutput(ns("Plot2"), height="550px"),
        downloadButton(ns("downlabels"), "Download updated labels")
    )
)}