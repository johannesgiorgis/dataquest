# Project: Transforming data with Python

Below are the notes and steps taken for this project.

## Introduction

In this project, we will be working with a dataset of submissions to Hacker News from 2006 to 2015. [Hacker News](http://news.ycombinator.com/) is a site where users can submit articles from across the internet (usually about technology and startups), and others can "upvote" the articles, signifying that they like them. The more upvotes a submission gets, the more popular it was in the community. Popular articles get to the "front page" of Hacker News, where they're more likely to be seen by others.

The dataset you'll be using was compiled by Arnaud Drizard using the Hacker News API, and can be found [here](https://github.com/arnauddri/hn). We've sampled `10000` rows from the data randomly, and removed all extraneous columns. Our dataset only has four columns:

- `submission_time` -- when the story was submitted.
- `upvotes` -- number of upvotes the submission got.
- `url` -- the base domain of the submission.
- `headline` -- the headline of the submission. Users can edit this, and it doesn't have to match the headline of the original article.

We will be writing scripts to answer some main questions:

- What words appear most often in the headlines?
- What domains were submitted most often to Hacker News?
- At what times are the most articles submitted?


## Exploring domains

Let's explore which domains were submitted most often.

We can extend this analysis and make it a bit more robust by removing subdomains. For example, `blog.iweb.com` and `iweb.com` would be separate domains at the moment, but they are the same. By removing the subdomain, we can turn `blog.iweb.com` into `iweb.com`. We can remove the subdomain using the `Series.apply` and `Dataframe.apply` methods in pandas.


## Exploring Articles Submission times

We want to know when the most articles are submitted. One easy way to reframe this is to look at what hour articles are submitted. To figure this out, we'll need to use the `submission_time` column.

The `submission_time` column contains timestamps, which look like this: `2011-11-09T21:56:22Z`. These times are expressed in [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).

To get hour from a timestamp, we can use the `dateutil` library. The `parser` module in `dateutil` contains the `parse` function, which can take in a timestamp, and return a _datetime_ object. [Here's](https://dateutil.readthedocs.org/en/latest/parser.html) a link to the documentation. After parsing the timestamp, the `hour` property of the resulting date object will tell us the hour the article was submitted.

We can repeat this procedure to find how many articles were submitted on each day of the month, year, minute, day of the week, and so on.


## Next Steps

Some questions to explore next:

- What headline length leads to the most upvotes?
- What submission time leads to the most upvotes?
- How are the total numbers of upvotes changing over time?