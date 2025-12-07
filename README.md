# Bad Units
Bad Units is a system for working with units, that is bad.

<p>
    <img alt="Stats" src="https://img.shields.io/pypi/v/bad-units">
    <img alt="Stats" src="https://img.shields.io/pypi/pyversions/bad-units">
    <img alt="Stats" src="https://img.shields.io/pypi/l/bad-units">
    <img alt="Stats" src="https://static.pepy.tech/badge/bad-units">
    <img alt="Stats" src="https://static.pepy.tech/badge/bad-units/month">
</p>

# Unit class
This is the most basic part of Bad Units. To make a new unit, you inherit from Unit and set the base_units_per and the unit_type.
Example:
```python
class Meter(Unit):
    unit_type = "length"
    base_units_per = 1
```
Those are the only two things you will ever need to set, Bad Units figures everything out for you. That's nice of it, maybe it isn't so bad after all? Oh, you just wait and see...

Convert between units with the .to() method:
```python
print(Meter().to(Centimeter()))
```
Yes, that's right. The unit to be converted to is an instance of a class and not the class itself. What was I thinking when I made this?

You can add and subtract units:
```python
print(Meter(5)+Centimeter(3)-Millimeter(42))
```
# Compound Units  
## DO NOT USE FOR NOW
Bad Units also supports compound units. That means you can divide one unit by another, multiply them together, and create all kinds of messy physics-like expressions.

Example:

```python
speed = Meter(10) / Second(2)
acceleration = speed / Second(5)
momentum = Meter(10) * Second(2)
```

You can even combine them in horrifying ways:

```python
complex_unit = (Meter(10) / Second(2)) / (Second(5) / Meter(3))
print(complex_unit)
```

The output is… well, it looks like something that belongs in a physics exam. But don’t worry, **Bad Units** will still track your numerators and denominators correctly.

---

# Adding and Subtracting Compound Units  
Yes, you can add and subtract compound units — but only if they “make sense.” Bad Units will yell at you if you try to do something stupid, like add meters per second to kilograms:

```python
valid = (Meter(10) / Second(2)) + (Centimeter(100) / Second(2))
invalid = (Meter(10) / Second(2)) + (Second(5) / Meter(3))  # This will throw a UnitError
```

Notice how the first one works after automatic conversion to base units. The second one is… well… it’s just plain bad.

---

# Printing Units  
When you print a unit or compound unit, Bad Units tries to make it look nice:

```python
print(Meter(10) / Second(2))
# -> 10 Meter/2 Second

print((Meter(10)/Second(2)) / Second(5))
# -> (10 Meter/2 Second)/5 Second
```

If you’re lucky, it even formats nested compound units in a way that’s somewhat readable.

---

# Why “Bad Units”?  
Because it’s intentionally quirky.  
- You deal with **instances instead of classes** for conversions.  
- It complains if you do math that’s dimensionally invalid.  
- Nested compound units can get ugly, fast.  

And yet… somehow it works. Mostly. Maybe. Probably.

---

# Example Usage

```python
class Meter(Unit):
    unit_type = "length"
    base_units_per = 1

class Centimeter(Unit):
    unit_type = "length"
    base_units_per = 0.01

class Second(Unit):
    unit_type = "time"
    base_units_per = 1

# Simple addition
print(Meter(1) + Centimeter(100))

# Compound units
speed = Meter(10) / Second(2)
acceleration = speed / Second(5)
print(speed)
print(acceleration)

# Adding compatible compound units
speed2 = Centimeter(200) / Second(2)
print(speed + speed2)
```

---

# Known Issues / Limitations
- Compound unit conversion is limited; nested or complex units may require manual conversions.  
- Adding incompatible units (like meters/second + seconds/meter) will raise a `UnitError`.  
- Printing deeply nested compounds can get visually messy.  
- Units must be instances for conversions (`Meter().to(Centimeter())`), not classes.  
- It’s “bad” on purpose. That’s part of the charm.
