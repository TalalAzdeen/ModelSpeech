from AppUI import create_api
from .chatbot.templates  import TemplateSpeechStudioBuilder
from .space.templates  import TemplateSpacePlatformBuilder
from .dashboard.templates  import TamplateDashBuilder
from .t2text.templates  import TemplateTextToTextStudioBuilder,TemplateTextToTextBuilder
from .t2speech.templates  import TemplateTextToSpeechStudioBuilder,TemplateTextToSpeechBuilder
isDev=True
APIS=[
  (create_api(TemplateSpeechStudioBuilder,isDev),'/user')
  (create_api(TemplateTextToTextStudioBuilder,isDev),'/textstudiorouter'),
]
