from rest_framework import serializers

from .models import Answer, Question


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_answers(self, obj):
        results = obj.answers.all()
        serializer = AnswerSerializer(results, many=True)
        return serializer.data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
