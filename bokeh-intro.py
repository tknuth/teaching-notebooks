# +
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
import altair as alt

output_notebook()

# +
from random import randrange
from numpy.random import randint

plot = figure(width=400, height=400)

n = 10
x = list(range(n))
y = randint(1, 10, size=n)

# Der Plot erlaubt verschiedene Methoden, um Objekte (Glyphen) zu zeichnen
# Hier werden die Daten/Koordinaten als Listen (x, y) übergeben
plot.circle(x, y, size=10, color="red", alpha=0.5)

show(plot)

# +
plot = figure(width=400, height=400)

plot.line(x, y, line_width=2)

show(plot)

# +
from random import randrange
from numpy.random import randint

plot = figure(
    width=400,
    height=400,
    y_range=(min(y) - 1, max(y) + 1),
    x_range=(min(x) - 1, max(x) + 1),
)

plot.circle(x, y, size=10, color="red", alpha=0.5)

# Die verschiedenen Formen sind hier aufgezählt:
# https://docs.bokeh.org/en/latest/docs/reference/plotting/figure.html
plot.text(x, y, y, x_offset=5, y_offset=-5)

show(plot)

# +
y_with_nan = list(y)
y_with_nan[3] = float("nan")

plot = figure(width=400, height=400)

plot.line(x, y_with_nan, line_width=2)
plot.circle(x, y_with_nan, fill_color="white", size=8)

show(plot)

# +
import numpy as np

plot = figure(width=400, height=400)

plot.hspan([1, 3, 4], line_width=2, line_color="grey", alpha=0.5)
plot.vspan([1, 2, 4], line_width=2, line_color="grey", alpha=0.5)

show(plot)

# +
plot = figure(width=400, height=400)

# Der Plot erlaubt verschiedene Methoden, um Objekte (Glyphen) zu zeichnen
# Hier werden die Daten/Koordinaten als Listen (x, y) übergeben
plot.circle(x, y, size=y**2, color="red", alpha=0.5)

show(plot)

# +
from bokeh.transform import linear_cmap
from bokeh.models import ColumnDataSource

plot = figure(width=400, height=400)

source = ColumnDataSource({"x": x, "y": y})

plot.circle("x", "y", size=20, alpha=0.5, source=source)

show(plot)

# +
# from bokeh.palettes import Inferno256
from bokeh.transform import linear_cmap

plot = figure(width=400, height=400)

source = ColumnDataSource({"x": x, "y": y, "size": y**2})

# https://docs.bokeh.org/en/latest/docs/reference/palettes.html
cmap = linear_cmap("y", "Inferno256", min(y), max(y))

circles = plot.circle("x", "y", size="size", color=cmap, alpha=0.5, source=source)

color_bar = circles.construct_color_bar(width=10, title="Temperature")

plot.add_layout(color_bar, "right")

show(plot)

# +
from bokeh.transform import factor_mark, factor_cmap
from bokeh.palettes import Category10

plot = figure(width=400, height=400)

# https://docs.bokeh.org/en/latest/docs/user_guide/basic/scatters.html
markers = ["circle", "triangle", "hex"]

m = list(map(str, y % 3))
source = ColumnDataSource({"x": x, "y": y, "m": m})

factors = sorted(map(str, set(source.data["m"])))
fmark = factor_mark("m", markers, factors)
fcmap = factor_cmap("m", "Category10_3", factors)

plot.scatter("x", "y", color=fcmap, marker=fmark, size=20, alpha=0.5, source=source)

show(plot)

# +
from bokeh.models import Range1d

plot = figure(width=400, height=400, x_range=(0, 10))

source = ColumnDataSource({"x": x, "y": y, "m": m})

plot.circle(x="x", y="y", size=10, source=source)

plot.y_range = Range1d(0, 10, bounds=(0, 11))

show(plot)

# +
from datetime import datetime

now = datetime.now()
ts = now.timestamp()

n = 12
x = ts * 1000 + np.arange(n) * 60 * 60 * 24 * 1000 * 30
y = np.arange(n) + np.random.randn(n)

plot = figure(width=400, height=400, x_axis_type="datetime")

plot.line(x, y)

show(plot)

# +
activities = ["tennis", "golf", "soccer", "running", "badminton"]

# plot = figure(width=400, height=400)
plot = figure(width=400, height=400, x_range=activities)

counts = [1, 4, 3, 5, 2]

# plot.vbar([0, 1, 2, 3, 4], top=counts)
plot.vbar(activities, top=counts, width=0.5)

plot.xgrid.grid_line_color = None
plot.y_range.start = 0

show(plot)

# +
activities = ["tennis", "golf", "soccer", "running", "badminton"]

counts = [1, 4, 3, 5, 2]

