from django.shortcuts import render
import wikipediaapi

# Create your views here.
def index(request):
	return render(request,'index.html')

def wiki(request):
	wiki_wiki = wikipediaapi.Wikipedia('en')
	if 'search' in request.GET:
		search = request.GET['search']

		page = wiki_wiki.page(search)

		links = page.links
		availableLinks=[]
		for title in sorted(links.keys()):
			availableLinks.append(title)

		if page.exists()==True:
			context={"pageExist":"Page Exists",
					 "pageTitle":page.title,
					 "pageSummary":page.summary[0:1000],
					 "pageLinks":availableLinks,}
		else:
			context={"pageExist":"Invalid Search"}
	else:
		context={"pageExist":"Page Does not Exist"}

	return render(request,'api/wiki.html',context)