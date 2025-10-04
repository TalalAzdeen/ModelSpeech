from fastapi import FastAPI
import gradio as gr
from fastapi.responses import RedirectResponse

from gradio_ui import demo
import t2speech
import t2text
import chatbot
import dashboard
import t2speechmuit
import userspace
import menupage
from  encrypt import company_handler
import dach
import roadGuard

import audio_interface
app = FastAPI()

@app.get('/')
async def root():
    return 'Gradio app is running at /gradio', 200
@app.get("/redirect")
async def redirect_to_site():
    # إعادة التوجيه إلى موقع معين
    return RedirectResponse(url="http://lahja.runasp.net/services")



company_handler = CompanyHandler() 
app.include_router(company_handler.get_router(), prefix="/company", tags=["Company"])
app = gr.mount_gradio_app(app, menupage.demo, path='/menupage')
app = gr.mount_gradio_app(app, dach.demo, path='/dach')
app = gr.mount_gradio_app(app, roadGuard.demo, path='/roadGuard')
#app = gr.mount_gradio_app(app, t2speech.demo, path='/t2speech')
#app = gr.mount_gradio_app(app, testc.demo, path='/testc')
# app = gr.mount_gradio_app(app, t2text.demo, path='/studio-t2text')

#app = gr.mount_gradio_app(app, dash.demo, path='/dash')

# app = gr.mount_gradio_app(app, chatbot.demo, path='/chatbot')
#app = gr.mount_gradio_app(app, dashboard.dashboard, path='/dashboard')
# app = gr.mount_gradio_app(app, t2speechmuit.demo, path='/t2speechmuit')
# app = gr.mount_gradio_app(app, userspace.app, path='/createspace')

#app = gr.mount_gradio_app(app, audio_interface.demo, path='/manger-audio')





from apps.ui_apps import APPS
for uiapp,path in APPS:
   
    app = gr.mount_gradio_app(app, uiapp, path="/"+path)
    #uiapp.launch(show_error=True,share=True)

from apps.api_routers import APIS
for router,path in  APIS:
     app.include_router(router, prefix=f"/api/{path}")
 
