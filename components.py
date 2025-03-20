from .data import *
import plotly.express as px

def change_filter(service_type,data,name_type="Type"):
            if service_type == "ALL":
                return data
            else:
                return data[data[name_type] == service_type]
def createPlotCard(data,labels,type_chart="bar"):
   return gr.BarPlot(data, x=labels["x"], y=labels["y"], color=labels["Type"])  if type_chart=="bar" else gr.LinePlot(data, x=labels["x"], y=labels["y"], color=labels["Type"])


def  BarServiceCard(data,labels=None,titel="Bar Service",type_chart="bar"):


        if labels is None:
            labels = {
                "label_dropdown":"Type",
                "Type": "Type",
                "x": "x",
                "y": "y"
            }


        with gr.Accordion(titel) as panel:
                  dropdownchart=gr.Radio(["bar","line"], value=type_chart, label="Chart Type")
                  dropdown=gr.Dropdown(choices=["ALL"]+list(data[labels["Type"]].unique()), label=labels["label_dropdown"])
                  dashplot=createPlotCard(data,labels,type_chart)
                  dropdown.change(fn=lambda service_type: change_filter(service_type,data,labels["Type"]), inputs=dropdown, outputs=dashplot)
                  dropdownchart.change(fn=lambda type_chart: createPlotCard(data,labels,type_chart), inputs=dropdownchart, outputs=dashplot)
        return panel,dashplot,dropdown



def  create_section_state(builder,labels):
            with gr.Accordion(labels["PlanRequestsVisualization"]) as plan:

                        with gr.Row():
                            with  gr.Column(scale=1):
                                with gr.Column():
                                      plotservice=gr.Plot(builder.get_data_byservices)

                            with gr.Column(scale=1):
                                with gr.Column():
                                      plotpiereq=gr.Plot(builder.get_data_byplan)
                            with gr.Column(scale=1):
                                  gr.Plot(builder.get_data_byplan)
            return   plan


def plotpie(values,labels,title="Plan Requests Distribution",
            hole=0.4,
            color_discrete_sequence=["rgba(11, 186, 131, 1)", "#99CCFF"],
            height=300):



    # إنشاء المخطط باستخدام plotly
    fig = px.pie(
        names=labels,
        values=values,
        title=title,
        hole=hole,  # مخطط دائري مجوف
        color_discrete_sequence=color_discrete_sequence,
        height=height,
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # خلفية الورقة
        plot_bgcolor='rgba(0,0,0,0)',  # خلفية الرسم
        font_color='black'  # النص الأسود للوضع العادي (يتغير حسب الوضع الليلي)
    )
    return fig


def   creatBarplotgroup(builder,labels):
        with gr.Row():
                  # مخططات للطلبات
                  requests_by_time = gr.LinePlot(
                      builder.get_staterequests(),
                      x="time",
                      y="requests",
                      title=labels["requests_by_time_title"]
                  )

                  # مخططات للأخطاء
                  errors_by_time = gr.LinePlot(
                      builder.get_stateerrors(),
                      x="time",
                      y="errors",
                      title=labels["errors_by_time_title"]
                  )
        return requests_by_time,errors_by_time


def   create_section_bytime(builder,labels):
             with gr.Accordion(labels["apply_btn"]) as panel:
                tokenauth=gr.State(builder.token)
                with gr.Row():
                        start = gr.DateTime("2025-01-01 00:00:00", label=labels["start_date"])
                        end = gr.DateTime("2025-01-05 00:00:00", label=labels["end_date"])
                        apply_btn = gr.Button(labels["apply_btn"], scale=0)


                with gr.Row():
                    group_by = gr.Radio([labels["none"], labels["30m"], labels["1h"], labels["4h"], labels["1d"]], value=labels["none"], label=labels["group_by"])
                    aggregate = gr.Radio(["sum", "mean", "median", "min", "max"], value="sum", label=labels["aggregation"])



                requests_by_time,errors_by_time=creatBarplotgroup(builder,labels)


                labels_service = {
                "label_dropdown":"Type Service",
                "Type": "service_type",
                "x": "time",
                "y": "requests"
                }
                panel,dashplot,dropdowntypeservce=BarServiceCard(builder.get_staterequests(),labels_service,labels["requests_by_time_title"])
                time_graphs = [requests_by_time, errors_by_time]
                def  change_group_by(token,group):
                        return [gr.LinePlot(x_bin=None if group == labels["none"] else group)] * len(time_graphs)
                group_by.change(fn=change_group_by,inputs=[tokenauth,group_by],outputs=time_graphs)
                # group_by.change(
                #           lambda group: [gr.LinePlot(x_bin=None if group == labels["none"] else group)] * len(time_graphs),
                #           group_by,
                #           time_graphs
                #       )
                def  change_aggregate_by(token,y_aggregate):

                        return [gr.LinePlot(y_aggregate=aggregate)] * len(time_graphs)
                aggregate.change(fn=change_aggregate_by,inputs=[tokenauth,aggregate],outputs=time_graphs)
                # aggregate.change(
                #           lambda aggregate: [gr.LinePlot(y_aggregate=aggregate)] * len(time_graphs),
                #           aggregate,
                #           time_graphs
                #       )

                    # خدمة rescale
                def rescale(select: gr.SelectData):
                        return select.index
                rescale_evt = gr.on([plot.select for plot in time_graphs], rescale, None, [start, end])
                def  filter(token,start,end):
                        data=builder.ge_by_filter(start,end)
                        return  [ gr.LinePlot(
                          data,
                          x="time",
                          y="errors",
                          title=labels["errors_by_time_title"]
                      ) ,gr.LinePlot(
                          data,
                          x="time",
                          y="requests",
                          title=labels["requests_by_time_title"]
                      )]




                apply_btn.click(filter,inputs=[tokenauth,start,end],outputs=time_graphs)
                for trigger in [apply_btn.click, rescale_evt.then]:
                        trigger(
                            lambda start, end: [gr.LinePlot(x_lim=[start, end])] * len(time_graphs), [start, end], time_graphs
                        )


def  create_section_by_all_services(builder,labels):
        with gr.Accordion(labels["requests_by_service"]) as panel2:

                  data,labels_servs=builder.get_data_byplan_services()
                  panel5=BarServiceCard(data,labels_servs,type_chart="bar")
Style = """
    <style>
      :root {
    --name: default;

    --primary-500: rgba(11, 186, 131, 1);
    }
    """
