# General rules

## Questions
### Split
#### Problem
Write a *function* called split which will take two iterables as
input - One called `items` and another called `ratios`. It should
return an iterable of iterables which contains random elements from
`items` in the proportions as indicated in `ratios`. You should
round up or down to make sure all elements are there in the return
value.
   
e.g. The following invocation will split `[1,2,3,4,5,6,7,8,9,10]`
into 3 lists. The first one will have 5 random elements (50%), the
next will have 4 (40%)  and the last will have 1 (10%).

      split([1,2,3,4,5,6,7,8,9,10], [0.5, 0.4, 0.1])
     
will return something like 

       [[4,2,3,9,10], [1,5,6,8], [7]]
       
If instead, we called it like this

        split([1,2,3,4,5,6,7,8,9,10], [0.25, 0.5, 0.25])

will return something like

          [[2,3,5], [1,4,6,7,9], [8,10]]

Notice that the 0.25 entries have different values to accommodate
all the elements. 
#### Rules
1. Please don't use any 3rd party libraries to do this. No pandas,
   numpy etc. 
2. Make sure your code is well structured and easy to read. Good
   variable names, proper functions etc will go a long way.
3. Include unit tests for your submission
    
    
### Crawler
#### Problem
Write a program called `crawler.py` to scrape the website `https://www.gettyimages.in/photos/aamir-khan-actor` and download all *60* images of the actor. 

* Each image will have a URL like this `https://media.gettyimages.com/photos/indian-actor-amir-khan-1988-picture-id499342585?k=6&m=499342585&s=612x612&w=0&h=4jP2Zn9qP_R5kN8NpOwTTCDBO2SEVeqfZDcF0VebaKw=`. This what you need to download. They will be linked to a larger image like `https://media.gettyimages.com/photos/indian-actor-amir-khan-1988-picture-id499342585?s=2048x2048`. You don't need to download that. Only the smaller former one. 
* After you download an image, save it in a directory called `images`. The filename has to be created from the input URL using the pathname. E.g. if the URL from which you downloaded is `https://media.gettyimages.com/photos/indian-actor-amir-khan-1988-picture-id499342585?k=6&m=499342585&s=612x612&w=0&h=4jP2Zn9qP_R5kN8NpOwTTCDBO2SEVeqfZDcF0VebaKw=` the filename will be called `indian-actor-amir-khan-1988-picture-id499342585.jpg`. This is the pathname of the URL without the `/photos` prefix. 
* At the end of the operation, you will have a directory called `images` that contains 60 images of the actor with the correct names and checksums.

Click on the following image to see an ascii screencast of how this will work.

[![asciicast](https://asciinema.org/a/4CcU1jXDzKwILhFlbF07fH6NT.svg)](https://asciinema.org/a/4CcU1jXDzKwILhFlbF07fH6NT)

#### Rules
    1. Use whatever libraries you need for this. But please provide a
       proper `requirements.txt` and a `setup.py` file. 

### Statistics
#### Problem
The attached file called `unemployment-rate.csv` contains a list of
employment ratios for various countries for various years. Each entry
looks like this


        Belgium,BEL,2010,8.28999996185303
        
Where Belgium is the country, BEL is the symbol for the country. 2018
is the year and 8.28999996185303 is the unemployment ratio.

Write a command line program called `statistics.py` which should
accept an input file and the following command line parameters


        --country COUNTRY  Country to perform operation for
        -o {avg,min,max}   Operation to perform on dates. (Default avg)
        --from FROM_       Starting year (inclusive)
        --to TO            Ending year (inclusive)

It should then parse the input file and filter the output as per the
provided parameters and display. 

The `--country` parameter is compulsory and will narrow the statistics
to  only entries  for  that  country. It  accepts  country names  (not
symbols)

The `-o` option will take the operation to perform. It can be either
`min` for minimum, `max` for maximum or `avg` for average. It will
perform this operation on the unemployment rates for that
country. This is not compulsory. The default (when nothing is provided
is avg).

`--from` and `--to` are optional and used to restrict the operations
to a date range. e.g. if you run it with `--from=1999`, it will only
consider the lines with the year greater than or equal to
`1999`. Similarly, `--to=2000` will only consider lines less with the
year than or equal to `2000`. 

The output will simply print the requested statistic.

Click on the following image to see an ascii screencast of how this will work.
[![asciicast](https://asciinema.org/a/QJghGKUY4v7CBDzC2biH9bXL7.svg)](https://asciinema.org/a/QJghGKUY4v7CBDzC2biH9bXL7)

#### Rules
1. Don't use anything except the standard library to do this. No
   pandas, numpy etc.
2. Make sure that the code is modular and has separate functions to do
   various tasks
3. Unit tests are compulsory. Please include them.
4. Use an argument parsing library to handle the command line parsing



## Evaluation criteria
1. Modular code. We expect you to write proper functions for each task
   and then put them together rather than one single program
2. We expect a proper `requirements.txt` file and a `setup.py` file so
   that the program can be installed and used
3. (optional) If you include a test suite, you will be awarded extra
   points
4. Good code style - Proper variable names, no misspellings, adherence
   to Python common coding standards will all be considered.
5. Please version control your development and send us a git
   repository with your code. It's important that we see the process
   of development so please don't just upload everything in a single
   shot. 
