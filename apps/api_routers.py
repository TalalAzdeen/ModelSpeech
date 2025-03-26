from AppUI import create_api

from .chatbot.templates  import TemplateSpeechStudioBuilder
from .space.templates  import TemplateSpacePlatformBuilder
isDev=False
APIS=[
  (create_api(TemplateSpeechStudioBuilder,isDev),'/user'),
  (create_api(TemplateSpacePlatformBuilder,isDev),'/spaceapi')
]
