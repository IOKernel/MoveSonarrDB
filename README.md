# Purpose
Change the pathings of the Sonarr database hosted on a windows machine to a linux machine.  

# Usage
1. **Create a backup of your nzbdrone.db file**
2. Place your nzbdrone.db file in the same folder as the script
3. If your new linux pathing isn't /media/ change the script accordingly. [Check here](https://github.com/IOKernel/MoveSonarrDB/issues/1)
4. The script assumes that your folders on the windows machine is directly on the drive path, ex:  
    >C:\TV Shows  
    >C:\Movies  


## WARNING

This isn't supposed to be run blindly, I made the script quickly to move my database from windows to linux, and only posted this for anyone who is as lost as I was when I started this.