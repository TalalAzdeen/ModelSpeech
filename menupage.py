import gradio as gr

routes = [
    ('createspace', '🚀 Create Space'),
    ('dashboard', '📊 Dashboard'),
    ('chatbot', '🗣️ Chatbot'),
    ('t2text', '📝 Text to Text'),
    ('studio-t2text', '🎛️ T2Text Studio'),
    ('t2speech', '🔊 Text to Speech'),
    ('studio-t2speech', '🎙️ T2Speech Studio'),
]

def build_menu_html(routes, base_url, token):
    # إذا أردت استخدام التوكن في الرابط (مثلاً كـ param) يمكن تضمينه هنا
    token_param = f"?token={token}" if token else ""

    html = f"""
    <div style="
        max-width: 450px; 
        margin: 30px auto; 
        padding: 30px; 
        background: #f9f9f9; 
        border-radius: 15px; 
        box-shadow: 0 8px 16px rgba(0,0,0,0.15);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    ">
        <h2 style="text-align:center; color:#333; margin-bottom: 20px;">📂 Applications Menu</h2>
        <ul style="list-style:none; padding-left:0;">
    """
    for path, label in routes:
        full_url = f"{base_url}/{path}{token_param}"
        html += f"""
        <li style="margin: 12px 0; text-align:center;">
            <a href="{full_url}" target="_blank" 
               style="
                    text-decoration:none; 
                    font-size:18px; 
                    color:#007bff; 
                    padding: 10px 15px; 
                    display: inline-block; 
                    border-radius: 8px; 
                    transition: background-color 0.3s ease;
                "
               onmouseover="this.style.backgroundColor='#e6f0ff';" 
               onmouseout="this.style.backgroundColor='transparent';"
            >{label}</a>
        </li>
        """
    html += "</ul></div>"
    return html

def update_menu(base_url, token):
    # تحقق من أن الرابط الأساسي يبدأ بـ http:// أو https://
    if not base_url.startswith("http://") and not base_url.startswith("https://"):
        base_url = "https://" + base_url
    return build_menu_html(routes, base_url, token)

with gr.Blocks() as demo:
    gr.Markdown("## 🔑 Enter Server Base URL and Token (optional)")
    with gr.Row():
        base_url_input = gr.Textbox(label="Server Base URL", value="https://modelspeech-sy6y.onrender.com", max_lines=1)
        token_input = gr.Textbox(label="Token", placeholder="Enter your token here (optional)", max_lines=1)
    menu_html = gr.HTML()
    
    # ربط التغيير لتحديث القائمة تلقائيًا
    base_url_input.change(fn=update_menu, inputs=[base_url_input, token_input], outputs=menu_html)
    token_input.change(fn=update_menu, inputs=[base_url_input, token_input], outputs=menu_html)
    
    # تهيئة العرض عند بدء التشغيل
    demo.load(fn=update_menu, inputs=[base_url_input, token_input], outputs=menu_html)

#demo.launch()
