from cgi import parse_qs
def application(environ, start_response):
	status = '200 OK'
	output = 'Esto es, ESPARTAAA!!!'
	
	GET = parse_qs(environ['QUERY_STRING'])

	output += "\nGet parameters: \n"
	for key in GET:
		output += key+":" + GET[key][0] + "\n"
	request_body_length = int(environ.get('CONTETNT_LENGTH',0))
	output += "\n------------\n"

	req_body = environ['wsgi.input'].read(request_body_length)

	POST = parse_qs(req_body)
	output += "Post parameters: \n"
	for key in POST:
		output += key+":" + POST[key][0] + "\n"

	response_headers = [(
		'Content-type',
		'text/plain'),
		('Content-Length', str(len(output)) )]

	start_response(status, response_headers)

	return [output]
