from rest_framework import viewsets
from django.db.models import F, Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question, Answer, Option
from .serializer import QuestionSerializers, AnswerSerializers, OptionSerializers

class QuestionViewSet(viewsets.ModelViewSet):
   
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = QuestionSerializers(queryset, many=True)
        return Response(serializer.data)


class AnswerViewSet(viewsets.ModelViewSet):
   
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = AnswerSerializers(queryset, many=True)
        return Response(serializer.data)

    def report(self, request):
        queryset = self.get_queryset()

        correct_answers = queryset.filter(question__expected_answer__alternative=F('option__alternative')).count()
        wrong_answers = queryset.filter(~Q(question__expected_answer__alternative=F('option__alternative'))).count()
        total_question = Question.objects.all().count()

        percentual_performance = correct_answers/total_question if total_question else 0

        data = {
            "Total de Acertos" : correct_answers,
            "Total de Erros": wrong_answers,
            "Aproveitamento": f"{percentual_performance:.2%}"
        }
        return Response(data)


class OptionViewSet(viewsets.ModelViewSet):
   
    queryset = Option.objects.all()
    serializer_class = OptionSerializers
    
    def list(self, request):
        queryset = self.get_queryset()
        serializer = OptionSerializers(queryset, many=True)
        return Response(serializer.data)
