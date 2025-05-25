from .data import *

bodyicon = """
    <style>
      :root {
    --name: default;

    --primary-500: rgba(11, 186, 131, 1);
    }
      .shadow-primary {
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.25);
      }
      .icon-xxl {
        width: 170px;
        height: 170px;
        line-height: 6.8rem;
        align-items: center;
      }
      .icon-md, .icon-lg, .icon-xl, .icon-xxl {
        display: flex;
        justify-content: center;
        align-items: center;
        border-radius: 50%;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        background-color: #ffffff;
      }
      .flex-shrink-0 {
        flex-shrink: 0 !important;
      }
      .rounded-circle {
        border-radius: 50% !important;
      }
      .text-center {
        text-align: center;
      }
      .mud-icon-root.mud-svg-icon {
        fill: rgba(11,186,131,1);
      }
      .mud-icon-size-large {
        font-size: 4.25rem !important;
        width: 7.25rem !important;
        height: 7.25rem !important;
      }
      .mud-success-text {
        color: rgba(11,186,131,1);
      }
      .icon-cont-center {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;

      }
      .built-with.svelte-sar7eh.svelte-sar7eh.svelte-sar7eh {
        display:none !important;
      }
     footer.svelte-sar7eh.svelte-sar7eh.svelte-sar7eh {
    position: fixed;
    right: 20px;
    top: 0;
}
       .gap.svelte-vt1mxs {
    gap: 8px !important;
}
    </style>
    <div class="icon-cont-center  ">
    <div id="logo-icon-static-id" class="icon-xxl text-center shadow-primary rounded-circle flex-shrink-0">
        <svg class="mud-icon-root mud-svg-icon mud-success-text mud-icon-size-large" style="direction:ltr !important;margin:8px !important" focusable="false" viewBox="0 0 24 24" aria-hidden="true" role="img">
            <title>API</title>
            <path d="M0 0h24v24H0z" fill="none"></path>
            <path d="M6 13c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0 4c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0-8c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm-3 .5c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zM6 5c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm15 5.5c.28 0 .5-.22.5-.5s-.22-.5-.5-.5-.5.22-.5.5.22.5.5.5zM14 7c.55 0 1-.45 1-1s-.45-1-1-1-1 .45-1 1 .45 1 1 1zm0-3.5c.28 0 .5-.22.5-.5s-.22-.5-.5-.5-.5.22-.5.5.22.5.5.5zm-11 10c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zm7 7c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zm0-17c.28 0 .5-.22.5-.5s-.22-.5-.5-.5-.5.22-.5.5.22.5.5.5zM10 7c.55 0 1-.45 1-1s-.45-1-1-1-1 .45-1 1 .45 1 1 1zm0 5.5c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zm8 .5c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0 4c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0-8c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0-4c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm3 8.5c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zM14 17c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm0 3.5c-.28 0-.5.22-.5.5s.22.5.5.5.5-.22.5-.5-.22-.5-.5-.5zm-4-12c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zm0 8.5c-.55 0-1 .45-1 1s.45 1 1 1 1-.45 1-1-.45-1-1-1zm4-4.5c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5zm0-4c-.83 0-1.5.67-1.5 1.5s.67 1.5 1.5 1.5 1.5-.67 1.5-1.5-.67-1.5-1.5-1.5z"></path>
        </svg>
    </div>
    </div>
"""
users = [("admin", "password123"), ("user", "userpass")]
 
 

import gradio as gr
from gradio_client import Client
import pandas as pd
from random import randint
import modelscope_studio.components.antd as antd
import modelscope_studio.components.antdx as antdx
import modelscope_studio.components.base as ms
import modelscope_studio.components.pro as pro
import plotly.express as px
import time
from .models import *
from typing import Optional
def get_categories(builder, type_name,type_name_dev):
    """Helper function to get category list and first category"""
    if not builder:
        return [], None

    if builder.Isdiv is False:

        categories = builder.get_filter(FilterModelAI(Type=type_name), "category")
        if categories==None:
           return [],None 
    else:
        
        categories = builder.builder.get_property(type_name_dev)

    first = categories[0] if categories else None
    return categories, first

