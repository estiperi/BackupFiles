# BackupFiles
Python script that backs up a folder, either with files or folders inside.

### Input:
- Folder to back up (the _origin_ folder).
- Folder in which the backup will be made (the _destination_ folder).


### Process:
The script loops through all files and subfolders in the _origin_ folder. For each one, it creates a copy in an analogous location inside the _destination_ folder.
If a file is directly located in the _origin_ folder, its copy will be created in the _destination_ folder. In a file is inside a subfolder of the _origin_ folder, the backup file will be created in a similar subfolder of the _destination_.
Examples:

Origin: C:/Folder_level_1
Destination: H:/Backup_of_C

File C:/Folder_level_1/example1.txt -> H:/Backup_of_C/example1.txt
File C:/Folder_level_1/Folder_level_2/example2.txt -> H:/Backup_of_C/Folder_level_2/example2.txt
File C:/Folder_level_1/Folder_level_2/Folder_level_3/example9.txt -> H:/Backup_of_C/Folder_level_2/Folder_level_3/example9.txt


### Output:
- A .txt file with the list of files processed by the script and the outcome: backed-up (copied from _origin_ to _destination_) or not.
