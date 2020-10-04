import uuid
import os


def handle_uploaded_file(f):
    try:
        os.mkdir('media')
    except:
        pass
    
    with open("media/" + f.name , 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    my_file_path = "media/" + f.name
    print("my_file_path :", my_file_path)

    # process_image(my_file_path)
    # url = my_upload(my_file_path)
    # print("AWS Url : ", url)
    # return url