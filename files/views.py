from .models import InputFile
from .serializers import InputFileSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ml_model import signals


@api_view(['GET', 'POST'])
def files_list(request):

    if request.method == 'GET':
        content = {'title': 'working'}
        return Response(content)

    elif request.method == 'POST':
        serializer = InputFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            file_name = serializer.data['input_name']
            inputfile = InputFile.objects.filter(input_name = file_name).first()
            input_file = inputfile.input_file.url
            input_file = input_file[1:]
            summarised = signals.summarize(input_file, 4)

            return Response(summarised, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
