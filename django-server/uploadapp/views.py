from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import File
from django.conf import settings
from django.http import FileResponse

from .serializers import FileSerializer

import os


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
      
      file_serializer = FileSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          

class FileListView(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request, ss):
        files = File.objects.filter(session=ss)
        file_serializer = FileSerializer(files, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)    


class FileDeleteView(APIView):
    parser_class = (FileUploadParser,)

    def get_object(self, pk):
        return File.objects.get(pk=pk)

    def delete(self, request, pk):
        try:
            fl = self.get_object(pk)
            fl.file.delete()
            fl.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

class DeleteAllView(APIView):
    parser_class = (FileUploadParser,)

    def delete(self, request, ss):
        try:
            files = File.objects.filter(session=ss)
            for fl in files:
                fl.file.delete()
                fl.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            path = os.path.join(settings.MEDIA_ROOT, ss)
            os.rmdir(path)
        except:
            pass
        return Response(status=status.HTTP_200_OK)

class StubFileDeleteView(APIView):
    parser_class = (FileUploadParser,)

    def delete(self, request, ss):
        sss = ss + "/stub"
        try:
            files = File.objects.filter(session=sss)
            for fl in files:
                fl.file.delete()
                fl.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            path = os.path.join(settings.MEDIA_ROOT, sss)
            os.rmdir(path)
        except:
            pass
        return Response(status=status.HTTP_200_OK)

class StubListView(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request, ss):
        sss = ss+"/stub"
        files = File.objects.filter(session=sss)
        file_serializer = FileSerializer(files, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)

class ResultsFileDeleteView(APIView):
    parser_class = (FileUploadParser,)

    def delete(self, request, ss):
        sss = ss + "/results"
        try:
            files = File.objects.filter(session=sss)
            for fl in files:
                fl.file.delete()
                fl.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            path = os.path.join(settings.MEDIA_ROOT, sss)
            os.rmdir(path)
        except:
            pass
        return Response(status=status.HTTP_200_OK)

class ResultsListView(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request, ss):
        sss = ss+"/results"
        files = File.objects.filter(session=sss)
        file_serializer = FileSerializer(files, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)

class ResultsDownloadView(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request, ss):
        sss = ss+"/results"
        files = File.objects.filter(session=sss)
        instance=files[0]
        file_handle = instance.file.open()

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response


