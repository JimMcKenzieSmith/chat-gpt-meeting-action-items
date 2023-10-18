# Chat GPT-4 Meeting Notes and Action Items Generator

In our virtually connected world, we use video meetings more than ever.  And these meetings often have automated transcripts running that have a record of what everyone said in the meeting in text format.  What if we could take this text based meeting transcript, run it throught Chat GPT, and get back a meeting summary with meeting action items?  This repo sets out to show how to do with with a simple Python based API.

## How It Works

A sample meeting transcript file is provided in the data folder, and this gets loaded by the app and passed to Chat GPT.  A system prompt and a user prompt is leveraged to generate a meeting summary, action items, and topics for discussion next meeting.

## Installation

Requires Python 3.8 or newer.

Create an [openai account](https://platform.openai.com/) if you do not already have one.

Obtain an API key from the [api keys](https://platform.openai.com/account/api-keys) account page, and seed your account with money to make requests. 
As of 10/18/2023 you could seed your account with as little as $10 to get started.

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required packages from requirements.txt.

```bash
pip install -r requirements.txt
```

Set your api key in your .zshrc file if using a Mac.

```bash
export CHATGPT_API_KEY=your-api-key-from-your-openai-account
```

## Usage

Start the development server:

```bash
python main.py
```

Example curl POST request for a meeting transcript file that resides on your computer:

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"file_loc":"data/meeting-ctas-county-commission.txt"}' \
  http://localhost:5000/api/meeting-summary
```


## Example Chat GPT Response for CTAS County Commission Meeting Transcript
```
Overall Summary of Discussion:
The CTAS County Commission meeting was held to discuss and vote on several key issues. The agenda was approved and the minutes from the last meeting were corrected to include Commissioner McCroskey's name. A resolution was passed to move money from the Data Processing Reserve Account to purchase a laptop. Commissioner McKee withdrew his motion to sell property near the airport. A motion to increase the state match local litigation tax was discussed, amended to allocate 25% of the proceeds from the tax increase on criminal cases to the sheriff's department, but ultimately failed to pass. A resolution to increase the wheel tax by $10 to compensate for state cuts in education funding was passed. Announcements were made about upcoming meetings and events.

Action Items:
1. Clerk to correct minutes to include Commissioner McCroskey's name in the Special Committee on Indigent Care.
2. Funds to be moved from the Data Processing Reserve Account to the equipment line for the purchase of a laptop.
3. Budget Committee to review solid waste funding recommendations on July 16.
4. Next CTAS County Commission meeting scheduled for August 19.

Topics for Next Meeting:
No specific topics were mentioned for the next meeting. However, given the contentious nature of the tax increase discussions, it is likely that further discussions on county revenue and budget allocations may be needed.
```

## Limitations

I quickly found that Chat GPT currently only supports a meeting transcript of about 185 lines of text maximum.  However, I'm certain that this technology will only get better and limitations such as this will be lifted.
