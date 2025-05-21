from AppUI import create_api
from .t2text.templates  import TemplateTextToTextStudioBuilder,TemplateTextToTextBuilder
from .chatbot.templates  import TemplateSpeechStudioBuilder
from .space.templates  import TemplateSpacePlatformBuilder
isDev=True
APIS=[
  (create_api(TemplateSpeechStudioBuilder,isDev),'/user')
  (create_api(TemplateTextToTextStudioBuilder,isDev),'/textstudiorouter'),
]
