from django.shortcuts import render


def search(request):
    """
    Search function view to view search results
    """
    if request.method == "POST":
        searched = request.POST['searched']
        return render(request, 'search_bar/search.html',
                      {'searched': searched})
    else:
        return render(request, 'search_bar/search.html', {})
