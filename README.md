# Given Challenge:
## Introduction and expectations

Hi there! Please complete the problem described below to the best of
your ability, using the tools you're most comfortable with. Assume
that you're sending your submission in for code review from peers;
we'll be talking about your submission in your interview in that
context.

We expect this to take less than 4 hours of actual coding time; please
consider submitting a working but incomplete solution instead of
spending more time on it. We're also aware that getting after-hours
coding time can be challenging; we'd like a submission within a week
and if you need more time please let us know.

## The problem: CSV normalization

Please write a tool that reads a CSV formatted file on `stdin` and
emits a normalized CSV formatted file on `stdout`. Normalized, in this
case, means:

* The entire CSV is in the UTF-8 character set.
* The Timestamp column should be formatted in ISO-8601 format.
* The Timestamp column should be assumed to be in US/Pacific time;
  please convert it to US/Eastern.
* All ZIP codes should be formatted as 5 digits. If there are less
  than 5 digits, assume 0 as the prefix.
* All name columns should be converted to uppercase. There will be
  non-English names.
* The Address column should be passed through as is, except for
  Unicode validation. Please note that there are commas in the Address
  field, your CSV parsing will need to take that into account.
* The columns `FooDuration` and `BarDuration` are in HH:MM:SS.MS
  format; please convert them to a floating point seconds format.
* The column "TotalDuration" is filled with garbage data. For each
  row, please replace the value of TotalDuration with the sum of
  FooDuration and BarDuration.
* The column "Notes" is free form text input by end-users; please do
  not perform any transformations on this column. If there are invalid
  UTF-8 characters, please replace them with the Unicode Replacement
  Character.

You can assume that the input document is in UTF-8 and that any times
that are missing timezone information are in US/Pacific. If a
character is invalid, please replace it with the Unicode Replacement
Character. If that replacement makes data invalid (for example,
because it turns a date field into something unparseable), print a
warning to `stderr` and drop the row from your output.

You can assume that the sample data we provide will contain all date
and time format variants you will need to handle.


# My Comments: 

## Running my script:
I've written a simple script that basically just runs in the terminal. I used Python 3.6.2 while building this project and worked on a mac. 

If you have python 3 installed, you should be able to run 
```
python3 app.py
```
 from within this folder. (Or whatever you have as your normal command to run a python 3 project.)

## Assumtions I am making:
1. The columns will always be in the same order
1. This is not expected to be a final product! 

## Notes / Other Comments:
I have several TODO items listed in my code of things I wanted to go back to if I had the time, but I wanted to stay within the requested 4 hour window. Some of these items included asking for clarification which I normally would have done at the beginning when reading over the project requirements. (Or at least as soon as they occured to me, but I was working over the weekend and didn't want to wait for a response)

I've spent most of my time recently using JavaScript and the context switch to Python (which I am not as strong with) slowed me down more than I had expected. I chose Python over JavaScript because Python seemed likely to be the better tool for this job. 

## With more time:
* Address all the items I listed as TODO in the code
* Clean up the code (apply DRY concepts where I could)
* Keep looking (or ask other programmers) for better solutions. There were a few places where I know there has to be a better solution, but I didn't have enough time to get too lost in Google/Stack Overflow.