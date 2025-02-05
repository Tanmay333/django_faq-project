from rest_framework import serializers
from .models import FAQ
from .utils import translate_text  # No issues here

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()
    translated_answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ["id", "question", "answer", "language", "translated_question", "translated_answer"]

    def get_translated_question(self, obj):
        return translate_text(obj.question, "en")

    def get_translated_answer(self, obj):
        return translate_text(obj.answer, "en")
