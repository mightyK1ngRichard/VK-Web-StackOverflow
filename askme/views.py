from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    class Question:
        def __init__(self, title, content, author_img):
            self.title = title
            self.content = content
            self.author_img = author_img

    questions = [
        Question('Sample Title',
                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor at odio tempus scelerisque.',
                 'https://sun9-76.userapi.com/impg/9UT7SzAC_gHL2GBES69P-hXudzqKmS8_f0oPXA/AN2fmitt7Bs.jpg?size=1080x1920&quality=95&sign=812fa659cab85e0be2fc74516dc27ae7&type=album'),
        Question('Sample Title',
                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor at odio tempus scelerisque.',
                 'https://sun9-76.userapi.com/impg/9UT7SzAC_gHL2GBES69P-hXudzqKmS8_f0oPXA/AN2fmitt7Bs.jpg?size=1080x1920&quality=95&sign=812fa659cab85e0be2fc74516dc27ae7&type=album'),
        Question('Sample Title',
                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor at odio tempus scelerisque.',
                 'https://sun9-76.userapi.com/impg/9UT7SzAC_gHL2GBES69P-hXudzqKmS8_f0oPXA/AN2fmitt7Bs.jpg?size=1080x1920&quality=95&sign=812fa659cab85e0be2fc74516dc27ae7&type=album'),
        Question('Sample Title',
                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor at odio tempus scelerisque.',
                 'https://sun9-76.userapi.com/impg/9UT7SzAC_gHL2GBES69P-hXudzqKmS8_f0oPXA/AN2fmitt7Bs.jpg?size=1080x1920&quality=95&sign=812fa659cab85e0be2fc74516dc27ae7&type=album'),
        Question('Sample Title',
                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor at odio tempus scelerisque.',
                 'https://sun9-76.userapi.com/impg/9UT7SzAC_gHL2GBES69P-hXudzqKmS8_f0oPXA/AN2fmitt7Bs.jpg?size=1080x1920&quality=95&sign=812fa659cab85e0be2fc74516dc27ae7&type=album'),
        Question('Sample Title',
                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor at odio tempus scelerisque.',
                 'https://sun9-76.userapi.com/impg/9UT7SzAC_gHL2GBES69P-hXudzqKmS8_f0oPXA/AN2fmitt7Bs.jpg?size=1080x1920&quality=95&sign=812fa659cab85e0be2fc74516dc27ae7&type=album'),
        Question('Sample Title',
                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor at odio tempus scelerisque.',
                 'https://sun9-76.userapi.com/impg/9UT7SzAC_gHL2GBES69P-hXudzqKmS8_f0oPXA/AN2fmitt7Bs.jpg?size=1080x1920&quality=95&sign=812fa659cab85e0be2fc74516dc27ae7&type=album'),
        Question('Sample Title',
                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor at odio tempus scelerisque.',
                 'https://sun9-76.userapi.com/impg/9UT7SzAC_gHL2GBES69P-hXudzqKmS8_f0oPXA/AN2fmitt7Bs.jpg?size=1080x1920&quality=95&sign=812fa659cab85e0be2fc74516dc27ae7&type=album'),
        Question('Sample Title',
                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tortor at odio tempus scelerisque.',
                 'https://sun9-76.userapi.com/impg/9UT7SzAC_gHL2GBES69P-hXudzqKmS8_f0oPXA/AN2fmitt7Bs.jpg?size=1080x1920&quality=95&sign=812fa659cab85e0be2fc74516dc27ae7&type=album'),
    ]

    return render(request, 'index.html', {'questions': questions})


def ask_question(request):
    return render(request, 'ask_question.html')


def settings(request):
    return render(request, 'settings.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def question(request, question_id):
    answers = [
        'Просто какой-то текст',
        'Просто какой-то текст',
        'Просто какой-то текст',
        'Просто какой-то текст',
        'Просто какой-то текст',
    ]
    return render(request, 'question.html', {'answers': answers})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
