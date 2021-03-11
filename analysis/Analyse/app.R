library(shiny)
library(shinydashboard)
library(plotly)


ui <- dashboardPage(
    dashboardHeader(
        titleWidth = 300,
        title = 'Dashboard'),
    dashboardSidebar(
        width = 300,
        sidebarMenu(
            menuItem("Distribution par Gender", 
                     tabName = "lunettes_gender"),
            menuItem("Anne d'expedition des lunettes", 
                     tabName = "annee_lunettes"),
            menuItem("Catégorie des lunettes par\n ans d'expedition", 
                     tabName = "categorie_ans"),
            menuItem("Densite Taille par Gender", 
                     tabName = "taille_gender"),
            menuItem("Proportions Material par Marque", 
                     tabName = "material_marque"),
            menuItem("Categorie par ans", 
                     tabName = "categorie_marque")
        )
    ),
    dashboardBody(
        tabItems(
            tabItem(tabName = "lunettes_gender", 
                    fluidRow(
                        column(width = 12,
                               box(width = 12,
                                   plotOutput('lunettes_gender')
                               )))
            ),
            tabItem(tabName = "annee_lunettes", 
                    fluidRow(
                        column(width = 12,
                                box(width = 12,
                                    plotOutput('annee_lunettes')
                        )))
                    ),
            tabItem(tabName = "categorie_ans", 
                    fluidRow(
                        column(width = 12,
                               box(width = 12,
                                   plotlyOutput('categorie.ans')
                               ))
            )),
            tabItem(tabName = "taille_gender", 
                    fluidRow(
                        column(width = 12,
                               box(width = 12,
                                   plotOutput('taille.gender')
                               ))
            )),
            tabItem(tabName = "material_marque", 
                    fluidRow(
                        column(width = 12,
                               box(width = 12,
                                   plotlyOutput('material.marque')
                               ))
            )),
            tabItem(tabName = "categorie_marque", 
                    fluidRow(
                        column(width = 12,
                               box(width = 12,
                                   plotlyOutput('categorie.marque')
                               ))
            ))
    )
))


server <- function(input, output) {
    output$lunettes_gender <- 
        renderPlot(lunettes_gender)
    output$annee_lunettes <- 
        renderPlot(annee_lunettes)
    output$categorie.ans <- 
        renderPlotly(categorie.ans)
    output$taille.gender <- 
        renderPlot(taille.gender)
    output$material.marque <- 
        renderPlotly(material.marque)
    output$categorie.marque <- 
        renderPlotly(categorie.marque)
}

shinyApp(ui, server)
