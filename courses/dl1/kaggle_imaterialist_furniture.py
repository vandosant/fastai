import urllib.request
import urllib.error
import shutil
import ssl

def save_remote_image(url, file_path):
    try:
        with urllib.request.urlopen(url, timeout=4) as response, open(file_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    except (urllib.error.HTTPError, urllib.error.URLError, ssl.CertificateError) as error:
        print(f'failed to get {file_path}')