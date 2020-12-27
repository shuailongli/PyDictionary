# PyDictionary
This program is running in the command line framework. Basic functions include text speaking, word lookup, English-to-Chinese sentence translation, Youtube audio play and download. Users can also add and save new words and sentences to the dictionary.

<h3>Prerequisite python libraries:</h3> 
<ul>
<li><a href="https://pypi.org/project/youtube_dl/" target="_blank">youtube_dl</a>
<li><a href="https://pypi.org/project/google-trans-new/" target="_blank">google_trans_new</a>
<li><a href="https://pypi.org/project/gTTS/" target="_blank">gtts</a>
<li><a href="https://pypi.org/project/SpeechRecognition/" target="_blank">speech_recognition</a>
</ul>

<h3>Setup</h3>
<ol>
  <li>Download the .zip file to local file_dir
  <li>Launch terminal, input and execute the following command lines

```
cd file_dir/PyDict
```
```
python PyDictionary.py
```
</ol>
<h3>Demos</h3>
<h4>Word Lookup and English-to Chinese Translation</h4>
#Word Lookup and English-to Chinese Translation

These two functions are initated with the command 'translate', followed by the word to look up or the English sentence to translate. If the followed content constains only one word, 'translate' will return the word definitions from 

[Google Dictionary-Chinese](https://gdictchinese.freecollocation.com)
