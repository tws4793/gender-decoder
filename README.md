#genderdecoder

This is a python package for assessing gender-coded words in a job adverts.

It is a fork of the django app [gender-decoder.katmatfield.com](http://gender-decoder.katmatfield.com) / https://github.com/lovedaybrooke/gender-decoder developed by [Kat Matfield](http://www.katmatfield.com) and based the paper ["Evidence That Gendered Wording in Job Advertisements Exists and Sustains Gender Inequality"](http://gender-decoder.katmatfield.com/static/Gaucher-Friesen-Kay-JPSP-Gendered-Wording-in-Job-ads.pdf) by 
Danielle Gaucher and Justin Friesen and Aaron C. Kay.

##Install

```
pip install genderdecoder
```

##Usage

```
import genderdecoder

job_description = "Example job description text"
print job_description.assess(job_description)

```