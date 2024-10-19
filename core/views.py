from django.shortcuts import render,redirect
from .models import Person


# Create your views here.
def home(request):
    if request.method == 'POST':
        code = request.POST.get('quiz_code')
        person = Person.objects.get(unique_code=code)
        if person:
            print('line 11')
            return redirect('reponn', slug=code)
        else:
            return render(request, 'index.html', {'messages': 'Invalid code'}) 
    return render(request, 'index.html')


# views.py


def create_answers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        answer_1_question_1 = request.POST.get('answer_1_question_1')
        answer_2_question_1 = request.POST.get('answer_2_question_1')
        correct_answer_1 = request.POST.get('correct_answer_1')

        answer_1_question_2 = request.POST.get('answer_1_question_2')
        answer_2_question_2 = request.POST.get('answer_2_question_2')
        correct_answer_2 = request.POST.get('correct_answer_2')

        answer_1_question_3 = request.POST.get('answer_1_question_3')
        answer_2_question_3 = request.POST.get('answer_2_question_3')
        correct_answer_3 = request.POST.get('correct_answer_3')

        answer_1_question_4 = request.POST.get('answer_1_question_4')
        answer_2_question_4 = request.POST.get('answer_2_question_4')
        correct_answer_4 = request.POST.get('correct_answer_4')

        answer_1_question_5 = request.POST.get('answer_1_question_5')
        answer_2_question_5 = request.POST.get('answer_2_question_5')
        correct_answer_5 = request.POST.get('correct_answer_5')

        # Create a new Person object
        person = Person(
            name=name,
            answer_1_question_1=answer_1_question_1,
            answer_2_question_1=answer_2_question_1,
            correct_answer_1=correct_answer_1,
            answer_1_question_2=answer_1_question_2,
            answer_2_question_2=answer_2_question_2,
            correct_answer_2=correct_answer_2,
            answer_1_question_3=answer_1_question_3,
            answer_2_question_3=answer_2_question_3,
            correct_answer_3=correct_answer_3,
            answer_1_question_4=answer_1_question_4,
            answer_2_question_4=answer_2_question_4,
            correct_answer_4=correct_answer_4,
            answer_1_question_5=answer_1_question_5,
            answer_2_question_5=answer_2_question_5,
            correct_answer_5=correct_answer_5
        )
        person.save()  # Save the person instance to the database

        # Redirect to success page with unique code
        return render(request, 'success.html', {'unique_code': person.unique_code})

    return render(request, 'create.html')


    if request.method == 'POST':
        answer_1_question_1 = request.POST.get('answer_1_question_1')
        answer_2_question_1= request.POST.get('answer_2_question_1')
        correct_answer_1 = request.POST.get('correct_answer_1')

        # Answers of the question two : "what is your date of birth"
        answer_1_question_2 = request.POST.get('answer_1_question_2')
        answer_2_question_2 = request.POST.get('answer_2_question_2')
        correct_answer_2 = request.POST.get('correct_answer_2')

        # Answers of the question three : "what iss your maiden mother name"
        answer_1_question_3 = request.POST.get('answer_1_question_3')
        answer_2_question_3 = request.POST.get('answer_1_question_3')
        correct_answer_3 = request.POST.get('correct_answer_3')

        # Answers of the question four: "what is your first love name"
        answer_1_question_4 = request.POST.get('answer_1_question_4')
        answer_2_question_4 = request.POST.get('answer_2_question_4')
        correct_answer_4 = request.POST.get('correct_answer_4')

        # Answers of the question five: "what is your favorite color"
        answer_1_question_5 = request.POST.get('answer_1_question_5')
        answer_2_question_5 = request.POST.get('answer_2_question_5')
        correct_answer_5= request.POST.get('correct_answer_5')

        Person.objects.create(
            name=request.POST.get('name'),
            answer_1_question_1=answer_1_question_1,
            answer_2_question_1=answer_2_question_1,
            correct_answer_1=correct_answer_1,
            answer_1_question_2=answer_1_question_2,
            answer_2_question_2=answer_2_question_2,
            correct_answer_2=correct_answer_2,
            answer_1_question_3=answer_1_question_3,
            answer_2_question_3=answer_2_question_3,
            correct_answer_3=correct_answer_3,
            answer_1_question_4=answer_1_question_4,
            answer_2_question_4=answer_2_question_4,
            correct_answer_4=correct_answer_4,
            answer_1_question_5=answer_1_question_5,
            answer_2_question_5=answer_2_question_5,
            correct_answer_5=correct_answer_5,
        )

        return render(request, 'index.html', {'message': f'Ou kreye quiz ou a ak sikse itilize kod sa {Person.unique_code} pou moun ka vinn pase tes la'})
    return render(request, 'create.html')

def reponn(request,slug):
    person = Person.objects.get(unique_code=slug)
    if request.method == 'POST':
        # Collecting answers from the form
        name = request.POST.get('name')
        # Collecting answers to questions
        answer_1 = request.POST.get('answer_1')
        answer_2 = request.POST.get('answer_2')
        answer_3 = request.POST.get('answer_3')
        answer_4 = request.POST.get('answer_4')
        answer_5 = request.POST.get('answer_5')

        # Check answers
        correct_count = 0
        print(f"answer given {answer_1} {answer_2} {answer_3} {answer_4}, answer correct:{person.correct_answer_1}")
        if answer_1 == person.correct_answer_1:
            correct_count += 1
        if answer_2 == person.correct_answer_2:
            correct_count += 1
        if answer_3 == person.correct_answer_3:
            correct_count += 1
        if answer_4 == person.correct_answer_4:
            correct_count += 1
        if answer_5 == person.correct_answer_5:
            correct_count += 1

        # Process the answers (store them, return a response, etc.)
        # Redirecting to a success page or rendering results
        
        return render(request, 'index.html', {'message': f'{name} ou fe {correct_count} sou 5 pou {person.name}, fe youn tou pou patagl bay zanmiw',})

    return render(request, 'questions.html', {'person':person})