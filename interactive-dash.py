import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, html, dcc
from jupyter_dash import JupyterDash
from scipy.stats.mstats import trimmed_var
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

def wrangle(filepath):
    
    #reading the data
    df=pd.read_csv(filepath)
    
    #subsetting the dataset
    mask=(df["TURNFEAR"]==1) & (df["NETWORTH"]<2_000_00)
    
    df=df[mask]
    
    return df

df=wrangle("data/SCFP2022.csv")

app=Dash(__name__)

app.layout=html.Div([
    
    #application title
    html.H1("Survey of Consumer Finance"),
    
    #bar chart elements
    html.H2("High Variance Features"),

    #bar chart
    dcc.Graph(id="bar_graph"),

    dcc.RadioItems(options=[{"label":"Trimmed", "value":True}, {"label":"Not Trimmed", "value":False}], value=True, id="trim-button"),
    html.H2("K-means Clustering"),
    html.H3("Number of Clusters (k)"),

    #slider for the number of cluster the user prefers
    dcc.Slider(min=2, max=12, step=1, value=2, id="kmeans-slider"),

    html.Div(id="metrics"),

    #pca scatterplot
    dcc.Graph(id="pca-scatter")
 ])

def get_high_var_features(trimmed=True, feature_names=True):

    """This function calculate variances/trimmed variances and return the top five variance features."""

    #removing outliers in the values
    if trimmed:
        top_five_var_features=df.apply(trimmed_var).sort_values().tail()
    else:
        top_five_var_features=df.var().sort_values().tail()

    #extracting feature names
    if feature_names:
        top_five_var_features=top_five_var_features.index.to_list()

    return top_five_var_features

@app.callback(Output("bar_graph", "figure"), Input("trim-button", "value"))
def serve_bar_chart(trimmed=True):

    #get features
    top_five_var_features=get_high_var_features(trimmed=trimmed, feature_names=False)

    #plotting the graph
    fig=px.bar(x=top_five_var_features,
              y=top_five_var_features.index, orientation="h")
    fig.update_layout(xaxis_title="Variance", yaxis_title="Features")
    fig.show()
    
    return fig

def get_model_metrics(trimmed=True, k=2, return_metrics=False):

    #get high variance features
    features=get_high_var_features(trimmed=trimmed, feature_names=True)

    #create feature metrics
    X=df[features]

    #build the model
    model=make_pipeline(StandardScaler(), KMeans(n_clusters=k, random_state=42))
    model.fit(X)

    if return_metrics:

        #calculate inertia
        inertia=model.named_steps["kmeans"].inertia_

        #calculate silhouette score
        ss=silhouette_score(X, model.named_steps["kmeans"].labels_)

        #put the metrics into a dataframe
        metrics={"inertia":round(inertia),
                "silhouette": round(ss, 2)}
        return metrics
    return model
    

@app.callback(Output("metrics", "children"),Input("trim-button", "value"), Input("kmeans-slider", "value"))
def serve_metrics(trimmed=True, k=2):

    #get metrics
    metrics=get_model_metrics(trimmed=trimmed, k=k, return_metrics=True)
    print(metrics)
    #add metrics into html elements
    text=[
        html.H3(f"Inertia:{metrics['inertia']}"),
        html.H3(f"Silhouette Score:{metrics['silhouette']}")
    ]
    
    return text

def get_pca_labels(trimmed=True, k=2):

    #get features
    features=get_high_var_features(trimmed=trimmed, feature_names=True)

    #create the feature matrix
    X=df[features]

    #transformer
    pca=PCA(n_components=2, random_state=42)
    x_t=pca.fit_transform(X)

    #dataframe
    x_pca=pd.DataFrame(x_t, columns=["PC1", "PC2"])

    #add labels
    model=get_model_metrics(trimmed=trimmed, k=k, return_metrics=False)
    x_pca["labels"]= model.named_steps["kmeans"].labels_.astype(str)
    x_pca.sort_values("labels", inplace=True)
    
    return x_pca

@app.callback(Output("pca-scatter", "figure"), Input("trim-button", "value"), Input("kmeans-slider", "value"))
def serve_scatter_plot(trimmed=True, k=2):

    fig=px.scatter(data_frame=get_pca_labels(trimmed=trimmed, k=k), 
                   x="PC1", 
                   y="PC2",
                   color="labels",
                  title="PCA: Representation of Clusters")
    fig.update_layout(xaxis_title="PC1", yaxis_title="PC2")
    fig.show()
    return fig



if __name__=="__main__":
    app.run_server(host="127.0.0.1", port="8050")