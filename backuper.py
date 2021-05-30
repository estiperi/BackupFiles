# -*- coding: utf-8 -*-
"""
Script that lists all files in the origin folder modified after a certain date
(origin folder = pathFolder; date = lastBackupTimestamp)
and copies them all into the destination folder
(pathDestFolder)
It creates a log file in a TXT which shows all files processed
and if they were copied or not.
"""

import os
import time
from shutil import copyfile
from datetime import datetime
 
pathFolder = r''
pathDestFolder = r''
lastBackupTimestamp = (YYYY, MM, DD, HH, MM, SS, 0, 0, 0)
fileModFrom = time.mktime(lastBackupTimestamp)
 
#Create TXT file for logging actions
now = datetime.now()
currDateTime = now.strftime("%Y_%d_%m_%H_%M_%S")
logFileName = 'Backup log ' + currDateTime + '.txt'
logFile = open(logFileName, 'a')
 
for fld, com, file in os.walk(pathFolder):
    for f in file:
        filePath = os.path.join(fld, f)
        fileMod = os.path.getmtime(filePath)
        if fileMod > fileModFrom:
            logFile.write(filePath)
            logFile.write('\n')
            #Generate new file path (destination)
            newFilePath = filePath.replace(pathFolder,pathDestFolder)
            logFile.write(newFilePath)
            logFile.write('\n')
            #Copy file to destination folder. Log result for each file.
            try:
                copyfile(filePath,newFilePath)
                logFile.write('File copied successfully.')
                logFile.write('\n\n')
            except:
                logFile.write('File not copied.')
                logFile.write('\n\n')
logFile.close()