def createTextToText(builder, lg="en"):
    try:
        print(f"Creating TextToTextStudio")
        #m_category=builder.get_filter(FilterModelAI(type="Chat"),"category")

        # m_category=[]
        # fist_categary=[]
        # type_server_pige="Chat"
        # if builder.Isdiv==False:
        #     m_category=builder.get_filter(FilterModelAI(Type=type_server_pige),"category")
            
        # else:

        #     m_category = builder.builder.get_property("category")
        #     print(f"m_category:{m_category}")
            
        # if m_category !=None:
        #    fist_categary=m_category[0]
         
        #m_category=None
        m_category,fist_categary=get_categories(builder,type_name=TextStudioSetting.NameMode,type_name_dev=TextStudioSetting.StartModel)
        #m_category,fist_categary=get_categories(builder,type_name="Text-to-Speech",type_name_dev="category")
        # type_server_pige="Chat"
        current_language = lg

        with gr.Blocks() as panel:
            with gr.Row():
                with gr.Column(scale=1):
                    with gr.Accordion(LANGUAGES[current_language]["options"]):
                        category_dropdown = gr.Dropdown(
                            choices=m_category,
                            label=LANGUAGES[current_language]["category"],
                            value=fist_categary,
                            info=LANGUAGES[current_language]["choose_category"]

                        )
                        language_dropdown = gr.Dropdown(
                            choices=[],
                            label=LANGUAGES[current_language]["language"],
                            value=[],
                            visible=False,
                            info=LANGUAGES[current_language]["choose_language"]
                        )
                        dialect_dropdown = gr.Dropdown(
                            choices=[],
                            label=LANGUAGES[current_language]["dialect"],
                            value=[],
                            visible=False,
                            info=LANGUAGES[current_language]["choose_dialect"]
                        )
                        model_dropdown = gr.Dropdown(

                            label=LANGUAGES[current_language]["model_name"],
                            value=[],
                            visible=False,
                            interactive=True,
                            info=LANGUAGES[current_language]["choose_model"]
                        )

                    with gr.Accordion(LANGUAGES[current_language]["settings"]):
                        temperature_slider = gr.Slider(
                            label=LANGUAGES[current_language]["temperature"],
                            minimum=0.1, maximum=5, step=0.1, value=0.7
                        )
                        speech_rate_slider = gr.Slider(
                            label=LANGUAGES[current_language]["max_token"],
                            minimum=50, maximum=120000, step=50, value=1024
                        )
                        streaming_toggle = gr.Checkbox(
                            label=LANGUAGES[current_language]["streaming"],
                            value=True
                        )

                with gr.Column(scale=3):
                    bd = gr.HTML(bodyicon)  # عرض الأيقونة
                    out_textbox = gr.Textbox(
                        label=LANGUAGES[current_language]["voice_output"],
                        lines=6,
                        max_lines=6
                    )

                    chat_input = gr.MultimodalTextbox(
                        interactive=True,
                        file_count="single",
                        placeholder=LANGUAGES[current_language]["enter_message"],
                        show_label=False,
                        lines=3,
                        max_lines=3
                    )

                    category_dropdown.change(
                        builder.update_languages, inputs=[category_dropdown], outputs=[language_dropdown]
                    )

                    language_dropdown.change(
                        builder.update_dialects, inputs=[category_dropdown,language_dropdown], outputs=[dialect_dropdown]
                    )
                    dialect_dropdown.change(
                        builder.update_models, inputs=[category_dropdown,language_dropdown,dialect_dropdown], outputs=[model_dropdown]
                    )

                    chat_input.submit(
                    builder.bot,
                    inputs=[
                        chat_input,
                     
                        model_dropdown,
                       
                        speech_rate_slider,
                        temperature_slider,
                        streaming_toggle,
                    ],
                    outputs=[chat_input, out_textbox, bd]
                    )
        return panel

    except Exception as e:
        print(f"An error occurred: {e}")
DEFAULT_THEME = {
    "token": {
        "colorPrimary": "rgba(11, 186, 131, 1)",
    }

}
DEFAULT_SUGGESTIONS = [{
    "label":
    'Make a plan',
    "value":
    "Make a plan",
    "children": [{
        "label": "Start a business",
        "value": "Help me with a plan to start a business"
    }, {
        "label": "Achieve my goals",
        "value": "Help me with a plan to achieve my goals"
    }, {
        "label": "Successful interview",
        "value": "Help me with a plan for a successful interview"
    }]
}, {
    "label":
    'Help me write',
    "value":
    "Help me write",
    "children": [{
        "label": "Story with a twist ending",
        "value": "Help me write a story with a twist ending"
    }, {
        "label": "Blog post on mental health",
        "value": "Help me write a blog post on mental health"
    }, {
        "label": "Letter to my future self",
        "value": "Help me write a letter to my future self"
    }]
}]

DEFAULT_LOCALE = 'en_US'

# def create_t2text(builder, current_language="en"):
#     try:
#         m_category, first_category = get_categories(
#             builder, type_name="Text-to-Speech", type_name_dev="AbsolutePath"
#         )

#         with ms.Application(), antdx.XProvider(theme=DEFAULT_THEME, locale=DEFAULT_LOCALE), ms.AutoLoading():
#             with antd.Row(gutter=[20, 20], wrap=False, elem_id="t2text"):
#                 # Left Column (Inputs)
#                 with antd.Col(md=dict(flex="0 0 340px", span=24, order=0),
#                               span=0, order=1, elem_classes="t2text-controls"):
#                     with antd.Flex(vertical=True, gap="small", elem_style=dict(height="100%")):
#                         antd.Typography.Title("🎙 Text-to-Speech", level=4)

