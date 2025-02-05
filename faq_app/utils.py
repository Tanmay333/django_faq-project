from django.utils.translation import gettext_lazy as _
from googletrans import Translator

translator = Translator()

def translate_text(text, dest_language="en"):
    """Translate text to the specified language."""
    return translator.translate(text, dest=dest_language).text

def some_function():
    from faq_app.views import FAQViewSet, home_view  # Import inside function to prevent circular import
    # Your code here...
