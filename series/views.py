from django.shortcuts import render, get_object_or_404, redirect

from series.models import EpisodeReview, Series, Episode
from series.forms import GiveReviewForm
from accounts.models import Account

def give_episode_review(request, episode_id):

    context = {}

    user = request.user
    episode = get_object_or_404(Episode, id=episode_id)
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = GiveReviewForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.episode = episode
        obj.author = user
        obj.save()
        form = GiveReviewForm()

    context['form']=form

    return render(request, 'give_episode_review.html', context)

def select_series(request):
    series = Series.objects.all()
    context = {'series':series}

    return render(request, 'select_series.html', context)

def select_episode(request, series_id):
    episodes = Episode.objects.all()
    context = {'episodes':episodes}

    return render(request, 'select_episode.html', context)
