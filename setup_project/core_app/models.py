from django.db import models

# Create your models here.
class Option(models.Model):
    alternative = models.CharField(max_length=255, blank=True, null=True)     
    
    def __str__(self) -> str:
        return f"{self.alternative}"

class Question(models.Model):
    EXPECTED =(
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )
   
    tittle = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    alternative_a = models.TextField(blank=False, null=False, default="") 
    alternative_b = models.TextField(blank=False, null=False, default="")
    alternative_c = models.TextField(blank=False, null=False, default="")
    alternative_d = models.TextField(blank=False, null=False, default="")
    expected_answer = models.ForeignKey(Option, blank=True, null=False, on_delete=models.DO_NOTHING) 
        
    def __str__(self) -> str:
        return f"{self.tittle}"

class Answer(models.Model):
   
    question = models.OneToOneField(Question, on_delete=models.DO_NOTHING, primary_key=True)     
    option = models.ForeignKey(Option, blank=True, null=True, on_delete=models.DO_NOTHING)     
    
    def __str__(self) -> str:
        return f"Question Tittle: {self.question.tittle}, Expected Answer: {self.question.expected_answer}, Given Answer: {self.option.alternative}"
    ... 


