# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 14:53:05 2021

@author: amjph

fast downloader, just configure it once and save youtube videos fast
"""

# In a version to share, ask the folders where to organize
# Name the folder, what do you want to save in it (videos, audios, duration, manually), Add another folder inside it? Yes --> continue infinite, No ---> Back to the folder before and ask the same question


# Define the folders and for what its the folder

from pytube import YouTube

link = input("Video link: ") # Ask the video link
yt = YouTube(link)           # Get every video data
downloads = 0                # Count the consecutive downloads

"""
PUT YOUR MAIN FOLDER HERE
"""
folder = "D:\EditFiles"      # Define the MAIN folder to save the videos


tempfolder = ""
multiDownload = "y"

def orderList(l):
    """
    Parameters
    ----------
    l : TYPE: Array
        DESCRIPTION: Print element by element in different liens

    Returns
    -------
    None.
    """
    
    n = l.count()            # N saves the number of elements into the array
    i = 0                    #Count how many elements you alredy print it
    while i < n:
        print(l[i])
        i += 1

while True:
    
    # Ask to download again
    if downloads > 0:       # If you alredy download another video ask if you wanna download other or just close
        while True: 
            multiDownload = input("¿Do you wanna download another video? y/n: ")
            if multiDownload == "y":
                link = input("Put the link here: ")
                break
            elif multiDownload == "n":
                break
            else:
                while multiDownload != "y" and multiDownload != "n":
                    multiDownload = str(input("Enter a valid parameter (y/n): "))
                    print(multiDownload)
                break

    
    ### PRINT THE VIDEO DETAILS ###
    yt = YouTube(link)
    #Title of video
    print("Title: ", yt.title)
    #Number of views of video
    print("Number of views: ",yt.views)
    #Length of the video
    print("Length of video: ",yt.length,"seconds")
    #Description of video
    print("Description: ",yt.description[1:101], "...")
    #Tumbail link
    print("Tumbail link: ", yt.thumbnail_url)
    
    while multiDownload == "y":

                
        ### Ask if its a video or sound and show the quality options ###
        ans = (input("Do you want the Video, or Sound? ")).lower() 
        while True:
            if ans == "sound":
                stream = yt.streams.filter(only_audio=True)
                orderList(stream)
                break
            elif ans == "video":
                stream = yt.streams.filter(file_extension='mp4')
                orderList(stream)
                break
            else:
                ans = input("Invalid format, write 'video' or 'sound': ")
        tag = int(input("Quality tag number: ")) # Select the tag of the filetype you wanna download
        
        if downloads > 0: # If you download something before ask if you wanna use the same config 
            print(downloads)
            repeat = (input("Do you wanna repeat the last folder config? Y/N: ")).lower()
            if repeat == "y":
                folder = tempfolder
                print("////////////Loop brake to repeat the last config///////////////") #DEBUG
                break
            else:
                folder = "D:\EditFiles" 
        ### Select the exact folder where you wanna save the video ###
        
        """
        put your folders here
        """
        
        if ans == "video":
            ans = (input("Its a Meme, a GreenScreen or other. ")).lower()
            while True:
                if ans == "meme":
                    folder += "\Memes"
                    break
                elif ans == "greenscreen":
                    folder += "\GreenScreens"
                    break
                elif ans == "other":
                    folder += "\OtherVideos"
                    break
                else:
                    ans = (input("Invalid ans, pls wirte MEME/GREENSCREEN/OTHER: ")).lower()
            break
        elif ans == "sound":
            ans = (input("Its a SFX, Music or other. ")).lower()
            while True:
                if ans == "sfx":
                    folder += "\SFX"
                    break
                elif ans == "music":
                    folder += "\Music"
                    ans = (input("Its a 8bits, EPIC, OSTs, Meme or other. ")).lower()
                    while True:
                        if ans == "8bits":
                            folder += "\8bits"
                            break
                        elif ans == "epic": 
                            folder += "\EPIC"
                            break
                        elif ans == "osts": 
                            folder += "\OSTs"
                            break
                        elif ans == "other": 
                            folder += "\others"
                            break
                        elif ans == "meme":
                            folder += "\Meme"
                            break
                        else:
                            (input("Invalid value, pls write 8bits/EPIC/OSTs/OTHER ")).lower()
                    break
                elif ans == "other":
                    folder += "\OtherSounds"
                    break
                else:
                    ans = (input("Invalid ans, pls wirte SFX/MUSIC/OTHER: ")).lower()
            break


    tempfolder = folder                             # Save the last options
    stream = yt.streams.get_by_itag(tag)            # Get the video data
    stream.download(output_path=(folder))           # Download the video
    print("Your video was saved in " + folder)      # Print where the video was downloaded
    downloads = downloads+1                         # Add 1 download 
print("Goodbye")                                # Say "Goodbye" when the program close