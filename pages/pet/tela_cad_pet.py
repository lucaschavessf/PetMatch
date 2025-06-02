from dash import html, dcc
import dash_bootstrap_components as dbc

def return_layout():
    layout = dbc.Card([
    
        html.H1('CADASTRO DE PET',style={'display':'flex','align-items': 'center','justify-itemns':'center', 'color' : 'black'}),
        html.Hr(style={'color':'grey'}),
        html.Div(children=[
            html.H4('Espécie:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-cadpet-especie',options=[{'label':'Gato','value':'Gato'},{'label':'Cachorro','value':'Cachorro'},{'label':'Ave','value':'Ave'},{'label':'Réptil','value':'Réptil'},{'label':'Peixe','value':'Peixe'},{'label':'Outro','value':'Outro'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Estágio da vida:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-cadpet-estagio',options=[{'label':'Recém nascido','value':'Recém nascido'},{'label':'Filhote','value':'Filhote'},{'label':'Adulto','value':'Adulto'},{'label':'Velho','value':'Velho'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Porte:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-cadpet-porte',options=[{'label':'Pequeno','value':'Pequeno'},{'label':'Médio','value':'Médio'},{'label':'Grande','value':'Grande'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Deficiência:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-cadpet-deficiencia',options=[{'label':'Sim','value':'Sim'},{'label':'Não','value':'Não'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Para crianças:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-cadpet-criancas',options=[{'label':'Sim','value':'Sim'},{'label':'Não','value':'Não'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Pode viver com outros animais:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-cadpet-outros',options=[{'label':'Sim','value':'Sim'},{'label':'Não','value':'Não'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Temperamento:'),
            html.Div(children=[
                dbc.RadioItems(id='ri-cadpet-temperamento',options=[{'label':'Calmo','value':'Calmo'},{'label':'Brincalhão','value':'Brincalhão'},{'label':'Raivoso','value':'Raivoso'}],inline=True,inputStyle={"color": "black","background-color":'grey'}),
            ],style={'display':'flex', 'align-items': 'center','justify-itemns':'center'}),
            html.H4('Cor:'),
            html.Div(children=[
                dbc.Input(id='input-cadpet-cor',placeholder="Insira a Cor do PET",type='text', size="sm"),
            ],style={'display':'flex'}),
            html.H4('Raça:'),
            html.Div(children=[
                dbc.Input(id='input-cadpet-raca',placeholder="Insira a Raça do PET",type='text', size="sm"),
            ],style={'display':'flex'}),
            html.Div(children=[
                html.H4("Adicione uma imagem:",style={'margin-right':'10px'}),
                dcc.Upload(id='upload-image',children=html.Button('Upload de Imagem',style={'font-size':'12px','border-radius':'10px'}),multiple=False),
            ],style={'display':'flex','margin-top':'10px'}),
        ],style={'overflowY': 'auto'}),
        
        
        html.Hr(style={'margin-top': '3px','margin-bottom': '10px'}),
        html.Span(id='span-cadpet-aviso',style={'color':'#fd7e14','text-aling':'center'}),
        dbc.Button('ADICIONAR',id='btn-cadpet-add',color='primary')     
    ]
        ,style = {
            "height":"100%",
            "background-color" : "white",
            "padding":"20px"
        }
    )

    return layout