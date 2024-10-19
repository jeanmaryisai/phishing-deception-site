from django.db import models
import random
import string

def generate_unique_code():
    """Generate a unique alphanumeric code."""
    length = 5  # Adjust length as needed
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(characters, k=length))

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=255)
    unique_code = models.TextField(null=True)

    # Answers of the question one : "where you where born"
    answer_1_question_1 = models.TextField()
    answer_2_question_1= models.TextField()
    correct_answer_1 = models.TextField()

    # Answers of the question two : "what is your date of birth"
    answer_1_question_2 = models.TextField()
    answer_2_question_2 = models.TextField()
    correct_answer_2 = models.TextField()

    # Answers of the question three : "what iss your maiden mother name"
    answer_1_question_3 = models.TextField()
    answer_2_question_3 = models.TextField()
    correct_answer_3 = models.TextField()

    # Answers of the question four: "what is your first love name"
    answer_1_question_4 = models.TextField()
    answer_2_question_4 = models.TextField()
    correct_answer_4 = models.TextField()

    # Answers of the question five: "what is your favorite color"
    answer_1_question_5 = models.TextField()
    answer_2_question_5 = models.TextField()
    correct_answer_5= models.TextField()

    def save(self, *args, **kwargs):
        # Generate a unique code if it hasn't been set yet
        if not self.unique_code:
            code_is_unique = False
            while not code_is_unique:
                generated_code = generate_unique_code()
                # Check if the generated code is unique
                code_is_unique = not Person.objects.filter(unique_code=generated_code).exists()
                if code_is_unique:
                    self.unique_code = generated_code
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    


    
