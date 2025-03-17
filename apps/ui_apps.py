from AppUI import create_app
from .chatbot.templates  import TemplateSpeechStudioBuilder
from .CreateAndUpdateSpace.templates  import TemplateSpacePlatformBuilder
from .TextToText.templates  import TemplateTextToTextStudioBuilder
from .TextToSpeech.templates  import TemplateTextToSpeechStudioBuilder
isDev=True

APPS=[
      #(create_app(TemplateSpeechStudioBuilder,isDev),'chatbot'),
      (create_app(TemplateTextToSpeechStudioBuilder,isDev),'TextToSpeech'),
      #(create_app(TemplateSpacePlatformBuilder),'CreateAndUpdateSpace'),
      #(create_app(TemplateTextToTextStudioBuilder,isDev),'TextToText'),

      
]




