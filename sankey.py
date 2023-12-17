import plotly.graph_objects as go
from datetime import datetime

label = [
    "Josh",
    "James",
    "Fraser",
    "Stephen",
    "Gubz",
    "Jesse",
    "Eddie",
    "Sam",
    "Torin",
    "Marko",
    "1st preference",
]

fig = go.Figure(
    data=[
        go.Sankey(
            node=dict(
                pad=15,
                thickness=20,
                line=dict(color="black", width=0.5),
                label=label,
                color="blue",
            ),
            link=dict(
                source=[10] * 5 + [7, 8, 8, 1],
                target=[1, 3, 7, 8, 9, 9, 9, 3, 3],
                value=[2, 6, 1, 2, 2, 1, 1, 1, 2],
            ),
        )
    ]
)

fig.update_layout(
    title_text=f"Preference Flows for Secret Santa {datetime.utcnow().year}",
    font_size=10,
)
fig.show()
