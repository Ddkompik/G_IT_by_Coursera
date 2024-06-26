from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

from reportlab.lib.units import inch


styles = getSampleStyleSheet()
report = SimpleDocTemplate("C:\\Users\\dasha\\Documents\\CODE\\GitHub\\G_IT_by_Coursera\\AutoPython\\report.pdf")
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report.build([report_title])

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

table_data = []
for val, count in fruit.items():
    table_data.append([val,count])

report_table = Table(data=table_data)
report.build([report_title, report_table])
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style= table_style, hAlign="LEFT")
report.build([report_title, report_table])

report_pie = Pie(width=3*inch, height=3*inch)

report_pie.data = []
report_pie.labels = []
for fruits_count in sorted(fruit):
    report_pie.data.append(fruit[fruits_count])
    report_pie.labels.append(fruits_count)

report_chart = Drawing()
report_chart.add(report_pie)
report.build([report_title, report_table, report_chart])