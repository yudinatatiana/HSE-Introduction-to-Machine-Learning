# Interfaces I

## Command-line and text interfaces

#### Exercise: Give two examples of asynchronous communication. Give two examples of synchronous communication.

Asynchronous communication: correspondence by e-mail, in social networks, messengers


Synchronous communication: video communication via zoom or skype, phone call

## Using a CLI

### Reading command specifications

#### Exercise: Compare the output of ls vs ls -l and ls -a; describe how they are similar, and how they are different.


"ls" - outputs only names of files and directories in the current directory.

```$ ls

'Decision trees'         accuracy-vs-max_depth.png   plot.png            svm-svm-perceptron.pdf
'Decision trees.ipynb'   data.csv                    practical_2.ipynb   testfile
 SVM.ipynb               data_after_task2.csv        project             testfile2```

"ls -l" - outputs detailed information about the files and directories in the current directory.

```$ ls -l
total 116
drwxr-xr-x 1 yudina yudina  4096 Jun 13 22:05 'Decision trees'
-rw-r--r-- 1 yudina yudina 25937 Jun 13 22:03 'Decision trees.ipynb'
-rw-r--r-- 1 yudina yudina 35452 Jun  7 14:18  SVM.ipynb
-rw-r--r-- 1 yudina yudina  8733 Jun 13 22:01  accuracy-vs-max_depth.png
-rw-r--r-- 1 yudina yudina   647 Jun 13 22:02  data.csv
-rw-r--r-- 1 yudina yudina   747 Jun 13 20:41  data_after_task2.csv
-rw-r--r-- 1 yudina yudina  8733 Jun 13 22:03  plot.png
-rw-r--r-- 1 yudina yudina  2755 Jun 17 14:22  practical_2.ipynb
drwxr-xr-x 1 yudina yudina  4096 Apr  2 20:52  project
-rw-r--r-- 1 yudina yudina 13601 Jun  7 14:14  svm-svm-perceptron.pdf
-rw-r--r-- 1 yudina yudina     4 Jun 17 13:46  testfile
-rw-r--r-- 1 yudina yudina     5 Jun 17 13:46  testfile2```

"ls -a" - outputs all the files and directories including those starting with .

```$ ls -a
 .                   'Decision trees'         accuracy-vs-max_depth.png   plot.png            svm-svm-perceptron.pdf
 ..                  'Decision trees.ipynb'   data.csv                    practical_2.ipynb   testfile
 .ipynb_checkpoints   SVM.ipynb               data_after_task2.csv        project             testfile2```

### Navigating with the command-line

#### Exercise: Explain pushd and popd; what data structure represents your directory history? Give an example of using them to organise a folder with music.

#### Exercise: Draw a partial tree of your filesystem, starting from the children of your home directory. Include ancestors of your home directory, and siblings of those ancestors. Exclude files, just show directories. Here is mine:

(root)/
    |
    | - bin/
    | - boot/
    | - dev/
    | - etc/
    | - home/
    |     | - yudina/
    |     |      | - audio_data/
    |     |      | - global-classroom/
    |     |      | - nltk_data/
    |     |      | - node_modules/
    |     |      | - others/
    |     |      | - work/
    |
    | - lib/
    | - lib64/
    | - media/
    | - mnt/
    | - opt/
    | - proc/
    | - root/
    | - run/
    | - sbin/
    | - snap/
    | - srv/
    | - tmp/
    | - usr/
    | - var/

## Shell scripting

#### Exercise: Write a shell script that asks the user for their name, and greets them. Sample interaction:

```
#!/bin/bash

while [[ $name = "" ]]
do
  echo -n "What's your name?"
  read name
done

echo "Hello, $name"
exit 0
```

```
$ sed -i $'s/\r$//' greeting
$ bash ./greeting
What's your name?
What's your name?Tanya
Hello, Tanya
```

#### Exercise: Write a shell script that performs "ROT13" (Caesar cipher with shift 13.) For English, encryption and decryption are the same! (Explain why!) Sample interaction:

#### Exercise: Write a shell function that prints "hidden" if the current directory starts with a dot ".", or if any parent starts with a dot. (Files and directories that start with dots are considered "hidden" on many UNIX-like systems.) Sample interaction:

```
#!/bin/bash

PWD=`pwd`
PATTERN='/.'

if [[ $PWD =~ $PATTERN ]]; then
	echo hidden
	exit 0
fi
exit 0
```
```
$ sed -i $'s/\r$//' hidden
$ bash ./hidden
$ mkdir .secretdir
$ cd ./.secretdir
$ bash ./hidden
hidden
```
