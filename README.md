#genderdecoder

A python package for assessing the number of gender-coded in a job advert.

It is a fork of the django app [gender-decoder.katmatfield.com](http://gender-decoder.katmatfield.com) / https://github.com/lovedaybrooke/gender-decoder developed by [Kat Matfield](http://www.katmatfield.com).

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