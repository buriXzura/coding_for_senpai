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

    """! The file upload class.
    Registers the file in 'File model' and saves it in the media.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        """! Uploads the files. After the files are added to the queue, the files are
        uploaded to the server and the data is saved in case
        of success and error is returned in case of failure.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param *args used to pass a non-key worded, variable-length argument list
        @param **kwargs used to pass a keyworded, variable-length argument list
        @return response with requested data if valid and a status 201,
                 else response with error and a status 400
        """

    	file_serializer = FileSerializer(data=request.data)

    	if file_serializer.is_valid():
        	file_serializer.save()
        	return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    	else:
        	return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListView(APIView):

    """! The class that lists given files.
    It queries the database for files with the provided session
    and returns the resulting list of files.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def get(self, request, ss):

        """! Lists the uploaded files. The files which are uploaded by post function are
        listed under that user's session folder.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return response with status 200
        """

        files = File.objects.filter(session=ss)
        file_serializer = FileSerializer(files, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)


class FileDeleteView(APIView):

    """! The class that deletes a specfic file.
    Child functions retrieve the instance of that file and then delete that single file.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def get_object(self, pk):

        """! Gets that particular file object instance
        @param self reference to the current instance of the class
        @param pk instance of that particular file
        @return the file instance
        """

        return File.objects.get(pk=pk)

    def delete(self, request, pk):

        """! Deletes a single file. It first checks if the file exists and if it does then gets the
        file object instance and deletes it from the backend server.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param pk instance of that particular file
        @return response with status 200 if successful deletion,
                 else response with 404 if file not found
        """

        try:
            fl = self.get_object(pk)
            #file gets deleted
            fl.file.delete()
            fl.delete()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DeleteAllView(APIView):

    """! The class that deletes all files in the media of a particular user.
    Gets all the files particular to that session (user) which are currently
    there in the backend and then deletes each file one by one.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def delete(self, request, ss):

        """! Deletes all files. Gets all the files particular to that session (user) which are currently
        there in the backend and then deletes each file one by one unless any
        file went missing in which case it will throw an error and thereafter
        also deletes the folder corresponding to that particular session.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return response with status 200 if successful deletion,
                 else response with status 404 if any file not found
        """

        try:
            files = File.objects.filter(session=ss)
            for fl in files:
            	#file gets deleted
                fl.file.delete()
                fl.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            path = os.path.join(settings.MEDIA_ROOT, ss)
            #session folder gets deleted
            os.rmdir(path)
        except:
            pass
        return Response(status=status.HTTP_200_OK)


class StubFileDeleteView(APIView):

    """! The class that deletes the stub files.
    Gets the stub files particular to that session (user) which are currently
    there in the backend and then deletes them as well as the stub folder.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def delete(self, request, ss):
        #
        """! Deletes the stub files. Gets the stub files particular to that session (user) which are currently
        present in the backend inside the stub folder within the current session
        folder and then deletes the files unless some error is thrown and thereafter
        also deletes the stub folder corresponding to that particular session.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return response with status 200 if successful deletion,
                 else response with status 404 if any file not found
        """

        #path to stub folder for stub file
        sss = ss + "/stub"
        try:
            files = File.objects.filter(session=sss)
            for fl in files:
                print (fl)
                #file gets deleted
                fl.file.delete()
                fl.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            path = os.path.join(settings.MEDIA_ROOT, sss)
            #stub folder gets deleted
            os.rmdir(path)
        except:
            pass
        return Response(status=status.HTTP_200_OK)



class StubListView(APIView):

    """! The class that lists the stub files.
    It queries the database for the stub files with the provided session
    and returns the resulting list of stub files.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def get(self, request, ss):

        """! Lists the stub files. The stub files which are uploaded by post function are listed
        under that user's stub folder which is within the session folder.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return response with status 200
        """

        #path to stub folder for stub file
        sss = ss+"/stub"
        files = File.objects.filter(session=sss)
        file_serializer = FileSerializer(files, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)


