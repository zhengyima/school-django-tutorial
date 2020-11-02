from django.shortcuts import render
import json
from django.db import connections
from django.http import HttpResponse

def dictfetchall(cursor):
	desc = cursor.description
	return [
	dict(zip([col[0] for col in desc], row))
		for row in cursor.fetchall()
		]

def index(request):

	cursor = connections['default'].cursor()
	# cursor.execute("select * from user limit 1")
	cursor.execute("select * from course")
	raw = dictfetchall(cursor)
	print(raw)

	cursor.execute("select * from sc where sno = '2020200001'")
	raw_tom = dictfetchall(cursor)
	

	context          = {}
	context['hello'] = 'Hello World!'
	context['courses'] = raw
	context['courses_tom'] = raw_tom
	return render(request, 'index.html', context)



def xuanke(request):
	cno = request.GET['cno']
	cursor = connections['default'].cursor()
	cursor.execute("insert into sc values('2020200001',%d)" % int(cno))
	
	print(cno)
	response = HttpResponse(json.dumps({"status":1}),content_type="application/json")
	response["Access-Control-Allow-Origin"] = "*"
	response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
	response["Access-Control-Max-Age"] = "1000"
	response["Access-Control-Allow-Headers"] = "*"
	return response

