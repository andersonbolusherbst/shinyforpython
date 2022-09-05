from shiny import App, render, ui
import numpy as np
import pandas as pd
#import your python libraries here


#what you put in app.ui appears in the browser
app_ui = ui.page_fluid(
    ui.h3({"style":"text-align:centre"},"Interactive Model For Marketing Analysis"),
    ui.output_text_verbatim("intro"),
    ui.h3({"style":"text-align:centre"},"Model Inputs"),
    ui.row(
    ui.column(4, 
            ui.h5({"style":"text-align:centre"},"Ad platform 1: Facebook"),
            ui.input_numeric("s", "Ad budget $",value=1000),
            ui.input_slider("n", "Estimated number of Impressions", 0, 10000, 2000),
            ui.input_slider("c", "Impression to site visit conversion rate / Click through rate",0, 1, 0.08),
            
             ),
    ui.column(4,
            ui.h5({"style":"text-align:centre"},"Ad platform 2: Google Search"),
            ui.input_numeric("s2", "Ad budget $",value=1000),
            ui.input_slider("n2", "Estimated number of Impressions", 0, 10000, 700),
            ui.input_slider("c2", "Impression to site visit conversion rate / Click through rate",0, 1, 0.15),
           
            ),
    ui.column(4,
            ui.h5({"style":"text-align:centre"},"Ad platform 3: Youtube"),
            ui.input_numeric("s3", "Ad budget $",value=2000),
            ui.input_slider("n3", "Estimated number of Impressions", 0, 10000, 1000),
            ui.input_slider("c3", "Impression to site visit conversion rate / Click through rate",0, 1, 0.075),
           
            ),
    ),
    
    ui.output_text_verbatim("sitevisits"),
    ui.input_slider("f", "Site to form submission rate", 0, 1, 0.1),
    ui.output_text_verbatim("formsubs"),
    ui.input_slider("w", "Lead to sale conversion rate", 0, 1, 0.07),
    ui.output_text_verbatim("sales"),
    ui.output_text_verbatim("cost_per_lead"),
    ui.output_text_verbatim("customer_acquisition_cost"),
        
)

#put your functional logic here
def server(input, output, session):
    @output
    @render.text
    def intro():
        return "This interactive model can be used to assess the risk and potential performance of a marketing campaign"   

    @output
    @render.text   
    def sitevisits():
        val= (input.n() * input.c()) + (input.n2() * input.c2()) + (input.n3() * input.c3())
        return   f'number of website visits: "{val}"'

    @output
    @render.text   
    def formsubs():
        val= (input.n() * input.c()) + (input.n2() * input.c2()) + (input.n3() * input.c3())
        subs= val * input.f()
        return   f'number of form submissions / leads: "{subs}"'

    @output
    @render.text   
    def cost_per_lead():
        val= (input.n() * input.c()) + (input.n2() * input.c2()) + (input.n3() * input.c3())
        subs= val * input.f()
        cpl= (input.s() + input.s2() + input.s3())  / subs
        return   f'cost per lead "{cpl}"'

    @output
    @render.text   
    def sales():
        val= (input.n() * input.c()) + (input.n2() * input.c2()) + (input.n3() * input.c3())
        subs= val * input.f()
        sales = subs * input.w()
        return   f'number of sales: "{sales}"'


    @output
    @render.text 
    def customer_acquisition_cost():
        val= (input.n() * input.c()) + (input.n2() * input.c2()) + (input.n3() * input.c3())
        subs= val * input.f()
        sales = subs * input.w()
        cac =  (input.s() + input.s2() + input.s3()) / sales
        return   f'cost per sale / customer acquisition cost: "{cac}"'
        
 


app = App(app_ui, server)