class ResultsFileDeleteView(APIView):

    """! The class that deletes result files.
    Gets the result files particular to that session (user) which are currently
    there in the backend and then deletes them as well as the results folder.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def delete(self, request, ss):

        """! Deletes the results files. Gets the results files particular to that session (user) which are currently
        present in the backend inside the results folder within the current session
        folder and then deletes the files unless some error is thrown and thereafter
        also deletes the results folder corresponding to that particular session.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return response with status 200 if successful deletion,
                 else response with status 404 if any file not found
        """

        #path to results folder for csv file
        sss = ss + "/results"
        try:
            files = File.objects.filter(session=sss)
            for fl in files:
                print (fl)
                #file gets deleted
                fl.file.delete()
                fl.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            path = os.path.join(settings.MEDIA_ROOT, sss)
            #results folder gets deleted
            os.rmdir(path)
        except:
            pass
        return Response(status=status.HTTP_200_OK)



class ResultsListView(APIView):

    """! The class that lists the result files.
    It queries the database for result files with the provided session
    and returns the resulting list of result files.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def get(self, request, ss):

        """! Lists the results files. The results files which are uploaded by post function are listed
        under that user's results folder which is within the session folder.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return response with status 200
        """

        #path to results folder for csv file
        sss = ss+"/results"
        files = File.objects.filter(session=sss)
        file_serializer = FileSerializer(files, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)



class ResultsDownloadView(APIView):

    """! The download class for the csv result file.
    Creates an instance of the csv file and downloads it.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def get(self, request, ss):
        #
        """! Downloads csv file. Creates an instance of csv file which will contain the
        covariance matrix and associated parameters are given to it.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return file response associated with csv file
        """

        #path to csv file
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

    """! The class that processes false results. The core logic is run on files
    in the current session folder, and the resulting csv file is saved in the backend.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def get(self, request, ss):

        """! Processes false results. A command line argument is passed with an argument F (false) to
        run the core logic with files present within the session folder
        and then csv file is created and saved in the backend present
        within the results folder inside the session (user) folder.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return response with status 200
        """

        #path to results folder for csv file
        sss=ss+"/results"
        #print (sss)
        #command line argument passed for core logic with F (false) argument
        cmd = 'python3 plag_check.py "' + settings.MEDIA_ROOT + '/' + ss + '" F'
        #print (settings.MEDIA_ROOT)
        os.system(cmd)
        files = File()
        #saving the csv file
        files.file=sss+'/result.csv'
        files.session=sss
        files.save()
        filess = File.objects.filter(session=sss)
        file_serializer = FileSerializer(filess, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)



class TrueResultsProcessView(APIView):

    """! The class that processes true results. The core logic is run on files
    in the current session folder, and the resulting csv file is saved in the backend.
    """

    ## The file upload parser for the class
    parser_class = (FileUploadParser,)

    def get(self, request, ss):

        """! Processes true results. A command line argument is passed with an argument T (true) to
        run the core logic with files present within the session folder
        and then csv file is created and saved in the backend present
        within the results folder inside the session (user) folder.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return response with status 200
        """

        #path to results folder for csv file
        sss=ss+"/results"
        #print (sss)
        #command line argument passed for core logic with T (true) argument
        cmd = 'python3 plag_check.py "' + settings.MEDIA_ROOT + '/' + ss + '" T'
        #print (settings.MEDIA_ROOT)
        os.system(cmd)
        files = File()
        #saving the csv file
        files.file=sss+'/result.csv'
        files.session=sss
        files.save()
        filess = File.objects.filter(session=sss)
        file_serializer = FileSerializer(filess, many=True)
        return Response(file_serializer.data, status=status.HTTP_200_OK)


class CreatePlotsView(APIView):

    """! The class that creates different plots and returns the instance for surface plot.
    The plots_create file is run on the result csv files present in the backend corresponding
    to the current session. A surface plot, heatmap and markers text file are created and saved to the backend.
    """

    def get(self, request, ss):

        """! Creates different plots and returns the instance for surface plot. First all the previous plot files present in the plots folder is deleted
        and then a command line argument is passed with an argument A (all) to run the
        plots creating file with files present within the session folder and then 3
        files are created. One is a surface plot, second one is a heatmap and
        lastly a markers text file denoting all the files and all three files are
        saved within the plots folder within the session (user) folder.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return file response associated with the surface plot file
        """

        #print (ss)
        #path to plots folder for different plots
        sss=ss+"/plots"

        files = File.objects.filter(session=sss)
        for fl in files:
            print (fl)
            #plot gets deleted
            fl.file.delete()
            fl.delete()

        #command line argument passed for creating plots with A (all) argument
        cmd = 'python3 plots_create.py "' + settings.MEDIA_ROOT + '/' + ss + '" A'
        #print (settings.MEDIA_ROOT)
        os.system(cmd)
        files = File()
        #saving the surface plot
        files.file=sss+'/surfacePlot.png'
        files.session=sss
        files.save()


        files = File()
        #saving the heatmap
        files.file=sss+'/heatmap.png'
        files.session=sss
        files.save()

        files = File()
        #saving the markers text file
        files.file=sss+'/markers.txt'
        files.session=sss
        files.save()

        #files = File.objects.filter(session=sss)
        #print (sss)
        #print (files)

        #path to surface plot
        instance=File.objects.get(file=sss+"/surfacePlot.png")
        file_handle = instance.file.open()
        #print(file_handle)

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response


