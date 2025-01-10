import plotly.io as pio
import plotly.graph_objects as go
import pandas as pd

config = {
    'displaylogo': False,
    'displayModeBar': True,
    'scrollZoom': True,
    'toImageButtonOptions': {
        'format': 'svg',
        'filename': 'custom_image',
        'height': None,
        'width': None,
        'scale': 1
    },
    'modeBarButtonsToAdd': ['drawline',
                            'drawopenpath',
                            'eraseshape']
}

pio.templates.default = 'plotly_white'


# pd.options.plotting.backend = "plotly"

def plot_plotly(*df_cols):
    fig = go.Figure()

    for col in df_cols:
        if isinstance(col, pd.DataFrame):
            col = col.squeeze(axis=1)
        fig.add_trace(go.Scatter(x=col.index, y=col, name=col.name))
    fig.show(config=config)
