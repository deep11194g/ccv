import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from lib import post_parser


@csrf_exempt
def bulk_create(request):
    """Controller function to read XML file from given link and creating posts"""
    if not request.method == "POST":
        return JsonResponse({'message': 'Method should be POST'}, status=405)
    request_body = json.loads(request.body)
    xml_url = request_body.get('url')
    if not xml_url:
        return JsonResponse({'message': 'Body should have key `url`'}, status=400)
    create_count = post_parser.create_posts_from_xml(xml_url)
    return JsonResponse({'created_count': create_count})
