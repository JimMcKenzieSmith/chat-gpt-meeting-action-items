# Chat GPT-4 Meeting Notes and Action Items Generator

In our virtually connected world, we use video meetings more than ever.  And these meetings often have automated transcripts running that have a record of what everyone said in the meeting in text format.  What if we could take this text based meeting transcript, run it throught Chat GPT, and get back a meeting summary with meeting action items?  This repo sets out to show how to do with with a simple Python based API.

## How It Works

Sample meeting transcript files are provided in the data folder, and these get loaded into a Pandas dataframe by the app.

## Installation

Requires Python 3.8 or newer.

Create an [openai account](https://platform.openai.com/) if you do not already have one.

Obtain an API key from the [api keys](https://platform.openai.com/account/api-keys) account page, and seed your account with money to make requests. 
As of 10/18/2023 you could seed your account with as little as $10 to get started.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages from requirements.txt.

