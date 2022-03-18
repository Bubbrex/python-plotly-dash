import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
# pip install dash (version 2.0.0 or higher)
from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)

# Import Data

df = pd.read_excel("./data/footprint_criteria.xlsx", index_col=0,
                   dtype={"coef_val": "str", "coef_swiped": "str", "fz": "int32", "camber": "int32"})


# App Layout

options_coef_swiped = [
    {"label": "Belt in_plane bend stiffness",
        "value": "belt_in_plane_bend_stiffn"},
    {"label": "Belt_lateral bend stiffness", "value": "belt_lat_bend_stiffn"},
    {"label": "Belt torsion stiffness", "value": "belt_torsion_stiffn"},
    {"label": "Belt twist stiffness", "value": "belt_twist_stiffn"},
    {"label": "Belt width", "value": "belt_width"},
    {"label": "Rel long belt memb tension", "value": "rel_long_belt_memb_tension"}]

options_fz = [
    {"label": "Fz = 3400 N", "value": 3400},
    {"label": "Fz = 6900 N", "value": 6900},
    {"label": "Fz = 300 N", "value": 300}]

options_camber = [
    {"label": "Camber = 0\N{degree sign}", "value": 0},
    {"label": "Camber = 6\N{degree sign}", "value": 6}]
options_radio = [
    {"label":"One","value":1},
    {"label":"Two","value":2},
    {"label":"Three","value":3},
]
app.layout = html.Div([
    # Dash Title
    html.H1(
        "Footprint Result", 
        style={"text-align": "center"}),
    # First three dropdown menu
    html.Div(id="dropdown1",children=[
        html.H4("First Trace",style={"margin":"1rem"}),
        dcc.Dropdown(
            id="coef_swiped",
            className = "dropdown",
            options=options_coef_swiped,
            value="belt_in_plane_bend_stiffn",
            style={"width": "40%"}),
        dcc.Dropdown(
            id="fz",
            options=options_fz,
            className = "dropdown",
            value=3400,
            style={"width": "40%"}),
        dcc.Dropdown(
            id="camber", 
            options=options_camber,
            className = "dropdown",
            value=0, 
            style={"width": "40%"}),
        ]),
    # Radio buttons for more traces (1,2,3) in figure
    html.H4("Show more traces",style={"margin":"1rem"}),
    dcc.RadioItems(
        id="radio",
        className = "dropdown",
        options=options_radio,
        value=1,
    ),
    # Hidden Dropdown menus enabled by radio button correspondingly
    html.Div(id="dropdown2",children=[
        html.H4("Second Trace",style={"margin":"1rem"}),
        dcc.Dropdown(
                id="coef_swiped2",
                className = "dropdown",
                options=options_coef_swiped,
                value="belt_width",
                style={"width": "40%"}),
            dcc.Dropdown(
                id="fz2",
                options=options_fz,
                className = "dropdown",
                value=6900,
                style={"width": "40%"}),
            dcc.Dropdown(
                id="camber2", 
                options=options_camber,
                className = "dropdown",
                value=6, 
                style={"width": "40%"}),
    ]),
  
    # Another Hidden Dropdown menus
    html.Div(id="dropdown3",children=[
        html.H4("Third Trace",style={"margin":"1rem"}),
        dcc.Dropdown(
                id="coef_swiped3",
                className = "dropdown",
                options=options_coef_swiped,
                value="belt_in_plane_bend_stiffn",
                style={"width": "40%"}),
            dcc.Dropdown(
                id="fz3",
                options=options_fz,
                className = "dropdown",
                value=3400,
                style={"width": "40%"}),
            dcc.Dropdown(
                id="camber3", 
                options=options_camber,
                className = "dropdown",
                value=0, 
                style={"width": "40%"}),
    ]),
    
    # Slider
    html.Div(
        style={"width": "50%"},
        className="test" ,
        children=[
            dcc.Graph(id="my_graph", figure={} ,className = "graph"),
            html.Div(id="slider_info", style={"margin":"1rem"},children=[]),
            html.Div(id="slider",children=[
                dcc.Slider(0.5, 1.9, 0.1,id="coef_ratio", value=1.2)]),
            html.Div(id="slider2",children=[
                html.Div(id="slider_info2", style={"margin":"1rem"},children=[]),
                dcc.Slider(0.5, 1.9, 0.1,id="coef_ratio2", value=0.7)]),
            html.Div(id="slider3",children=[
                html.Div(id="slider_info3", style={"margin":"1rem"},children=[]),
                dcc.Slider(0.5, 1.9, 0.1, id="coef_ratio3", value=1.5)]),
            ]),
])

