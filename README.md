# PyDictionary
This program is running in the command line framework. Basic functions include text speaking, word lookup, English-to-Chinese sentence translation, Youtube audio play and download. Users can also add and save new words and sentences to the notebook.

<h2>Prerequisite python libraries:</h2> 
<ul>
<li><a href="https://pypi.org/project/youtube_dl/" target="_blank">youtube_dl</a>
<li><a href="https://pypi.org/project/google-trans-new/" target="_blank">google_trans_new</a>
<li><a href="https://pypi.org/project/gTTS/" target="_blank">gtts</a>
<li><a href="https://pypi.org/project/SpeechRecognition/" target="_blank">speech_recognition</a>
</ul>

<h2>Setup</h2>
<ol>
  <li>Download the .zip file to local file_dir
  <li>Launch terminal, input and execute the following command lines

```
cd file_dir/PyDict
```
```
python PyDictionary.py
```
If the code runs successfully, you'll enter a command line interface started with prompt `PyDict>`.

</ol>
<h2>Demos</h2>
<h3>Word Lookup and English-to Chinese Translation</h3>

These two functions are initated with the command `translate`, followed by the word to look up or the English sentence to translate. If the following content constains only one single word, `translate` will return the word definitions from [Google Dictionary-Chinese](https://gdictchinese.freecollocation.com), otherwise,  a Chinese translation from [Google Translate](https://translate.google.com) will be returned.

**Example**

```
PyDict> translate eminent

1. of people人famous and respected, especially in a particular profession（尤指在某专业中）卓越的，著名的，显赫的
   -an eminent architect著名的建筑师

2. of good qualities良好品质unusual; excellent非凡的；杰出的
   -a man of eminent good sense极其明智的人
```


```
PyDict> translate The abilities of modern neural networks are the result of the interactions of thousands of neurons (sometimes tens of thousands or more!).

现代神经网络的能力是成千上万个神经元（有时成千上万个或更多！）相互作用的结果。
```

<h3>Text Speaking</h3>

Started with command `speak` and followed by the text to speak. This command will play the audio of the following English text.

**Syntax**
```
PyDict> speak any_text
```

<h3>Save to Notebook</h3>
PyDictionary provides the basic setups to help study English vocabularies, sentences and listening materials by saving them to notebook. Three setups are implemented in three modes:

<ul>
<li><h4>vocabulary</h4>

Enter the vocabulary mode
 ```
PyDict> vocabulary
 ```
 Add a word to notebook
 ```
 PyDict> add
word: apple
meaning: a round fruit with shiny red or green skin and firm white flesh
example: an apple pie
---Added word: 
   * apple
   * a round fruit with shiny red or green skin and firm white flesh
   * an apple pie
```
After exectuting `add vocabulary` in the first line, a block for a word in notebook is created. A word block contains three entries: word, meaning and example. While the word entry is required to save a word block to notebook, the other two are optional.

Display all saved word blocks
```
---------------------
PyDict> all

   * apple
   * a round fruit with shiny red or green skin and firm white flesh
   * an apple pie
   * 0
---------------------
```
The integer in the fourth entry shows the number of times the word has been studied. When `all` is followed by a string, it will display all word blocks initiated by that string.

Users can also listen to the saved words by executing
```
PyDict> play apple
```

Remove a word from notebook
```
PyDict> remove apple
Are you sure to remove: 
   * apple
   * a round fruit with shiny red or green skin and firm white flesh
   * an apple pie
   * 0
(y/n): y
apple removed from notebook
```

<li><h4>sentence</h4>

Enter sentence mode
```
PyDict> sentence
```

This mode works similarly to the vocabulary mode: use `add` command to add a sentence to notebook, `all` to display, `play` to speak and `remove` to remove the sentence.

<li><h4>listening</h4>

Enter sentence mode
```
PyDict> listening
```
User can download and play interesting audios from Youtube videos in this mode. 

Add audio to notebook through the Yutube link
```
PyDict> add 
Youtube link: https://youtu.be/yIZ95TBD85c
name: US Surpasses 19 Million COVID-19 Cases Amid Fears Of Holiday Surge
[youtube] yIZ95TBD85c: Downloading webpage
[download] storage/ListeningAudio/yIZ95TBD85c.m4a has already been downloaded
[download] 100% of 1.69MiB
[ffmpeg] Correcting container in "storage/ListeningAudio/yIZ95TBD85c.m4a"
[ffmpeg] Destination: storage/ListeningAudio/yIZ95TBD85c.mp3
Deleting original file storage/ListeningAudio/yIZ95TBD85c.m4a (pass -k to keep)
---Added vieo
   * yIZ95TBD85c
   * US Surpasses 19 Million COVID-19 Cases Amid Fears Of Holiday Surge
   * https://youtu.be/yIZ95TBD85c
   * 1:49
```
The fist entry in the audio block displays the Yutube video ID. Note that all audios in notebook are referred through the Yutube ID. Similarly, users use `all` to list, `play` to play and `remove` to remove the audios.
</ul>
