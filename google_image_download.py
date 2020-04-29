from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

for i in range(len(topics)):
    arguments = {"keywords":"topics[i]","limit":20,"print_urls":True}   #creating list of arguments
    paths = response.download(arguments)   #passing the arguments to the function
    print(paths)
