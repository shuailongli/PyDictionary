# PyDictionary
This program is running in the command line framework. Basic functions include text speaking, word lookup, English-to-Chinese sentence translation, Youtube audio play and download. Users can also add and save new words and sentences to the dictionary.

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

Initiated with command `speak` and followed by the text to speak. This command will play the audio of the English text.

**Syntax**
```
PyDict> speak any_text
```
