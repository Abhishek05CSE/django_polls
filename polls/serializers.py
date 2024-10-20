from rest_framework import serializers
from .models import Question,Choice
 
class QuestionSerializer(serializers.ModelSerializer):
     owner = serializers.ReadOnlyField(source='owner.username')
     class Meta:
        model= Question
        fields= ['id','question_text', 'pub_date','owner']
  

class ChoiceSerializer(serializers.ModelSerializer):
    question = QuestionSerializer(read_only = True)
    q_choice = serializers.PrimaryKeyRelatedField(
        queryset= Question.objects.all(),source='question', write_only=True
    )
    class Meta:
        model=Choice
        fields= ['id', 'choice_text', 'votes','question', 'q_choice']
    
 
class QuestionSerializer(serializers.ModelSerializer):
     choices = ChoiceSerializer(many=True, read_only=True, source='choice_set')
     owner = serializers.ReadOnlyField(source='owner.username')
     class Meta:
        model= Question
        fields= ['id','question_text', 'pub_date','owner', 'choices' ]



# class QuestionSerializer(serializers.ModelSerializer):
#      class Meta:
#         model= Question
#         fields= ['id','question_text', 'pub_date']

#         def validate_question_text(self,value):
#             if 'spam' in value.lower():
#                 raise serializers.ValidationError("No spam allowed in question text")
#             return value
        

# validate_fieldname methods allow custom field-level validation.
# validate method for object-level validation.