# Connect the graph and the components


@app.callback([
    Output(component_id='slider_info', component_property='children'),
    Output(component_id='slider_info2', component_property='children'),
    Output(component_id='slider_info3', component_property='children'),
    Output(component_id='my_graph', component_property='figure'),
    Output(component_id='dropdown2', component_property='style'),
    Output(component_id='dropdown3', component_property='style'),
    Output(component_id='slider2', component_property='style'),
    Output(component_id='slider3', component_property='style'),],     
    [
    Input(component_id='coef_swiped', component_property='value'),
    Input(component_id='fz', component_property='value'),
    Input(component_id='camber', component_property='value'),
    Input(component_id='coef_ratio', component_property='value'),
    Input(component_id='coef_swiped2', component_property='value'),
    Input(component_id='fz2', component_property='value'),
    Input(component_id='camber2', component_property='value'),
    Input(component_id='coef_ratio2', component_property='value'),
    Input(component_id='coef_swiped3', component_property='value'),
    Input(component_id='fz3', component_property='value'),
    Input(component_id='camber3', component_property='value'),
    Input(component_id='coef_ratio3', component_property='value'),
    Input(component_id='radio', component_property='value')]
)
def update_graph(coef_swiped, fz, camber, coef_ratio,coef_swiped2, fz2, camber2, coef_ratio2,coef_swiped3, fz3, camber3, coef_ratio3,radio):
    
    print(coef_ratio,coef_ratio2,coef_ratio3)

    dropdown2= {"display":"none"}
    slider2 = {"display":"none"}
    dropdown3 = {"display":"none"}
    slider3 = {"display":"none"}
    coef_val = 0
    coef_val2 = 0
    coef_val3 = 0

    if radio >=2:
        
        dropdown2 = {"display":"block"}
        slider2 = {"display":"block"}
        if radio == 3:
            dropdown3 = {"display":"block"}
            slider3 = {"display":"block"}


    def getXY(coef_swiped,fz,camber,coef_ratio):
        dff = df.copy()
        dff = dff[dff["coef_swiped"] == coef_swiped]
        dff = dff[dff["fz"] == fz]
        dff = dff[dff["camber"] == camber]
        dff = dff[dff["coef_ratio"] == coef_ratio]
        coef_val = dff.iloc[0]["coef_val"]
        file = dff.iloc[0]["file"]
        current_path = "./data/" + coef_swiped + "/" + \
            str(coef_val).replace(
            ".", "_") + "/"+str(file)
        dfx = pd.read_fwf(current_path)
        return dfx, coef_val


    fig = go.Figure()

    dfx,coef_val = getXY(coef_swiped,fz,camber,coef_ratio)
    fig.add_trace(go.Scatter(
        visible=True,
        x=dfx.x_ftire,
        y=dfx.y_ftire,
        line=go.scatter.Line(color="rgba(93,172,129,0.8)",width=5),
        name="First Trace"
        ))
    if radio >= 2:
        dfx2,coef_val2 = getXY(coef_swiped2,fz2,camber2,coef_ratio2)
        fig.add_trace(go.Scatter(
            visible=True,
            x=dfx2.x_ftire,
            y=dfx2.y_ftire,
            line=go.scatter.Line(color="gray",width=5),
            name="Second Trace"
        ))
 
        if radio == 3:
            dfx3,coef_val3 = getXY(coef_swiped3,fz2,camber3,coef_ratio3)
            fig.add_trace(go.Scatter(
                visible=True,
                x=dfx3.x_ftire,
                y=dfx3.y_ftire,
                line=go.scatter.Line(color="blue",width=5),
                 name="Third Trace"
            ))
            
    slider_info = "The coefficient value is {}".format(coef_val)  
    slider_info2 = "The coefficient value is {}".format(coef_val2)    
    slider_info3 = "The coefficient value is {}".format(coef_val3)    

    

    fig.update_layout(
        height = 550,
        title_text="Result",
        title_xanchor="center",
        title_x=0.5
    )

    return slider_info,slider_info2,slider_info3, fig,dropdown2,dropdown3,slider2,slider3


# Run the dash
if __name__ == "__main__":
    app.run_server(debug=True)