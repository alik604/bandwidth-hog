# Bandwidth-hog

> Download a file many times, but do not save the data. Useful for stressing out a network... possibly your own  

## Sample Usage 

Parameters: `python bandwidth-hog.py #ofThreads #ofTimesToDL urlAsAString ` 

```python
python bandwidth-hog.py 4 100 "https://www.E-corp.com/file/largeFile.rar"
```

## Suggested Integration

Integrate into a bot-net to organically ddos a network. This may require merging this proof-of-concept into a headless browser and configuring it to appear to be a popular end-user browser which will in-turn mask traffic as legitimate  

Interesting posts to neglect reading 

* stackoverflow.com/a/46929945
* duo.com/decipher/driving-headless-chrome-with-python

_Surely 10 hours in the lab will save you 1 hour in the library_

## Related projects
1. [CMPT 318: Cyber Security](https://github.com/alik604/Classes/tree/master/CMPT318)
    - [Presenation on Anomaly Detection](https://github.com/alik604/Classes/blob/master/CMPT318/CMPT_318_Presentation.pdf) 
2. [myPybackdoor](https://github.com/alik604/myPybackdoor)
    - Navigrate Directories 
    - Download, Create, and Delete Files
    - Execute custom CMD commands
    - Get wifi Password list
3. [chromePasswordThieve](https://github.com/alik604/chromePasswordThieve)
    - Grab passwords saved in chrome and email them out 
    - [Blog post](https://alik604.github.io/chromePasswordThieve/index.html)
    
## Sponsorship Notice 

I am pleased to announce that I am being sponsored by your local Internet Service Provider

## Legal Notice 

It’s safe to assume using this for the obvious purpose is illegal...  paying fines will “Make America Great Again” and bolster Donald Trump's retirement fund  