class HeatMapView(APIView):

    """! The class that returns the instance for the result heatmap.
    Retrieves the heatmap instance from the file backend given the session id of the current user.
    """

    def get(self, request, ss):

        """! Returns the instance for the heatmap.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return file response associated with the heatmap file
        """

        #path to heatmap
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

    """! The class that returns the instance for the result markers text file.
    Retrieves the markers text file instance from the file backend given the session id of the current user.
    """

    def get(self, request, ss):

        """! Returns the instance for markers text file.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return file response associated with the markers text file
        """

        #path to markers text file
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

    """! The class that creates different plots only for the selected files.
    Given a list of files to be plotted and the current session folder, the surface plot,
    heatmap and markers text file are generated and saved only for the selected files.
    """

    def post(self, request, ss):

        """! Creates different plots only for the selected files. First all the previous plot files present in the plots folder is deleted and
        then a command line argument is passed with an argument S (selected) and another
        argument having the list of files to be plotted to run the plots creating file
        with files present within the session folder and then 3 files are created. One is
        a surface plot, second one is a heatmap and lastly a markers text file denoting
        only the selected files and all three files are saved within the plots folder
        within the session (user) folder.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return  response with status 200
        """
        print(request.data['list'])
        #path to plots folder for different plots
        sss=ss+"/plots"

        files = File.objects.filter(session=sss)
        for fl in files:
            print (fl)
            #deleting the plots
            fl.file.delete()
            fl.delete()

        #command line argument passed for creating plots with S (selected) argument
        #and the list of selected files passed as another argument
        cmd = 'python3 plots_create.py "' + settings.MEDIA_ROOT + '/' + ss + '" S "' + request.data['list']+'" '
        #print (settings.MEDIA_ROOT)
        os.system(cmd)
        files = File()
        #saving the surface plot
        files.file=sss+'/surfacePlot.png'
        files.session=sss
        files.save()


        files = File()
        #saving the heatmap
        files.file=sss+'/heatmap.png'
        files.session=sss
        files.save()

        files = File()
        #saving the markers text file
        files.file=sss+'/markers.txt'
        files.session=sss
        files.save()

        return Response(status=status.HTTP_200_OK)


class SomePlotView(APIView):

    """! The class that returns the instance for the result surface plot.
    Retrieves the surface plott instance from the file backend given the session id of the current user.
    """

    def get(self,request,ss):
        #
        """! Returns the instance for the surface plot.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return file response associated with the surface plot file
        """

        #path to plots folder for different plots
        sss=ss+"/plots"
        #path to surface plot
        instance=File.objects.get(file=sss+"/surfacePlot.png")
        file_handle = instance.file.open()
        #print(file_handle)

        # send file
        response = FileResponse(file_handle, content_type='whatever')
        response['Content-Length'] = instance.file.size
        response['Content-Disposition'] = 'attachment; filename="%s"' % instance.file.name

        return response

class DeletePlotsView(APIView):

    """! The class that deletes the plot files.
    It queries the database for files in the plot folder with the provided session
    and deletes the files followed by the plot folder as well.
    """

     def delete(self, request, ss):

        """Deletes the plot files. Gets the plot files particular to that session (user) which are currently
        present in the backend inside the plots folder within the current session
        folder and then deletes the files unless some error is thrown and thereafter
        also deletes the plots folder corresponding to that particular session.

        @param self reference to the current instance of the class
        @param request passes the state through the system
        @param ss refers to the current session of the user
        @return response with status 200 if successful deletion,
                 else response with 404 if file not found
        """

        #path to plots folder for different plots
        sss = ss+"/plots"
        try:
            files = File.objects.filter(session=sss)
            for fl in files:
            	#deleting the plots
                fl.file.delete()
                fl.delete()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            path = os.path.join(settings.MEDIA_ROOT, sss)
            #deleting the plots folder
            os.rmdir(path)
        except:
            pass
        return Response(status=status.HTTP_200_OK)
