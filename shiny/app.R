#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(shinyWidgets)

my_choices <- c(
  "2018Q1","2018Q2","2018Q3", "2018Q4", "2019Q1", "2019Q2")



# Define UI for application that draws a histogram
ui <- fluidPage(
   
   # Application title
   titlePanel("Old Faithful Geyser Data"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
         sliderInput("bins",
                     "Number of bins:",
                     min = 1,
                     max = 50,
                     value = 30)
      ),
      
      # Show a plot of the generated distribution
      mainPanel(
         plotOutput("distPlot")
      )
   ),
   
   pickerInput(
     inputId = "id",
     label = "SELECT PERIOD:",
     choices = my_choices,
     selected = NULL,
     multiple = TRUE, 
     options = list(
       `actions-box` = TRUE, size = 15, `selected-text-format` = "count > 3"
     ),
     choicesOpt = list(
       content = stringr::str_trunc(my_choices, width = 75)
     )
   ),
   verbatimTextOutput(outputId = "res")

)

# Define server logic required to draw a histogram
server <- function(input, output, session) {
   
   output$distPlot <- renderPlot({
      # generate bins based on input$bins from ui.R
      x    <- faithful[, 2] 
      bins <- seq(min(x), max(x), length.out = input$bins + 1)
      
      # draw the histogram with the specified number of bins
      hist(x, breaks = bins, col = 'darkgray', border = 'white')
      
      observe({
        assign(
          x = "your_global_variable", 
          value = input$id, 
          envir = .GlobalEnv
        )
      })
      })
}

# Run the application 
shinyApp(ui = ui, server = server)








