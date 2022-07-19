from rest_framework import serializers
from .models import Question, Answer, Option

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class OptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'
