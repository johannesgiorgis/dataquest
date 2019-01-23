# Project: Working with Data Downloads

Below are the notes and steps taken for this project.

## Introduction to the dataset

The data set we'll work with is called the Civil Rights Data Collection. It contains information on educational achievement and opportunities in the U.S., broken down by race and school. For example, it records the racial composition of the students enrolled in advanced classes at each school. Each row represents a school, while each column records an indicator of academic achievement.

For the purposes of this exercise, we'll be using a subset of the data that only contains `1` out of every `100` rows in the original data set. If you'd like to work with the original version, you can download it from [data.gov](https://catalog.data.gov/dataset/civil-rights-data-collection-2013-14).

Before we can load and analyze the data, we'll need to extract the files from the archive file, `crdc201314csv.zip`. We can run the [unzip](https://linux.die.net/man/1/unzip) command on an archive file to extract the files within it.

## Exploring Data Dictionary

The folder you unzipped contains two files:

- `CRDC2013_14.csv`: the actual subset of the data we'll explore
- `CRDC2013_14content.csv`: an explanatory file that describes each of the columns in `CRDC2013_14.csv`
    
The explanatory file, also known as a [data dictionary](https://en.wikipedia.org/wiki/Data_dictionary), was included because the dataset contains more than `2000` columns. Let's start by reading in the data dictionary into pandas and exploring it more.

## Explore Interesting columns

Now that we've looked at the column names more closely, here are some potentially interesting ones that popped out:

- `JJ` - Indicates whether the school is part of a [juvenile justice facility](https://en.wikipedia.org/wiki/Youth_detention_center), or youth prison.
- `SCH_STATUS_MAGNET` - Indicates whether the school is a [magnet school](https://en.wikipedia.org/wiki/Magnet_school), an advanced school for students who achieve high scores on certain tests.

We can dig around for interesting patterns here by using [Series.value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) to find unique values in each column. This will tell us how many schools are juvenile justice facilities or magnet schools.

We can also count how many students are in juvenile justice facilities by using the [pandas.pivot_table()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.pivot_table.html) function to create a pivot table. Building a pivot table will allow us to aggregate `TOT_ENR_M` and `TOT_ENR_F` (which record school enrollment by gender) by `JJ` and `SCH_STATUS_MAGNET`. This will count up how many students are in magnet schools or juvenile justice facilities.

The Python code below, for example, will create a pivot table that counts the total number of male and female students in juvenile justice facilities:


```
import pandas as pd
pd.pivot_table(data, values=["TOT_ENR_M", "TOT_ENR_F"], index="JJ", aggfunc="sum")
```

## Enrollment by Race and Gender

Several of the columns in our data break school attributes down by race and gender. The names of these columns begin with an abbreviation for the attribute name. `SCH_ENR` stands for "school enrollment," for example. Next, they include a code name for race, such as `HP`. The last part is a code name for gender, which is either `F` or `M`. For example, the complete name for the column that records hispanic female enrollment is `SCH_ENR_HI_F`.

Here are the code names for each race:

- `HI` - Hispanic
- `AM` - American Indian
- `AS` - Asian
- `HP` - Hawaiian or Pacific Islander
- `BL` - Black
- `WH` - White
- `TR` - Two or more races

Here are the gender code names:

- `F` - Female
- `M` - Male

The data set contains one column for every possible combination of racial and gender code names associated with an attribute -- that's why there are more than 2,000 columns!

Here's a list of all of the columns that indicate school enrollment, for example:

- `SCH_ENR_HI_M`
- `SCH_ENR_HI_F`
- `SCH_ENR_AM_M`
- `SCH_ENR_AM_F`
- `SCH_ENR_AS_M`
- `SCH_ENR_AS_F`
- `SCH_ENR_HP_M`
- `SCH_ENR_HP_F`
- `SCH_ENR_BL_M`
- `SCH_ENR_BL_F`
- `SCH_ENR_WH_M`
- `SCH_ENR_WH_F`
- `SCH_ENR_TR_M`
- `SCH_ENR_TR_F`

There are also two columns that indicate total enrollment by gender:

- `TOT_ENR_M` - Total male enrollment
- `TOT_ENR_F` - Total female enrollment

Several other column names combine race and gender codes, including:

- `SCH_HBREPORTED_DIS` - Students who report being harrased or bullied
- `SCH_DISCWODIS_EXPWOE` - Students without disabilities who were expelled from school
- `SCH_RET_G12` - Students who started and completed grade 12


## Next steps

Now that you've read in the files and found some interesting columns, you can dig in and analyze the data more. There are quite a few interesting angles you could explore:

- Review expulsions (which refers to when students are kicked out of school permanently). Columns like `SCH_DISCWODIS_EXPWOE_HI_M` and `TOT_DISCWODIS_EXPZT_F` contain information on expulsions.
- Explore gender and race differences in SAT scores. Columns like `SCH_SATACT_HI_M` contain this information.
- Figure out the racial and gender breakdowns for different types of schools, such as magnet schools.
- Determine how many students are in gifted and talented programs, or advanced placement classes.
- Investigate how racial differences in enrollment change from preschool to high school.
- Explore school bullying. The `SCH_HBDISCIPLINED_DIS_HI_M` column contains some of this information.
