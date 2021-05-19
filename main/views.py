from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def main(request):
	return render(request, "main.html")


@login_required
def cabinet(request):
	return render(request, "cabinet.html")


def about(request):
	return render(request, "about_us.html")


def contact(request):
	return render(request, "contact.html")