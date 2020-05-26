from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

from django.db.models import Q

# Create your views here.
def home(request):
	# query = ""
	# if request.GET:
	# 	query = request.GET['q']
	# 	context['query'] = str(query)
	# tags = Product.objects.tags
	products = Product.objects
	return render(request, 'products/home.html',{'products':products})

def search(request):
	products = Product.objects
	return render(request, 'products/search.html',{'products':products})

# def search(query=None):
# 	queryset = []
# 	queries = query.split(" ") # samsung s8 -> queryset = [samsung, s8]
# 	for q in queries:
# 		posts = Product.objects.filter(
# 				Q(title__icontrains=q) | Q(body__icontains=q)
# 			).distinct()

# 		for post in posts:
# 			queryset.append(post)

# 	return list(set(queryset))



@login_required(login_url="/accounts/signup")
def create(request):
	if request.method == 'POST':
		# Add exception
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
			product = Product()
			product.title = request.POST['title']
			product.body = request.POST['body']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				product.url = request.POST['url']
			else:
				product.url = 'http://' + request.POST['url']
			product.icon = request.FILES['icon']
			product.image = request.FILES['image']
			product.pub_date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			return redirect('/products/' + str(product.id))

		else:
			return render(request, 'products/create.html', {'error':'All fields are required.'})
	else:
		return render(request, 'products/create.html')


def detail(request, product_id):
	product = get_object_or_404(Product, pk=product_id)
	return render(request, 'products/detail.html', {'product':product})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
	if request.method == 'POST':
		product = get_object_or_404(Product, pk=product_id)
		product.votes_total += 1
		product.save()
		return redirect('/products/' + str(product.id))

# def search(query=None):
# 	queryset = []
# 	queryset = query.split(" ") # samsung s8 -> queryset = [samsung, s8]
# 	for q in queries:
# 		posts = Product.objects.filter(
# 				Q(title__icontrains=q) | Q(body__icontains=q)
# 			).distinct()

# 		for post in posts:
# 			queryset.append(post)

# 	return list(set(queryset))












