library(shiny)

source("gui/ui_logic/sidebar/options.R")

analysismenu <- function(id, label="analysismenu") {
ns = NS(id)
menuItem(
    "Analysis",
    id = "analysisbtn",
    icon = icon("chart-bar"),
    startExpanded = FALSE,
    menuSubItem(
        icon = NULL,
        list(
            div(
                class = "div_step div_n_genes",
                list(
                    sliderInput(
                        ns("mark_markers_n"),
                        "Select number of genes",
                        min = 1, max = 500, value = 50
                    ),
                    splitLayout(
                        cellWidths = c("50%", "50%"),
                        textInput(
                            ns("mark_alpha"),
                            label = "alpha",
                            value = defaults$mark_alpha
                        ),
                        selectInput(
                            ns("mark_correction"),
                            "Correction",
                            choices = options$correction
                        )
                    ),
                    splitLayout(
                        cellWidths = c("50%", "50%"),
                        selectInput(
                            ns("subset1"),
                            "Choose Subset 1",
                            choices = c("")
                        ),
                        selectInput(
                            ns("subset2"),
                            "Choose Subset 2",
                            choices = c("")
                        )
                    ),
                    actionButton(
                        ns("getdegenes"),
                        "Run DE analysis",
                        class="longbtn"
                    )
                )
            ),

            div(
                class = "div_step div_genecard",
                list(
                    uiOutput("genecard"),
                    htmlOutput("inc"),
                    splitLayout(
                        textInput(
                            ns("searchgene"),
                            "Search Gene card",
                            placeholder = "Enter gene"
                        ),
                        actionButton(
                            ns("search"),
                            "Search Card",
                            class = "secondcol"
                        )
                    )
                )
            )

            # splitLayout(
            #     cellWidths = c("40%", "40%", "20%"),
            #     actionButton("subset1", "Store Subset 1", class = "sidebtn"),
            #     actionButton("subset2", "Store Subset 2",
            #                  class = "sidebtn scdbtn"),
            #     actionButton("DEsubsets", "DE", class = "sidebtn scdbtn")
            # ),

            # splitLayout(
            #     cellWidths = c("50%", "50%"),
            #     selectInput("chgcluster","Cluster to Rename",choice = 0),
            #     textInput("newcluster", "New Name", value = "",
            #               width = NULL, placeholder = NULL)
            # ),
            # actionButton("chg","Apply Change"),
            #actionButton("disable","Disable buttons"),



            # actionButton("runanalysis", "Run analysis for clusters",
            #              class="sidebtn longbtn")
        )
    )
)}