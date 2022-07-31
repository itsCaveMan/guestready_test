# Guest Ready screening test
This Django project is dedicated to the devs @ GuestReady.com as part of their interviewing process


> Written in  [StackEdit](https://stackedit.io/).


## Technologies

 - Python 🐍 - 3.9
 - Django 📄 - 4.0.6
 

## Setup

1. Clone repository
2. Create/activate venv of choice
3. `cd` into freshly cloned repo
4. `pip install requirements.txt`
5. Create your local db with `python3 manage.py migrate`
6. and run server with `python3 manage.py runserver`
7. or  run tests with `python3 manage.py test`


## Main implementations
- models.py
- index.py
- test_previous_reservation.py
- views.py

<br>


## Spoilers
![result](https://user-images.githubusercontent.com/51651537/182032388-068f6eaf-b17e-4fa9-aaaf-6dab995a14b1.png)





<br>
<br>

# ref - Test description
  

**TEST TASK - Python Django Engineer - Remote**

  

**Lets we have a django project.**

With models:

  

**Rental**

- name

**Reservation**

- rental_id

- checkin(date)

- checkout(date)

  

  

**Add the view with the table of Reservations with "previous reservation ID".**

**Previous reservation is a reservation that is before the current one into same**

**rental.**

  

  

Example:

Rental-1

Res-1(2022-01-01, 2022-01-13)

Res-2(2022-01-20, 2022-02-10)

Res-3(2022-02-20, 2022-03-10)

  

Rental-2

Res-4(2022-01-02, 2022-01-20)

Res-5(2022-01-20, 2022-02-11)

  

  

|Rental_name  |ID  |Checkin  |Checkout  |Previous reservation, ID  |

|rental-1 |Res-1 ID  | 2022-01-01  |2022-01-13  | -  |

|rental-1 |Res-2 ID  | 2022-01-20  |2022-02-10  | Res-1 ID |

|rental-1 |Res-3 ID  | 2022-02-20  |2022-03-10  | Res-2 ID |

|rental-2 |Res-4 ID  | 2022-01-02  |2022-01-20  | -  |

|rental-2 |Res-5 ID  | 2022-01-20  |2022-01-11  | Res-4 ID |

  

**Also, add a tests.**

**Create it into github repo and provide a link to it.**
