import re

from django.db.models import Count
from django.db.models.functions import Round
from django.db.models.functions.math import Ln
from django.shortcuts import render

from text_handler.forms import DocumentForm
from text_handler.models import Document, Word


def index(request):
    template = 'text_handler/index.html'
    if request.method == 'POST':
        form = DocumentForm(request.POST or None, files=request.FILES or None)
        if form.is_valid():
            file = form.save(commit=False)
            file.name = request.FILES['file'].name
            file.save()
            words = file.file.instance.file.read().decode('UTF-8').lower()
            words = re.sub(r'[^\w\s]', '', words).split()
            tfidf = calculate(words, file)
            return render(request, 'text_handler/good.html', context={
                'page_obj': tfidf,
                'num_docs': count_doc_obj(),
                'num_words': Word.objects.all().count()
            })
        return render(request, template, {'form': form})
    form = DocumentForm()
    return render(request, template, {'form': form})


def calculate(words: list, file: Document) -> list[dict]:
    tf = [
        {
            'word': word,
            'tf': "{:.2f}".format(words.count(word)/len(words))
        } for word in words]
    objs = [
        Word(
            word=word, count=words.count(word), document=file
        ) for word in words
    ]
    Word.objects.bulk_create(objs)
    num_docs = count_doc_obj()
    idf = Word.objects.values('word').filter(word__in=words).annotate(
        idf=Round(Ln(num_docs*1.0/Count('word')), 2)).values('word', 'idf')
    l1 = {d['word']: d for d in tf}
    tfidf = [dict(
        d,
        **l1.get(d['word']),
        **{'tfidf': '%.2f' % (d['idf']*float(l1.get(d['word'])['tf']))}
    ) for d in idf]
    tfidf = sorted(tfidf, key=lambda x: x['tf'], reverse=True)
    return tfidf


def count_doc_obj() -> int:
    return Document.objects.all().count()
