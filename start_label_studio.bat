@echo off
set LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
set LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=C:\Users\Administrator\Desktop\code\coconut-annotations\storage

py update_paths.py
label-studio start -b -db "./label_studio.sqlite3"
