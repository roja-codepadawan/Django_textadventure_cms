from django.shortcuts import render, get_object_or_404
from .models import Story, Chapter, Choice


def story_list(request):
    stories = Story.objects.all()
    print("Gefundene Storys:", stories)
    return render(request, 'play/story_list.html', {'stories': stories})


def story_start(request, story_id):
    story = get_object_or_404(Story, id=story_id)
    start_chapter = story.chapter_set.filter(is_start=True).first()
    return render(request, "play/chapter.html", {"chapter": start_chapter})


def show_chapter(request, chapter_id):
    chapter = get_object_or_404(Chapter, id=chapter_id)
    return render(request, "play/chapter.html", {"chapter": chapter})
