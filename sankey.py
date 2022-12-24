import plotly.graph_objects as go

label = [
  "Josh", 
  "James", 
  "Fraser",
  "Stephen",
  "Gubz", 
  "Jesse",
  "Eddie",
  "Torin",
  "Marko",
  "1st preference",
]

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label=label,
      color = "blue"
    ),
    link = dict(
      source = [9, 9, 9, 9, 9, 1, 3,6,],
      target = [1,2, 8, 6, 3, 2, 2, 2],
      value = [1,3, 4, 3, 1, 1, 1, 3]
  ))])

fig.update_layout(title_text="Preference Flows for Secret Santa", font_size=10)
fig.show()
