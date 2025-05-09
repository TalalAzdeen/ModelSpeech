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
import plotly.express as px
import time
from .models import *
from typing import Optional

def createTextToText(builder, lg="en"):
    try:
        print(f"Creating TextToText")
        #m_category=builder.get_filter(FilterModelAI(type="Chat"),"category")

        m_category=[]
        fist_categary=[]
        type_server_pige="Chat"
        if builder.Isdiv==False:
            m_category=builder.get_filter(FilterModelAI(Type=type_server_pige),"category")
        else:

            m_category = builder.builder.get_property("category")
            
        if m_category !=None:
           fist_categary=m_category[0]
         
        #m_category=None
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
def create_t2text(builder,current_language="en"):
    try:
        type_server_pige="Chat"
        #listmodel =builder.builder.get_property("absolutePath")
        listmodel=builder.get_filter(FilterModelAI(Type=type_server_pige),"absolutePath")
        if listmodel is None:
            frist=None
            listmodel = []
            print(listmodel)

        else:
            frist=listmodel[0]
        with gr.Row():
            with gr.Column():
                model_name = gr.Dropdown(
                    choices=listmodel,
                    label=LANGUAGESTEXT[current_language]["model_name"],
                    value=frist,
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

