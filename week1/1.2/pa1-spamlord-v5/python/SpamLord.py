import sys
import os
import regex as re
import pprint

pattern = r"[^//](\w+\.)?(\w+)(\s)?(at|@|&#x40;|WHERE){1}(\s)?(\w+)?(\s)?(\.|dot|;)?(\s)?(\w+)+(\s)?(\.|dot|dt|;|DOM)+(\s)?(edu|EDU|com{1})[^/|>| ]"
pattern2 = r"[^//](\w+)(@){1}(\s{1})?(\w+)?(\.)(\w+)(.edu)[\[^/| |>]"
pattern3 = r'(\w+.)?(\w+)?\s+(\(followed by &ldquo;|\(followed by ")(@)(\w+.?\w+)(.edu)'
pattern4 =  r"[^//](\w+)[\s](at)[\s](\w+)(\s)(\w+)(\s)(edu)[,][\[^/| |>]"
pattern5 = r"([\w-]+)(@)-([\w-]+).-([\w-]+\w)"
obfuscatepattern = r"(\w+\.edu)','(\w+)"
phone_pattern = r"\(?(\d{3})[\) -]+(\d{3})[ -]+(\d{4})"

def process_file(name, f):
    """This really should be refactored to bring the pattern matching into its own function"""
    """but I'm feeling lazy and this isn't production code so c'est le vie"""
    res = []
    for line in f:
        matches = re.findall(pattern,line)
        for m in matches:
            email = ''
            for x in m:
                if x.strip() != '':
                    if x == 'at' or x == '&#x40;' or x == 'WHERE':
                        email += '@'
                    elif x == 'dot' or x == 'dt' or x == ';' or x == 'DOM':
                        email += '.'
                    else:
                        email+= x
            res.append((name,'e',email))
        second_matches = re.findall(pattern2, line)
        for m in second_matches:
            email = ''
            for x in m:
                if x.strip() != '':
                    if x == 'at' or x == '&#x40;' or x == 'WHERE':
                        email += '@'
                    elif x == 'dot' or x == 'dt' or x == ';' or x == 'DOM':
                        email += '.'
                    else:
                        email+= x
#             print email
            res.append((name,'e',email))
        third_matches = re.findall(pattern3, line)
        for m in third_matches:
            email = ''
            for x in m:
                if x.strip() != '':
                    if x == '(followed by &ldquo;' or x == '(followed by "':
                        email += ''
                    elif x == 'dot' or x == 'dt' or x == ';' or x == 'DOM':
                        email += '.'
                    else:
                        email+= x
#             print m
#             print type(m)
            res.append((name,'e',email))
        fourth_matches = re.findall(obfuscatepattern, line)
        for m in fourth_matches:
                email = '{0}@{1}'.format(m[1],m[0])
#                 print email
                res.append((name,'e',email))
        matches4 = re.findall(pattern4,line)
        for m in matches4:
            email = ''
            for x in m:
            #      if x.strip() != '':
                 if x == 'at':
                     email += '@'
                 elif x == ' ':
                     email += '.'    
                 else:
                     email+= x
            #print type(email)
            res.append((name,'e',email))
        fifth_matches = re.findall(pattern5, line)
        email =''
        for m in fifth_matches:
            print m
            for q in m:
                email += q.replace('-','').replace('edu','.edu')
        if email != '':
            res.append((name,'e',email))
        phone_matches = re.findall(phone_pattern,line)
        for p in phone_matches:
#             print p
            phone = ''
            for z in p:
                if z != '(' and z != ')' and z != ' ' and z!= '-':
                    phone += z
#             print '{}-{}-{}'.format(phone[0:3],phone[3:6],phone[6:10])
            res.append((name,'p','{}-{}-{}'.format(phone[0:3],phone[3:6],phone[6:10])))
    return res

"""
You should not need to edit this function, nor should you alter
its interface as it will be called directly by the submit script
"""
def process_dir(data_path):
    # get candidates
    guess_list = []
    for fname in os.listdir(data_path):
        if fname[0] == '.':
            continue
        path = os.path.join(data_path,fname)
        f = open(path,'r')
        f_guesses = process_file(fname, f)
        guess_list.extend(f_guesses)
    return guess_list

"""
You should not need to edit this function.
Given a path to a tsv file of gold e-mails and phone numbers
this function returns a list of tuples of the canonical form:
(filename, type, value)
"""
def get_gold(gold_path):
    # get gold answers
    gold_list = []
    f_gold = open(gold_path,'r')
    for line in f_gold:
        gold_list.append(tuple(line.strip().split('\t')))
    return gold_list

"""
You should not need to edit this function.
Given a list of guessed contacts and gold contacts, this function
computes the intersection and set differences, to compute the true
positives, false positives and false negatives.  Importantly, it
converts all of the values to lower case before comparing
"""
def score(guess_list, gold_list):
    guess_list = [(fname, _type, value.lower()) for (fname, _type, value) in guess_list]
    gold_list = [(fname, _type, value.lower()) for (fname, _type, value) in gold_list]
    guess_set = set(guess_list)
    gold_set = set(gold_list)

    tp = guess_set.intersection(gold_set)
    fp = guess_set - gold_set
    fn = gold_set - guess_set

    pp = pprint.PrettyPrinter()
    #print 'Guesses (%d): ' % len(guess_set)
    #pp.pprint(guess_set)
    #print 'Gold (%d): ' % len(gold_set)
    #pp.pprint(gold_set)
    print 'True Positives (%d): ' % len(tp)
    pp.pprint(tp)
    print 'False Positives (%d): ' % len(fp)
    pp.pprint(fp)
    print 'False Negatives (%d): ' % len(fn)
    pp.pprint(fn)
    print 'Summary: tp=%d, fp=%d, fn=%d' % (len(tp),len(fp),len(fn))

"""
You should not need to edit this function.
It takes in the string path to the data directory and the
gold file
"""
def main(data_path, gold_path):
    guess_list = process_dir(data_path)
    gold_list =  get_gold(gold_path)
    score(guess_list, gold_list)

"""
commandline interface takes a directory name and gold file.
It then processes each file within that directory and extracts any
matching e-mails or phone numbers and compares them to the gold file
"""
if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print 'usage:\tSpamLord.py <data_dir> <gold_file>'
        sys.exit(0)
    main(sys.argv[1],sys.argv[2])
