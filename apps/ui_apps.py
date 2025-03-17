from AppUI import create_app
from .chatbot.templates  import TemplateSpeechStudioBuilder
from .space.templates  import TemplateSpacePlatformBuilder
from .t2text.templates  import TemplateTextToTextStudioBuilder
from .t2speech.templates  import TemplateTextToSpeechStudioBuilder
isDev=True

APPS=[
      #(create_app(TemplateSpeechStudioBuilder,isDev),'chatbot'),
      (create_app(TemplateTextToSpeechStudioBuilder,isDev),'TextToSpeech'),
      #(create_app(TemplateSpacePlatformBuilder),'CreateAndUpdateSpace'),
      #(create_app(TemplateTextToTextStudioBuilder,isDev),'TextToText'),

      
]




