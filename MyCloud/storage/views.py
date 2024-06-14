import os
import logging

from django.conf import settings
from django.http import HttpResponse

from dotenv import load_dotenv

from .models import Document
locals()

load_dotenv()

logger = logging.getLogger(__name__)


def redirect_to_document(request, hash):
    try:
        share_link = f"{os.getenv('REACT_APP_API_URL')}/s/{hash}"
        document_obj = Document.objects.get(share_link=share_link)
        response = HttpResponse(document_obj.file)
        response['Content-Disposition'] = f'attachment; filename="{document_obj.filename}"'
        logger.info(f"Document '{document_obj.filename}' provided for download.")
        return response
    except Document.DoesNotExist:
        logger.error("Share link not found.")
        return HttpResponse("Share link not found", status=404)