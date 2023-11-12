import os, shutil

downloadPath = r"C:\Users\justa\Downloads"
documentPath = r"c:\Users\justa\Documents"
imagePath = r"c:\Users\justa\Pictures"
videoPath = r"c:\Users\justa\Videos"
othersPath = r"c:\Users\justa\Miscellaneous"

image_file_types = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".bmp",
    ".tiff",
    ".webp",
    ".svg",
    ".ico",
    ".jfif",
    ".exif",
    ".raw",
    ".heif",
    ".bat",
    ".bpg",
    ".indd",
    ".ai",
    ".eps",
    ".psd",
)
document_file_types = (
    ".doc",
    ".docx",
    ".txt",
    ".pdf",
    ".rtf",
    ".odt",
    ".ods",
    ".odp",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".csv",
    ".md",
    ".html",
    ".xml",
    ".json",
)
video_file_types = (
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".wmv",
    ".flv",
    ".webm",
    ".mpeg",
    ".mpg",
    ".3gp",
    ".ogv",
    ".m4v",
    ".divx",
    ".vob",
    ".qt",
    ".rm",
    ".rmvb",
    ".asf",
    ".ts",
    ".m2ts",
    ".mxf",
)


def findFileType(extension):
    if extension in image_file_types:
        return imagePath
    elif extension in document_file_types:
        return documentPath
    elif extension in video_file_types:
        return videoPath
    return othersPath


for i in os.listdir(downloadPath):
    currentItemLocation = downloadPath + "\\" + i
    fileExtension = os.path.splitext(i)
    correctLocation = findFileType(fileExtension[1])
    if not correctLocation:
        continue
    correctLocation += "\\" + i
    if os.path.isfile(currentItemLocation):
        shutil.move(currentItemLocation, correctLocation)
    elif os.path.isdir(currentItemLocation):
        shutil.move(currentItemLocation, correctLocation + "\\" + i)
    else:
        shutil.move(currentItemLocation, correctLocation + "\\" + i)
        print(
            i,
            "Unknown File Type => Moving to Miscellaneous",
        )
