from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import File
from django.conf import settings
from django.http import FileResponse

from .serializers import FileSerializer

import os,subprocess


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
                print (fl)
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
                print (fl)
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
        sss = ss+"/results/result.csv"
        #files = File.objects.get(session=sss)
        instance=File.objects.get(file=sss)
        file_handle = instance.file.open()
        print (file_handle)
        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response

class FalseResultsProcessView(APIView):
    parser_class = (FileUploadParser,)
   
    def get(self, request, ss):
        sss=ss+"/results"
        #print (sss)
        cmd = 'python3 plag_check.py "' + settings.MEDIA_ROOT + '/' + ss + '" F'
        #print (settings.MEDIA_ROOT)
        os.system(cmd)
        files = File()
        files.file=sss+'/result.csv'
        files.session=sss
        files.save()
        filess = File.objects.filter(session=sss)
        file_serializer = FileSerializer(filess, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)

class TrueResultsProcessView(APIView):
    parser_class = (FileUploadParser,)
   
    def get(self, request, ss):
        sss=ss+"/results"
        #print (sss)
        cmd = 'python3 plag_check.py "' + settings.MEDIA_ROOT + '/' + ss + '" T'
        #print (settings.MEDIA_ROOT)
        os.system(cmd)
        files = File()
        files.file=sss+'/result.csv'
        files.session=sss
        files.save()
        filess = File.objects.filter(session=sss)
        file_serializer = FileSerializer(filess, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)


class CreatePlotsView(APIView):

    def get(self, request, ss):
        #print (ss)
        sss=ss+"/plots"

        files = File.objects.filter(session=sss)
        for fl in files:
            print (fl)
            fl.file.delete()
            fl.delete()
        
        cmd = 'python3 plots_create.py "' + settings.MEDIA_ROOT + '/' + ss + '" A'
        #print (settings.MEDIA_ROOT)
        os.system(cmd)
        files = File()
        files.file=sss+'/surfacePlot.png'
        files.session=sss
        files.save()
        
        
        files = File()
        files.file=sss+'/heatmap.png'
        files.session=sss
        files.save()
        
        files = File()
        files.file=sss+'/markers.txt'
        files.session=sss
        files.save()

        #files = File.objects.filter(session=sss)
        #print (sss)
        #print (files)
        instance=File.objects.get(file=sss+"/surfacePlot.png")
        file_handle = instance.file.open()
        #print(file_handle)

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response
        
class HeatMapView(APIView):

    def get(self, request, ss):
        sss = ss+"/plots/heatmap.png"

        instance=File.objects.get(file=sss)
        file_handle = instance.file.open()
        print (file_handle)
        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response

class MarkersView(APIView):

    def get(self, request, ss):
        sss = ss+"/plots/markers.txt"

        instance=File.objects.get(file=sss)
        file_handle = instance.file.open()
        print (file_handle)
        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response

class GetListView(APIView):

    def post(self, request, ss):
        print(request.data['list'])
        
        sss=ss+"/plots"

        files = File.objects.filter(session=sss)
        for fl in files:
            print (fl)
            fl.file.delete()
            fl.delete()
        
        cmd = 'python3 plots_create.py "' + settings.MEDIA_ROOT + '/' + ss + '" S "' + request.data['list']+'" '
        #print (settings.MEDIA_ROOT)
        os.system(cmd)
        files = File()
        files.file=sss+'/surfacePlot.png'
        files.session=sss
        files.save()
        
        
        files = File()
        files.file=sss+'/heatmap.png'
        files.session=sss
        files.save()
        
        files = File()
        files.file=sss+'/markers.txt'
        files.session=sss
        files.save()

        return Response(status=status.HTTP_200_OK)

class SomePlotView(APIView):

    def get(self,request,ss):
        sss=ss+"/plots"
        
        instance=File.objects.get(file=sss+"/surfacePlot.png")
        file_handle = instance.file.open()
        #print(file_handle)

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response