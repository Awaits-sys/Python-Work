import zipfile
import shutil

"""fichier_zip = zipfile.ZipFile("fichier_zip", "w", zipfile.ZIP_DEFLATED)
fichier_zip.write("octobre.xlsx")
fichier_zip.write("novembre.xlsx")
fichier_zip.write("decembre.xlsx")
fichier_zip.close()"""

shutil.make_archive("filezip", "zip", "fichier_zipp")