sorted_activities = sorted(activities, key=lambda x: counts[activities.index(x)])

plot = figure(width=400, height=400, x_range=sorted_activities)

plot.vbar(activities, top=counts, width=0.5)

plot.xgrid.grid_line_color = None
plot.y_range.start = 0

show(plot)

# +
years = ["2020", "2021", "2022"]

data = {
    "activities": activities,
    "2020": [1, 1, 5, 8, 4],
    "2021": [2, 3, 5, 9, 5],
    "2022": [1, 2, 6, 8, 5],
}

plot = figure(
    x_range=activities,
    width=400,
    height=400,
    tools="hover",
    tooltips="$name @activities: @$name",
)

# Eine Farbe entspricht einem Jahr.
# Dies ist eine andere Verwendung als mit factor_cmap.
# Die Liste `years` selektiert die Spalten aus der CDS.
plot.vbar_stack(
    years,
    x="activities",
    color=Category10[3],
    legend_label=years,
    width=0.5,
    source=data,
)

plot.y_range.start = 0
plot.x_range.range_padding = 0.1
plot.xgrid.grid_line_color = None
plot.axis.minor_tick_line_color = None
plot.outline_line_color = None
plot.legend.location = "top_left"
# plot.legend.orientation = "horizontal"

show(plot)

# +
from bokeh.models import FactorRange, Legend
from bokeh.plotting import figure, show
import math

factors = [
    ("Q1", "01"),
    ("Q1", "02"),
    ("Q1", "03"),
    ("Q2", "04"),
    ("Q2", "05"),
    ("Q2", "06"),
    ("Q3", "07"),
    ("Q3", "08"),
    ("Q3", "09"),
    ("Q4", "10"),
    ("Q4", "11"),
    ("Q4", "12"),
]

regions = ["Bachelor", "Master"]

source = ColumnDataSource(
    data=dict(
        x=factors,
        Bachelor=[3, 2, 6, 7, 6, 3, 5, 3, 9, 8, 3, 2],
        Master=[1, 3, 4, 5, 7, 1, 4, 2, 3, 4, 6, 9],
    )
)

plot = figure(x_range=FactorRange(*factors), height=250, width=500)

plot.add_layout(Legend(), "right")
plot.vbar_stack(
    regions,
    x="x",
    width=0.8,
    color=Category10[3][:2],
    source=source,
    legend_label=regions,
)

plot.y_range.start = 0
plot.y_range.end = 14
plot.x_range.range_padding = 0.1
plot.xaxis.major_label_orientation = math.pi / 4
plot.xgrid.grid_line_color = None
plot.yaxis.minor_tick_line_color = None

show(plot)

# +
from bokeh.layouts import gridplot

x = list(range(10))
y = x[:]

plot1 = figure(height=250, width=250, background_fill_color="#fafafa")
plot1.circle(x, y, color=Category10[4][0], size=10)

plot2 = figure(height=250, width=250, background_fill_color="#fafafa")
plot2.scatter(x, y, marker="star", color=Category10[4][1], size=10)

plot3 = figure(height=250, width=250, background_fill_color="#fafafa")
plot3.scatter(x, y, marker="hex", color=Category10[4][2], size=10)

plot4 = figure(height=250, width=250, background_fill_color="#fafafa")
plot4.scatter(x, y, marker="triangle", color=Category10[4][3], size=10)

grid = gridplot([[plot1, plot2], [plot3, plot4]])

show(grid)

# +
from bokeh.io import export_svg

export_svg(grid, filename="plot.svg")

# +
from sklearn.datasets import load_iris
import pandas as pd

data = load_iris(as_frame=True)

df = data.data
df["y"] = data.target

# ":N" markiert eine nominale Variable; sonst würden die Klassen als numerische Werte interpretiert werden
alt.Chart(df).mark_circle().encode(
    x="sepal length (cm)", y="sepal width (cm)", color="y:N"
)

# +
plot1 = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="sepal length (cm)", y="sepal width (cm)", color="y:N")
)
plot2 = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="sepal length (cm)", y="petal width (cm)", color="y:N")
)

# Mit "|" nebeneinander, mit "&" übereinander
plot1 | plot2

# +
variables = [
    "sepal width (cm)",
    "sepal length (cm)",
    "petal width (cm)",
    "petal length (cm)",
]

# Die SPLOM ist etwas schwieriger in Bokeh:
# https://docs.bokeh.org/en/latest/docs/user_guide/topics/stats.html#ug-topics-stats
alt.Chart(df).mark_circle().encode(
    alt.X(alt.repeat("column"), type="quantitative"),
    alt.Y(alt.repeat("row"), type="quantitative"),
    color="y:N",
).properties(width=125, height=125).repeat(row=variables, column=variables)
