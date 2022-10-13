# Django-Sentiment-Analysis-Application

## Description
This application calculates the sentiment of given text and yelp reviews on a 1-5 scale (very bad - very good).

| Score | Sentiment |
|-------|-----------|
|   1   |  very bad |  
|   2   |    bad    |
|   3   |    meh    | 
|   4   |   good    |
|   5   | very good |

## Features
- Calculating sentiment
- Calculating sentiment of Yelp reviews with a given URL
- Sentiment chart for Yelp reviews
- Different forms of displaying data
- Simple and responsive design
- Navigation menu

## Examples
### Even if there are words like funny and witty, the overall structure is a negative type.
![image](https://user-images.githubusercontent.com/85257187/191634136-ac047c38-c06a-478d-8ff2-b1a27d8f1472.png)

### Similar to the last example, even though the words enjoy and sweet are usually considered positive, the overall structure is a negative type.
![image](https://user-images.githubusercontent.com/85257187/193474504-8ea8f7af-9799-424a-83b9-45df222677fc.png)

### Sentiments on a [yelp review](https://www.yelp.ie/biz/mudpie-beauty-cottage-dundrum)
![image](https://user-images.githubusercontent.com/85257187/191635027-fe1a49fe-3cee-471b-b8da-4c32d4e506ea.png)

### More compact table view
![image](https://user-images.githubusercontent.com/85257187/191635090-498331ed-7962-40a8-8248-f27983e44f1c.png)

### Chart

![image](https://user-images.githubusercontent.com/85257187/191635107-5c1db451-6956-492d-b4a0-23a35a277539.png)


## Set up
Follow [this](https://www.codespeedy.com/clone-and-run-a-django-project-from-github/), basically clone this and change the SECRET_KEY and install required libraries
```
pip install -r requirements.txt
```
installing torch might be different depending on your OS etc. so go [here](https://pytorch.org/get-started/locally/) for the command.

Then run this in the same folder where manage.py is and go to http://127.0.0.1:8000/
```
python manage.py runserver
```
