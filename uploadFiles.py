import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BK93otzltU916kENDGvbob6e5qTwyI-Jp0BGUW13P8v0yNyCx3EJLAhGJ6URrTAsJtFxxkGZo5elTG3pFaOA6IjQ9zaaKY3TaFfycfk6wj8pzwRfGPu8i954M3ll_wiyNrIEN0p2zqLc'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  

    
    transferData.upload_file(file_from, file_to)


    main()