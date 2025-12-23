
# import os
# import json

# # Folders to exclude (full paths or startswith)
# EXCLUDE_PATHS = [
#     r"C:\Windows",
#     r"C:\System Volume Information",
#     r"C:\PerfLogs",
#     r"C:\inetpub"
# ]

# def is_excluded(path):
#     # Check if the path is or is inside any excluded folder
#     path = os.path.normpath(path).lower()
#     for excl in EXCLUDE_PATHS:
#         excl_norm = os.path.normpath(excl).lower()
#         if path == excl_norm or path.startswith(excl_norm + os.sep):
#             return True
#     return False

# def index_folders(drives):
#     folder_index = {}

#     for drive in drives:
#         if not os.path.exists(drive):
#             continue
#         for root, dirs, files in os.walk(drive):
#             # Skip excluded folders and all subfolders
#             if is_excluded(root):
#                 # Don't go deeper inside excluded folder
#                 dirs[:] = []
#                 continue

#             folder_index[root] = {
#                 "subfolders": dirs.copy(),
#                 "files": files.copy()
#             }

#     return folder_index

# if __name__ == "__main__":
#     drives_to_scan = ["C:\\", "D:\\", "E:\\"]  # Add drives as you want
#     folder_data = index_folders(drives_to_scan)

#     with open("folder_index.json", "w") as f:
#         json.dump(folder_data, f, indent=2)

#     print("Folder index saved to folder_index.json")

