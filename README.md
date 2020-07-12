# Hourglass

Hourglass is still in its infancy, but if you want to install, you may do this:

```
pip install git+https://github.com/remykarem/hourglass#egg=hourglass
```

## Arithmetic

Perform intuitive arithmetics with the `hourglass.Date` object.

```python
>>> from hourglass import Date

>>> date = Date(2020,7,12)
>>> date + "5 days"
2020-07-17
>>> date + "2 weeks"
2020-07-26
>>> date - "3 months"
2020-04-14
```

The default behaviour when peforming arithmetics with `int` type is adding or subtracting the no. of days:

```python
>>> date - 1
2020-07-11
```

It can also take in multiple:

```python
>>> date + "2 weeks" - "3 days"
2020-07-26
```

Unfortunately, it's still not grammatical

```python
>>> date + "1 days"
2020-07-13
```

## Properties

The `hourglass.Date` object has several properties that the `datetime.date` has:

```python
>>> date.is_weekend
False
>>> date.day_of_week
1
>>> date.day_name
'Tuesday'
```

## Ranges

Iterate through dateranges with the `hourglass.daterange` class. Yes, it's lowercase so that it looks like Python's builtin `range`.

```python
>>> from hourglass import daterange

>>> for date in daterange(Date(2020,7,12), Date(2020,7,15)):
>>>     if date.is_weekday:
>>>         print(date)
2020-07-13
2020-07-14
```

You can rewrite the above without the `Date` too. Just make sure the start and end are tuples.

```python
>>> for date in daterange((2020,7,12), (2020,7,15)):
>>>     if date.is_weekday:
>>>         print(date)
2020-07-13
2020-07-14
```

The underlying objects are `datetime.date`.

## Other module-level functions

```python
>>> from hourglass import today, yesterday
>>> today()
2020-07-12
>>> yesterday()
2020-07-11
```
