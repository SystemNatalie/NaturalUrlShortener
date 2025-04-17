from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.shortcuts import redirect
from .utils import generate_urls
import validators
from .models import ShortURL

def dynamic_handler(request, slug):
    """
    Dynamic URL handler. Handles the 3 relevant URLs for this system:
        "shortener": The home page for the URL shortener.
        "doShorten": Makes a request to shorten a URL.
        <other>: Attempts to resolve to a stored URL.
    """
    if slug == 'shortener':                                                                         # Return shortener homepage
        return render(request, "index.html")
    elif slug == 'doShorten':                                                                       # Process shortening request
        return shorten_url(request)
    else:                                                                                           # Try to process and redirect to shortened URL
        try:
            obj = ShortURL.objects.get(short_URL=slug)
            return redirect(obj.original_URL)
        except ShortURL.DoesNotExist:                                                               # Failed to find shortened URL
            raise Http404("Page not found")






def shorten_url(request):                                                                           # Create a shortened URL
    if request.method == "POST":                                                                    # We only want to accept POST requests to this endpoint. No real reason I just feel like it.
        url = request.POST['url']
        if not (url.startswith("http://") or url.startswith("https://")):                           # Add "http://" if the url doesnt declare http/https
            url = "http://" + url
        if validators.url(url):                                                                     # Validate the URL for shortening. We could validate other ways but it doesn't really matter for us as we don't access the URL ourselves.
            try:
                existingShortURLObject = ShortURL.objects.get(original_URL=url)                     # Try to get any existing shortened URL that points to the same original URL
                existingShortURLObject.save()                                                       # Update the most recent access date if we found one
                shortURL=existingShortURLObject.short_URL
            except ShortURL.DoesNotExist:                                                           # If we didn't find the URL in our DB
                shortURL = generate_urls()                                                          # Return either False or a URL string
                if shortURL != False:
                    ShortURL.objects.create(original_URL=url, short_URL=shortURL)                   # Create an unused short-URL and assign it to our object
                else:
                    return HttpResponse("Failed to create URL.", status=500)                # If we fail to create a URL in 10 tries throw a 500
            return show_shorten_results(request, shortURL)                                          # Return a response page containing the shortened URL
        else:
            return HttpResponse("Failed to create URL, invalid URL",status=400)              # Failed to validate URL
    else:
        return HttpResponse("? watcha doin ?", status=403)                                   # Someone may be doing something they shouldn't 0.0

def show_shorten_results(request, shortURL):
    try:
        context={'url':shortURL}
        return render(request, "shortened_url.html", context)                           # Render shortened URL result page, passing the shortened URL for context
    except:
        return HttpResponse("? watcha doin ?", status=403)                                   # Someone may be doing something they shouldn't 0.0


