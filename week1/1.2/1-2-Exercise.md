1.2 Project
===========
Spamlord
-----------
### Harvesting emails and phone numbers

Here's your chance to be a SpamLord! Yes, you too can build regexes to help spread evil throughout the galaxy!

More specifically, your goal in this assignment is to write regular expressions that extract phone numbers and regular expressions that extract email addresses.

To start with a trivial example, given

    alessandro@galvanize.com
    
your job is to return

    alessandro@galvanize.com
    
But you also need to deal with more complex examples created by people trying to shield their addresses, such as the following types of examples that I'm sure you've all seen:

    alessandro(at)galvanize.com
    alessandro at galvanize dot com

You should even handle examples that look like the following:

    <script type="text/javascript">obfuscate('galvanize.com','alessandro')</script> 

For all of the above you should return the corresponding email address

    alessandro@galvanize.com

as appropriate.  
Similarly, for phone numbers, you need to handle examples like the following:

    TEL +1-415-805-1888
    Phone:  (415) 805-1888
    Tel (+1): 415-805-1888
    <a href="contact.html">TEL</a> +1&thinsp;415&thinsp;805&thinsp;1888

all of which should return the following canonical form:

    415-805-1888

(you can assume all phone numbers we give you will be inside North America).  
In order to make it easier for you to do this, we will be giving you some data to test your code on, what is technically called a *development test set*. This is a document with some emails and phone numbers, together with the correct answers, so that you can make sure your code extracts all and only the right information. However, because you want to be sure your code *generalizes* well, you should be creative in looking at the web and thinking of different types of ways of encoding emails and phone numbers, and not just rely on the methods we've listed here.

**You won't have to deal with:** really difficult examples like images of any kind, or examples that require parsing names into first/last like:

    "first name"@galvanize.com

or difficult examples like:

    To send me email, try the simplest address that makes sense.

#### Where can I find the starter code?

You will find starter code in the github repository.  
By default, if you execute:

    $ python SpamLord.py ../data/dev/ ../data/devGOLD

It will run your code on the files contained in data/dev/ and compare the results of a simple regular expression against the correct results. The results will look something like this:

    True Positives (4): 
    set([('balaji', 'e', 'balaji@stanford.edu'),
         ('nass', 'e', 'nass@stanford.edu'),
         ('shoham', 'e', 'shoham@stanford.edu'),
         ('thm', 'e', 'pkrokel@stanford.edu')])
    False Positives (1): 
    set([('psyoung', 'e', 'young@stanford.edu')])
    False Negatives (113): 
    set([('ashishg', 'e', 'ashishg@stanford.edu'),
         ('ashishg', 'e', 'rozm@stanford.edu'),
         ('ashishg', 'p', '650-723-1614'),
    ...

The true positive section displays e-mails and phone numbers which the starter code correctly matches, the false positive section displays e-mails which the starter code regular expressions match but which are not correct, and the false negative section displays e-mails and phone numbers which the starter code did not match, but which do exist in the html files. Your goal, then, is to reduce the number of false positives and negatives to zero. 

#### Where should I write my Python code?
The function
```python
def process_file(name, f):
```
has been flagged for you with the universal "TODO" marker. This function takes in a file object (or any iterable of strings) and returns a list of tuples representing e-mails or phone numbers found in that file. Specifically the tuple has the format:

    (filename, type, value)

where type is either 'e', for e-mail, or 'p' for phone number, and value is just the actual e-mail or phone number.

#### What format should the my phone numbers and e-mail have?

The canonical forms expected are:

    user@example.com
    415-555-1234

The case of the e-mails you find should not matter because the starter code will lowercase your matched e-mails before comparing them against the gold set