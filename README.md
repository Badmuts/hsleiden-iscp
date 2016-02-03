# ISCP
Real basic Python Twitter sentiment analysis. It uses the Twitter streaming API to retrieve tweets and uses a real basic analyser (written by me) to analyse the tweets.

It visualises the analysis to a webpage served via Flask which automatically updates every 300ms (DDOS incoming).

![Webpage](https://www.dropbox.com/s/rvhsl7nf9audfy5/Screen%20Shot%202016-01-29%20at%2022.29.57.png?dl=1)

# Installation
Install the requirments using pip
```
$ pip install -r requirments.txt
```
Create a config.json file in the `src` folder:
```
{
	"consumer_key": "YOUR CONSUMER KEY",
	"consumer_secret": "YOUR CONSUMER SECRET",
	"access_token": "YOUR ACCESS TOKEN",
	"access_token_secret": "YOUR ACCESS TOKEN SECRET"
}
```
Run the app from the `src` folder and serve to `127.0.0.1:5000`
```
$ python app.py
```

Start analyzing some tweets :D
