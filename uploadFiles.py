import os
import dropbox
from dropbox.files import WriteMode
from pathlib import Path

class TransferData(object):
    def __init__(self, token):
        self.token = token

    def upload(self, folder_from, folder_to):
        print("\nUploading Files...")
        dbx = dropbox.Dropbox(self.token)

        for root, dirs, files in os.walk(folder_from):
            for file in files:
                path = os.path.join(root, file)
                relative_path = os.path.relpath(path, folder_from)
                dropbox_path = os.path.join(folder_to, relative_path)

                f = open(path, 'rb')
                dbx.files_upload(f.read(), dropbox_path)
        print("Done!")

token = "9ZrsVeEYO-IAAAAAAAAAAYARCB55xMvP5wZlZDHAtf0HLnP4QjrpQtXxVV9lK5I9"
transferData = TransferData(token)

folder_from = input("Enter folder path to upload: ")
folder_to = input("Enter the full path in dropbox to upload: ")
    
transferData.upload(folder_from, folder_to)