#                         # Model dropdown
#                         model_name = antd.Select(
#                             options=[{"label": m, "value": m} for m in m_category],
#                             default_value=first_category,
#                             elem_style={"width": "100%"},
#                             allow_clear=False
#                         )

#                         # Text input box
#                         text_input = pro.MultimodalInput(
#                             placeholder=LANGUAGESTEXT[current_language]["enter_message"],
#                             upload_config=MultimodalInputUploadConfig(
#                                 upload_button_tooltip="Upload",
#                                 allow_speech=True,
#                                 allow_paste_file=True,
#                                 max_count=3,
#                                 multiple=False
#                             )
#                         )

#                         # Temperature (rate) slider
#                         rate_slider = antd.Slider(
#                             min=0.1, max=1.0, step=0.1,
#                             default_value=0.8,
#                             tooltip={"open": True},
#                             label=LANGUAGESTEXT[current_language]["temperature"]
#                         )

#                         # Max token (duration) slider
#                         duration_slider = antd.Slider(
#                             min=0.1, max=5.0, step=0.1,
#                             default_value=1.0,
#                             tooltip={"open": True},
#                             label=LANGUAGESTEXT[current_language]["max_token"]
#                         )

#                         # Streaming toggle
#                         streaming_toggle = antd.Switch(
#                             default_checked=True,
#                             label=LANGUAGESTEXT[current_language]["streaming"]
#                         )

#                         # Submit Button
#                         submit_button = antd.Button(
#                             "🔊 Convert",
#                             type="primary",
#                             block=True
#                         )

#                 # Right Column (Output)
#                 with antd.Col(flex=1, elem_style=dict(height="100%")):
#                     with antd.Flex(vertical=True, gap="middle"):
#                         html = gr.HTML(bodyicon)

#                         output_text = antd.Textarea(
#                             disabled=True,
#                             auto_size=True,
#                             placeholder=LANGUAGESTEXT[current_language]["output"]
#                         )

#             # Event binding
#             submit_button.click(
#                 fn=builder.bot,
#                 inputs=[
#                     text_input,
#                     model_name,
#                     rate_slider,
#                     duration_slider,
#                     streaming_toggle
#                 ],
#                 outputs=[text_input, output_text, html]
#             )

#     except Exception as e:
#         print(f"Error in create_t2text: {str(e)}")
#         return None

def create_t2text(builder,current_language="en"):
    try:

    


        
        m_category,fist_categary=get_categories(builder,type_name=TextbuilderSetting.NameMode,type_name_dev=TextbuilderSetting.StartModel)
     
        with gr.Row():
            with gr.Column():
                model_name = gr.Dropdown(
                    choices=m_category,
                    label=LANGUAGESTEXT[current_language]["model_name"],
                    value=fist_categary,
                    interactive=True
                    
                )
                # text_input = gr.Textbox(
                #     label=LANGUAGESPEECH[current_language]["enter_message"],
                #     placeholder=LANGUAGESPEECH[current_language]["enter_message"]
                # )

                text_input = gr.MultimodalTextbox(
                          interactive=True,
                           visible=True,
                          placeholder=LANGUAGESTEXT[current_language]["enter_message"],
                          show_label=False,
                          lines=3,
                          max_lines=6
                      )
                rate_slider = gr.Slider(
                    0.1, 1, step=0.1, value=0.8, label=LANGUAGESTEXT[current_language]["temperature"]
                )
                duration_slider = gr.Slider(
                    0.1, 5, step=0.1, value=1.0, label=LANGUAGESTEXT[current_language]["max_token"]
                )
                streaming_toggle = gr.Checkbox(
                            label=LANGUAGESTEXT[current_language]["streaming"],
                            value=True
                        )
                #submit_button = gr.Button(LANGUAGESPEECH[current_language]["convert"])

            with gr.Column():
                html = gr.HTML(bodyicon)
                output_text = gr.Textbox(label=LANGUAGESTEXT[current_language]["output"])

            text_input.submit(
                    builder.bot,
                    inputs=[
                        text_input,
                     
                        model_name,
                       
                        rate_slider,
                        duration_slider,
                        streaming_toggle,
                    ],
                    outputs=[text_input, output_text,html]
                    )
              
    except Exception as e:
        print(f"Error in create_t2text: {str(e)}")
        #print(f"Error message: {str(Builder.builder.)}"
        # هنا يمكن إضافة معالجة خطأ إضافية أو إرسال رسالة خطأ خاصة
        return None  # إعادة None في حال حدوث استثناء

