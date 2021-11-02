# Python-OS-Delete-Automation

In this code our main aim is to delete SRT files which are present in folders and sub-folders.

1) The first line is self-explanatory, where we're importing OS Module of Python.
2) In the second line we're feeding the path where we want to do the delete operation.
3) In the next line we're iterating file by file using for loop and os.listdir() function.
4) Next, we're joining the path to the sub-sequent sub-folders and storing it into the variable called path2. 
5) Then we're changing the directory to the path which we created in the last step using in-built function called os.chdir().
6) As usual what we did in the second step, we're re-iterating file by file using for loop and os.listdir() function.
7) Now here's the small logic of this program where we're checking whether the file is SRT file or not using if condition.
8) Usually, file name ends with file type like .jpg, .mp3, etc. Here we're checking for the file ends with .srt because subtitle files end with .srt.
9) Logic goes like this, if the last 3 characters of file name ends with srt then delete the file using os.remove() function

After running the above program, our directory will be free of all srt files, this program is not only limited to do this kind of task, we can use this technique to various kinds of files and other operations.

I just wanted to share this tip, because why we've to do everything manually when we've python? Happy Coding :)
