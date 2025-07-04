from .data import *
from .models import *
from apps.base.models import *
def create_chatbot_app(builderobj=None, lg="en"):
    import base64
    import os
    import uuid

    import gradio as gr
    import modelscope_studio.components.antd as antd
    import modelscope_studio.components.antdx as antdx
    import modelscope_studio.components.base as ms
    import modelscope_studio.components.pro as pro
    from modelscope_studio.components.pro.chatbot import (ChatbotActionConfig,
                                                        ChatbotBotConfig,
                                                        ChatbotUserConfig,
                                                        ChatbotWelcomeConfig)
    from modelscope_studio.components.pro.multimodal_input import \
    MultimodalInputUploadConfig
    from openai import OpenAI
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
    # =========== Configuration

    # API KEY
    # MODELSCOPE_ACCESS_TOKEN = os.getenv('MODELSCOPE_ACCESS_TOKEN')

    client = None
    model = "LAHJA-AI"

    save_history = False

    # =========== Configuration

    DEFAULT_PROMPTS = [{
        "label":
        "📅 Make a plan",
        "children": [{
            "description": "Help me with a plan to start a business",
        }, {
            "description": "Help me with a plan to achieve my goals",
        }]
    }, {
        "label":
        "🖋 Help me write",
        "children": [{
            "description": "SHelp me write a story with a twist ending",
        }, {
            "description": "Help me write a blog post on mental health",
        },
           
        ]
    }]
    
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

    DEFAULT_THEME = {
        "token": {
            "colorPrimary": "rgba(11, 186, 131, 1)",
        }
    }

    
    def menu_studio(builder, lg="en"):
          m_category = []
          fist_categary = []
          type_server_pige ="Text-to-Speech"
          
          if builder.Isdiv == False:
              m_category = builder.get_filter(FilterModelAI(Type=ChatSetting.NameMode),ChatSetting.StartModel )
          else:
              m_category = builder.builder.get_property(ChatSetting.StartModel)
          
          if m_category is not None and len(m_category) > 0:
              fist_categary = m_category[0]
          
          current_language = lg
          
          # Black theme CSS
          black_theme_css = """
          :root {#
              --bg-color: #1e1e1e;
              --panel-color: #1e1e1e;
              --text-color: #ffffff;
              --border-color: #333333;
              --hover-color: #2a2a2a;
          }
          .black-theme {
              background-color: var(--bg-color);
              color: var(--text-color);
              border-color: var(--border-color);
          }
          .black-theme .gr-accordion {
              background: var(--panel-color);
              border: 1px solid var(--border-color);
          }
          .black-theme .gr-dropdown, 
          .black-theme .gr-slider,
          .black-theme .gr-checkbox {
              background: var(--panel-color);
              color: var(--text-color);
          }
          .black-theme .gr-slider .gr-handle {
              background: var(--text-color);
          }
          """
          
          with gr.Blocks(css=black_theme_css) as panel:
              with gr.Row():
                  with gr.Column(scale=1, elem_classes="black-theme"):
                      # Options Accordion
                      with gr.Accordion(LANGUAGES[current_language]["options"], open=True):
                          category_dropdown = gr.Dropdown(
                              choices=m_category,
                              label=LANGUAGES[current_language]["category"],
                              value=fist_categary,
                              info=LANGUAGES[current_language]["choose_category"],
                              interactive=True
                          )
                          
                          language_dropdown = gr.Dropdown(
                              choices=[],
                              label=LANGUAGES[current_language]["language"],
                              value=[],
                              visible=False,
                              info=LANGUAGES[current_language]["choose_language"],
                              interactive=True
                          )
                          
                          dialect_dropdown = gr.Dropdown(
                              choices=[],
                              label=LANGUAGES[current_language]["dialect"],
                              value=[],
                              visible=False,
                              info=LANGUAGES[current_language]["choose_dialect"],
                              interactive=True
                          )
                          
                          model_dropdown = gr.Dropdown(
                              label=LANGUAGES[current_language]["model_name"],
                              value=[],
                              visible=False,
                              interactive=True,
                              info=LANGUAGES[current_language]["choose_model"]
                          )
                      
                      # Settings Accordion
                      with gr.Accordion(LANGUAGES[current_language]["settings"], open=False):
                          temperature_slider = gr.Slider(
                              label=LANGUAGES[current_language]["temperature"],
                              minimum=0.1, 
                              maximum=5, 
                              step=0.1, 
                              value=0.7,
                              interactive=True
                          )
                          
                          speech_rate_slider = gr.Slider(
                              label=LANGUAGES[current_language]["max_token"],
                              minimum=50, 
                              maximum=120000, 
                              step=50, 
                              value=1024,
                              interactive=True
                          )
                          
                          streaming_toggle = gr.Checkbox(
                              label=LANGUAGES[current_language]["streaming"],
                              interactive=True,
                              value=True
                          )
                      
                      # Event handlers
                      category_dropdown.change(
                          builder.update_languages, 
                          inputs=[category_dropdown], 
                          outputs=[language_dropdown]
                      )
                      
                      language_dropdown.change(
                          builder.update_dialects, 
                          inputs=[category_dropdown, language_dropdown], 
                          outputs=[dialect_dropdown]
                      )
                      
                      dialect_dropdown.change(
                          builder.update_models, 
                          inputs=[category_dropdown, language_dropdown, dialect_dropdown], 
                          outputs=[model_dropdown]
                      )
          
          

    def user_config(disabled_actions=None):
        return ChatbotUserConfig(actions=[
            "copy", "edit",
            ChatbotActionConfig(
                action="delete",
                popconfirm=dict(title="Delete the message",
                                description="Are you sure to delete this message?",
                                okButtonProps=dict(danger=True)))
        ],
                                disabled_actions=disabled_actions)


    def bot_config(disabled_actions=None):
        return ChatbotBotConfig(
            actions=[
                "copy", "like", "dislike", "edit",
                ChatbotActionConfig(
                    action="retry",
                    popconfirm=dict(
                        title="Regenerate the message",
                        description=
                        "Regenerate the message will also delete all subsequent messages.",
                        okButtonProps=dict(danger=True))),
                ChatbotActionConfig(action="delete",
                                    popconfirm=dict(
                                        title="Delete the message",
                                        description=
                                        "Are you sure to delete this message?",
                                        okButtonProps=dict(danger=True)))
            ],
            avatar="https://mdn.alipayobjects.com/huamei_iwk9zp/afts/img/A*s5sNRo5LjfQAAAAAAAAAAAAADgCCAQ/fmt.webp",
            disabled_actions=disabled_actions)

    from gradio_client import Client
    client = Client("wasmdashai/T2T")
    def ask_ai(message ):
        
        
        result = client.predict(
            text=message,
            key="AIzaSyC85_3TKmiXtOpwybhSFThZdF1nGKlxU5c",
            api_name="/predict"
        )
        return result
    class Gradio_Events:

        @staticmethod
        def submit(state_value):
            # Define your code here
            # The best way is to use the image url.
            def image_to_base64(image_path):
                with open(image_path, "rb") as image_file:
                    encoded_string = base64.b64encode(
                        image_file.read()).decode('utf-8')
                return f"data:image/jpeg;base64,{encoded_string}"

            def format_history(history):
                messages = [{
                    "role": "system",
                    "content": "You are a helpful and harmless assistant.",
                }]
                for item in history:
                    if item["role"] == "user":
                        messages.append({
                            "role":
                            "user",
                            "content": [{
                                "type": "image_url",
                                "image_url": image_to_base64(file)
                            } for file in item["content"][0]["content"]
                                        if os.path.exists(file)] +
                            [{
                                "type": "text",
                                "text": item["content"][1]["content"]
                            }]
                        })
                    elif item["role"] == "assistant":
                        messages.append({
                            "role": "assistant",
                            "content": item["content"]
                        })
                return messages

            history = state_value["conversations_history"][
                state_value["conversation_id"]]
            history_messages = format_history(history)

            history.append({
                "role": "assistant",
                "content": "",
                "loading": True,
                "status": "pending"
            })

            yield {
                chatbot: gr.update(value=history),
                state: gr.update(value=state_value),
            }
            try:
                print(f"history_messages={history_messages}")
                message = history_messages[-1]["content"]
                print(f"mesg:{message}")
                response =builderobj.ask_ai(message[0]['text'])
                for chunk in response:
                    history[-1]["content"] += chunk
                    history[-1]["loading"] = False
                    yield {
                        chatbot: gr.update(value=history),
                        state: gr.update(value=state_value)
                    }
                history[-1]["status"] = "done"
                yield {
                    chatbot: gr.update(value=history),
                    state: gr.update(value=state_value),
                }
            except Exception as e:
                history[-1]["loading"] = False
                history[-1]["status"] = "done"
                history[-1]["content"] = "Failed to respond, please try again."
                yield {
                    chatbot: gr.update(value=history),
                    state: gr.update(value=state_value)
                }
                raise e

        @staticmethod
        def add_user_message(input_value, state_value):
            if not state_value["conversation_id"]:
                random_id = str(uuid.uuid4())
                history = []
                state_value["conversation_id"] = random_id
                state_value["conversations_history"][random_id] = history
                state_value["conversations"].append({
                    "label": input_value["text"],
                    "key": random_id
                })

            history = state_value["conversations_history"][
                state_value["conversation_id"]]
            history.append({
                "role":
                "user",
                "content": [{
                    "type": "file",
                    "content": [f for f in input_value["files"]]
                }, {
                    "type": "text",
                    "content": input_value["text"]
                }]
            })
            return gr.update(value=state_value)

        @staticmethod
        def preprocess_submit(clear_input=True):

            def preprocess_submit_handler(state_value):
                history = state_value["conversations_history"][
                    state_value["conversation_id"]]
                return {
                    **({
                        input:
                        gr.update(value=None, loading=True) if clear_input else gr.update(loading=True),
                    } if clear_input else {}),
                    conversations:
                    gr.update(active_key=state_value["conversation_id"],
                                items=list(
                                    map(
                                        lambda item: {
                                            **item,
                                            "disabled":
                                            True if item["key"] != state_value[
                                                "conversation_id"] else False,
                                        }, state_value["conversations"]))),
                    add_conversation_btn:
                    gr.update(disabled=True),
                    clear_btn:
                    gr.update(disabled=True),
                    conversation_delete_menu_item:
                    gr.update(disabled=True),
                    chatbot:
                    gr.update(value=history,
                                bot_config=bot_config(
                                    disabled_actions=['edit', 'retry', 'delete']),
                                user_config=user_config(
                                    disabled_actions=['edit', 'delete'])),
                    state:
                    gr.update(value=state_value),
                }

            return preprocess_submit_handler

        @staticmethod
        def postprocess_submit(state_value):
            history = state_value["conversations_history"][
                state_value["conversation_id"]]
            return {
                input:
                gr.update(loading=False),
                conversation_delete_menu_item:
                gr.update(disabled=False),
                clear_btn:
                gr.update(disabled=False),
                conversations:
                gr.update(items=state_value["conversations"]),
                add_conversation_btn:
                gr.update(disabled=False),
                chatbot:
                gr.update(value=history,
                            bot_config=bot_config(),
                            user_config=user_config()),
                state:
                gr.update(value=state_value),
            }

        @staticmethod
        def cancel(state_value):
            history = state_value["conversations_history"][
                state_value["conversation_id"]]
            history[-1]["loading"] = False
            history[-1]["status"] = "done"
            history[-1]["footer"] = "Chat completion paused"
            return Gradio_Events.postprocess_submit(state_value)

        @staticmethod
        def delete_message(state_value, e: gr.EventData):
            index = e._data["payload"][0]["index"]
            history = state_value["conversations_history"][
                state_value["conversation_id"]]
            history = history[:index] + history[index + 1:]

            state_value["conversations_history"][
                state_value["conversation_id"]] = history

            return gr.update(value=state_value)

        @staticmethod
        def edit_message(state_value, chatbot_value, e: gr.EventData):
            index = e._data["payload"][0]["index"]
            history = state_value["conversations_history"][
                state_value["conversation_id"]]
            history[index]["content"] = chatbot_value[index]["content"]
            return gr.update(value=state_value)

        @staticmethod
        def regenerate_message(state_value, e: gr.EventData):
            index = e._data["payload"][0]["index"]
            history = state_value["conversations_history"][
                state_value["conversation_id"]]
            history = history[:index]
            state_value["conversations_history"][
                state_value["conversation_id"]] = history
            # custom code
            return gr.update(value=history), gr.update(value=state_value)

        @staticmethod
        def select_suggestion(input_value, e: gr.EventData):
            input_value["text"] = input_value["text"][:-1] + e._data["payload"][0]
            return gr.update(value=input_value)

        @staticmethod
        def apply_prompt(input_value, e: gr.EventData):
            input_value["text"] = e._data["payload"][0]["value"]["description"]
            return gr.update(value=input_value)

        @staticmethod
        def new_chat(state_value):
            if not state_value["conversation_id"]:
                return gr.skip()
            state_value["conversation_id"] = ""
            return gr.update(active_key=state_value["conversation_id"]), gr.update(
                value=None), gr.update(value=state_value)

        @staticmethod
        def select_conversation(state_value, e: gr.EventData):
            active_key = e._data["payload"][0]
            if state_value["conversation_id"] == active_key or (
                    active_key not in state_value["conversations_history"]):
                return gr.skip()
            state_value["conversation_id"] = active_key
            return gr.update(active_key=active_key), gr.update(
                value=state_value["conversations_history"][active_key]), gr.update(
                    value=state_value)

        @staticmethod
        def click_conversation_menu(state_value, e: gr.EventData):
            conversation_id = e._data["payload"][0]["key"]
            operation = e._data["payload"][1]["key"]
            if operation == "delete":
                del state_value["conversations_history"][conversation_id]

                state_value["conversations"] = [
                    item for item in state_value["conversations"]
                    if item["key"] != conversation_id
                ]

                if state_value["conversation_id"] == conversation_id:
                    state_value["conversation_id"] = ""
                    return gr.update(
                        items=state_value["conversations"],
                        active_key=state_value["conversation_id"]), gr.update(
                            value=None), gr.update(value=state_value)
                else:
                    return gr.update(
                        items=state_value["conversations"]), gr.skip(), gr.update(
                            value=state_value)
            return gr.skip()

        @staticmethod
        def clear_conversation_history(state_value):
            if not state_value["conversation_id"]:
                return gr.skip()
            state_value["conversations_history"][
                state_value["conversation_id"]] = []
            return gr.update(value=None), gr.update(value=state_value)

        @staticmethod
        def update_browser_state(state_value):

            return gr.update(value=dict(
                conversations=state_value["conversations"],
                conversations_history=state_value["conversations_history"]))

        @staticmethod
        def apply_browser_state(browser_state_value, state_value):
            state_value["conversations"] = browser_state_value["conversations"]
            state_value["conversations_history"] = browser_state_value[
                "conversations_history"]
            return gr.update(
                items=browser_state_value["conversations"]), gr.update(
                    value=state_value)


    css = """
    #chatbot {
      height: calc(100vh - 32px - 21px - 16px);
    }

    #chatbot .chatbot-conversations {
      height: 100%;
      background-color: var(--ms-gr-ant-color-bg-layout);
    }

    #chatbot .chatbot-conversations .chatbot-conversations-list {
      padding-left: 0;
      padding-right: 0;
    }

    #chatbot .chatbot-chat {
      padding: 32px;
      height: 100%;
    }

    @media (max-width: 768px) {
      #chatbot .chatbot-chat {
          padding: 0;
      }
    }
                    
          
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
    #chatbot .chatbot-chat .chatbot-chat-messages {
      flex: 1;
    }
    """


    def logo():
        with antd.Typography.Title(level=1,
                                elem_style=dict(fontSize=24,
                                                padding=8,
                                                margin=0)):
            with antd.Flex(align="center", gap="small", justify="center"):
                antd.Image(
                    "https://mdn.alipayobjects.com/huamei_iwk9zp/afts/img/A*eco6RrQhxbMAAAAAAAAAAAAADgCCAQ/original",
                    preview=False,
                    alt="logo",
                    width=24,
                    height=24)
                ms.Span("Chatbot")




    with gr.Blocks(css=css, fill_width=True) as demo:
        state = gr.State({
            "conversations_history": {},
            "conversations": [],
            "conversation_id": "",
        })

        with ms.Application(), antdx.XProvider(
                theme=DEFAULT_THEME, locale=DEFAULT_LOCALE), ms.AutoLoading():
           
        
         
            with antd.Row(gutter=[20, 20], wrap=False, elem_id="chatbot"):
                # Left Column
                with antd.Col(md=dict(flex="0 0 260px", span=24, order=0),
                            span=0,
                            order=1,
                            elem_classes="chatbot-conversations"):
                    with antd.Flex(vertical=True,
                                gap="small",
                                elem_style=dict(height="100%")):
                        # Logo
                        logo()

                        # New Conversation Button
                        with antd.Button(value=None,
                                            color="primary",
                                            variant="filled",
                                            block=True) as add_conversation_btn:
                            ms.Text("New Conversation")
                            with ms.Slot("icon"):
                                antd.Icon("PlusOutlined")

                        # Conversations List
                        with antdx.Conversations(
                                elem_classes="chatbot-conversations-list",
                        ) as conversations:
                            with ms.Slot('menu.items'):
                                with antd.Menu.Item(
                                        label="Delete", key="delete", danger=True
                                ) as conversation_delete_menu_item:
                                    with ms.Slot("icon"):
                                        antd.Icon("DeleteOutlined")
                        antd.Divider("Menu")
                        menu_studio(builderobj)               
                        antd.Divider("Settings")

                                    # Settings Area
                        with antd.Space(size="small",
                                                    wrap=True,
                                                    elem_id="settings-area"):
                                        system_prompt_btn = antd.Button(
                                            "⚙️ Set System Prompt", type="default")
                                        history_btn = antd.Dropdown.Button(
                                            "📜 History",
                                            type="default",
                                            elem_id="history-btn",
                                            menu=dict(items=[{
                                                "key": "clear",
                                                "label": "Clear History",
                                                "danger": True
                                            }]))
                # Right Column

                with antd.Col(flex=1, elem_style=dict(height="100%")):
                    with antd.Flex(vertical=True, elem_classes="chatbot-chat"):
                        gr.HTML(bodyicon)
                      
                        chatbot = pro.Chatbot(
                            elem_classes="chatbot-chat-messages",
                            welcome_config=ChatbotWelcomeConfig(
                                variant="borderless",
                                icon=
                                "https://mdn.alipayobjects.com/huamei_iwk9zp/afts/img/A*s5sNRo5LjfQAAAAAAAAAAAAADgCCAQ/fmt.webp",
                                title=f"Hello, I'm {model}",
                                description=
                                "You can upload images and text to get started.",
                                prompts=dict(
                                    title="How can I help you today?",
                                    styles={
                                        "list": {
                                            "width": '100%',
                                        },
                                        "item": {
                                            "flex": 1,
                                        },
                                    },
                                    items=[{
                                        "label":
                                        "🖋 Make a plan",
                                        "children": [{
                                            "description":
                                            "Help me with a plan to start a business"
                                        },]
                                    }, {
                                        "label":
                                        "📅 Help me write",
                                        "children": [{
                                            "description":
                                            "Help me write a story with a twist ending"
                                        }]
                                    }]),
                            ),
                            user_config=user_config(),
                            bot_config=bot_config())
                        # Input
                        with antdx.Suggestion(
                                items=DEFAULT_SUGGESTIONS,
                                # onKeyDown Handler in Javascript
                                should_trigger="""(e, { onTrigger, onKeyDown }) => {
                          switch(e.key) {
                            case '/':
                              onTrigger()
                              break
                            case 'ArrowRight':
                            case 'ArrowLeft':
                            case 'ArrowUp':
                            case 'ArrowDown':
                              break;
                            default:
                              onTrigger(false)
                          }
                          onKeyDown(e)
                        }""") as suggestion:
                            with ms.Slot("children"):
                                with pro.MultimodalInput(
                                        placeholder="Enter / to get suggestions",
                                        upload_config=MultimodalInputUploadConfig(
                                            upload_button_tooltip=
                                            "Upload Attachments",
                                            allow_speech=True, allow_paste_file=True,
                                            max_count=6,
                                            
                                            accept="image/*",
                                            multiple=True)) as input:
                                    with ms.Slot("prefix"):
                                        # Clear Button
                                        with antd.Tooltip(
                                                title="Clear Conversation History"
                                        ):
                                            with antd.Button(
                                                    value=None,
                                                    type="text") as clear_btn:
                                                with ms.Slot("icon"):
                                                    antd.Icon("ClearOutlined")

        # Events Handler
        if save_history:
            browser_state = gr.BrowserState(
                {
                    "conversations_history": {},
                    "conversations": [],
                },
                storage_key="ms_chatbot_storage")
            state.change(fn=Gradio_Events.update_browser_state,
                        inputs=[state],
                        outputs=[browser_state])

            demo.load(fn=Gradio_Events.apply_browser_state,
                    inputs=[browser_state, state],
                    outputs=[conversations, state])

        add_conversation_btn.click(fn=Gradio_Events.new_chat,
                                inputs=[state],
                                outputs=[conversations, chatbot, state])
        conversations.active_change(fn=Gradio_Events.select_conversation,
                                    inputs=[state],
                                    outputs=[conversations, chatbot, state])
        conversations.menu_click(fn=Gradio_Events.click_conversation_menu,
                                inputs=[state],
                                outputs=[conversations, chatbot, state])
        chatbot.welcome_prompt_select(fn=Gradio_Events.apply_prompt,
                                    inputs=[input],
                                    outputs=[input])

        clear_btn.click(fn=Gradio_Events.clear_conversation_history,
                        inputs=[state],
                        outputs=[chatbot, state])

        suggestion.select(fn=Gradio_Events.select_suggestion,
                        inputs=[input],
                        outputs=[input])
        chatbot.delete(fn=Gradio_Events.delete_message,
                    inputs=[state],
                    outputs=[state])
        chatbot.edit(fn=Gradio_Events.edit_message,
                    inputs=[state, chatbot],
                    outputs=[state])

        regenerating_event = chatbot.retry(
            fn=Gradio_Events.regenerate_message,
            inputs=[state],
            outputs=[chatbot, state
                    ]).then(fn=Gradio_Events.preprocess_submit(clear_input=False),
                            inputs=[state],
                            outputs=[
                                input, clear_btn, conversation_delete_menu_item,
                                add_conversation_btn, conversations, chatbot,
                                state
                            ]).then(fn=Gradio_Events.submit,
                                    inputs=[state],
                                    outputs=[chatbot, state])

        submit_event = input.submit(
            fn=Gradio_Events.add_user_message,
            inputs=[input, state],
            outputs=[state
                    ]).then(fn=Gradio_Events.preprocess_submit(clear_input=True),
                            inputs=[state],
                            outputs=[
                                input, clear_btn, conversation_delete_menu_item,
                                add_conversation_btn, conversations, chatbot,
                                state
                            ]).then(fn=Gradio_Events.submit,
                                    inputs=[state],
                                    outputs=[chatbot, state])
        regenerating_event.then(fn=Gradio_Events.postprocess_submit,
                                inputs=[state],
                                outputs=[
                                    input, conversation_delete_menu_item,
                                    clear_btn, conversations, add_conversation_btn,
                                    chatbot, state
                                ])
        submit_event.then(fn=Gradio_Events.postprocess_submit,
                        inputs=[state],
                        outputs=[
                            input, conversation_delete_menu_item, clear_btn,
                            conversations, add_conversation_btn, chatbot, state
                        ])
        input.cancel(fn=Gradio_Events.cancel,
                    inputs=[state],
                    outputs=[
                        input, conversation_delete_menu_item, clear_btn,
                        conversations, add_conversation_btn, chatbot, state
                    ],
                    cancels=[submit_event, regenerating_event],
                    queue=False)
    
    return demo

 
 