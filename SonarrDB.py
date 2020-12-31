import sqlite3

sqlfile = sqlite3.connect("nzbdrone.db")
#* Choose the route to your new media path in the linux machine *#
newRoute = '/media/'
# if your pathing is different change the if statements
# Edits RootFolder Path
def RootF ():
    cursor = sqlfile.cursor()
    cursor.execute("SELECT * FROM RootFolders")
    data = cursor.fetchall()
    for row in data:
        if row[1][:4] != '/med': #! Change if your new path isn't /media
            directories = row[1][3:].strip('\\')
            newPath = newRoute + directories
            oldPath = row[1]
            print(newPath)
            cursor.execute('UPDATE RootFolders SET Path = ? WHERE Path = ?', (newPath, oldPath))
            sqlfile.commit()

# Edits series Path
def Series():
    cursor = sqlfile.cursor()
    cursor.execute("SELECT Path FROM Series")
    data = cursor.fetchall()
    for row in data:
        if row[0][:4] != '/med': #! Change if your new path isn't /media
            #print(row)
            directory, filename = row[0][3:].split("\\")
            directory = directory.replace("shows", "Shows")
            newPath = newRoute + directory + "/" +  filename
            oldPath = row[0]
            print(newPath)
            cursor.execute('UPDATE Series SET Path = ? WHERE Path = ?', (newPath, oldPath))
            sqlfile.commit()

# Edits EpisodeFiles RelativePath
def EpisodeFiles():
    cursor = sqlfile.cursor()
    cursor.execute("SELECT RelativePath FROM EpisodeFiles")
    data = cursor.fetchall()
    for row in data:
        newPath = row[0].replace("\\","/")
        oldPath = row[0]
        if "\\" in oldPath:
            cursor.execute('UPDATE EpisodeFiles SET RelativePath = ? WHERE RelativePath = ?', (newPath, oldPath))
        print(newPath)
    sqlfile.commit()

# Edits ExtraFiles RelativePath
def ExtraFiles():
    cursor = sqlfile.cursor()
    cursor.execute("SELECT RelativePath FROM ExtraFiles")
    data = cursor.fetchall()
    for row in data:
        newPath = row[0].replace("\\","/")
        oldPath = row[0]
        if "\\" in oldPath:
            cursor.execute('UPDATE ExtraFiles SET RelativePath = ? WHERE RelativePath = ?', (newPath, oldPath))
        print(newPath)
    sqlfile.commit()

# Edits SubtitleFiles RelativePath
def SubtitleFiles():
    cursor = sqlfile.cursor()
    cursor.execute("SELECT RelativePath FROM SubtitleFiles")
    data = cursor.fetchall()
    for row in data:
        newPath = row[0].replace("\\","/")
        oldPath = row[0]
        if "\\" in oldPath:
            cursor.execute('UPDATE SubtitleFiles SET RelativePath = ? WHERE RelativePath = ?', (newPath, oldPath))
        print(newPath)
    sqlfile.commit()

RootF()
Series()
EpisodeFiles()
ExtraFiles()
SubtitleFiles()