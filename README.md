# Purchase-Analytics


## Problem

Instacart has published a [dataset](https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders.


**For this challenge, I calculated, for each department, the number of times a product was requested, number of times a product was requested for the first time and a ratio of those two numbers.**



## Input Datasets

I two separate input data sources, `order_products.csv` and `products.csv`.

You can assume each line of the file `order_products.csv` holds data on one request. The file contains data of the form

```
order_id,product_id,add_to_cart_order,reordered
2,33120,1,1
2,28985,2,1
2,9327,3,0
2,45918,4,1
3,17668,1,1
3,46667,2,1
3,17461,4,1
3,32665,3,1
4,46842,1,0
```

where

* `order_id`: unique identifier of order
* `product_id`: unique identifier of product
* `add_to_cart_order`: sequence order in which each product was added to shopping cart
* `reordered`: flag indicating if the product has been ordered by this user at some point in the past. The field is `1` if the user has ordered it in the past and `0` if the user has not. While data engineers should validate their data, for the purposes of this challenge, you can take the `reordered` flag at face value and assume it accurately reflects whether the product has been ordered by the user before.

The file `products.csv` holds data on every product, and looks something like this:

```
product_id,product_name,aisle_id,department_id
9327,Garlic Powder,104,13
17461,Air Chilled Organic Boneless Skinless Chicken Breasts,35,12
17668,Unsweetened Chocolate Almond Breeze Almond Milk,91,16
28985,Michigan Organic Kale,83,4
32665,Organic Ezekiel 49 Bread Cinnamon Raisin,112,3
33120,Organic Egg Whites,86,16
45918,Coconut Butter,19,13
46667,Organic Ginger Root,83,4
46842,Plain Pre-Sliced Bagels,93,3
```
where

* `product_id`: unique identifier of the order
* `product_name`: name of the product
* `aisle_id`: identifier of aisle in which product is located
* `department_id`: identifier of department


## Expected Output

Given the two input files in the input directory, your program should create an output file, `report.csv`, in the output directory that, for each department, surfaces the following statistics:

`number_of_orders`. How many times was a product requested from this department? (If the same product was ordered multiple times, we count it as multiple requests)

`number_of_first_orders`. How many of those requests contain products ordered for the first time?

`percentage`. What is the percentage of requests containing products ordered for the first time compared with the total number of requests for products from that department? (e.g., `number_of_first_orders` divided by `number_of_orders`)

For example, with the input files given above, the correct output file is

```
department_id,number_of_orders,number_of_first_orders,percentage
3,2,1,0.50
4,2,0,0.00
12,1,0,0.00
13,2,1,0.50
16,2,0,0.00
```

<<<<<<< HEAD
*The output file should adhere to the following rules*
=======
*The output file should adhered to the following rules*
>>>>>>> 71000f3acbbfd44b7cb53832e00a151679848e28

- It is listed in ascending order by `department_id`
- A `department_id` should be listed only if `number_of_orders` is greater than `0`
- `percentage` should be rounded to the second decimal

The examples input and out files are provided in the `insight_testsuite/tests/test_1/input` and `insight_testsuite/tests/test_1/output` folders, respectively.

<<<<<<< HEAD
## Instructions
 To solve this challenge you might pick a programing language of your choice (preferably Python, Scala, Java, or C/C++ because they are commonly used and will help us better assess you), but you are only allowed to use the default data structures that come with that programming language (you might use I/O libraries). For example, you can code in Python, but you should not use Pandas or any other external libraries.

***The objective here is to see if you can implement the solution using basic data structure building blocks and software engineering best practices (by writing clean, modular, and well-tested code).***


# Tips on getting an interview

## Writing clean, scalable and well-tested code

As a data engineer, it’s important that you write clean, well-documented code that scales for a large amount of data. For this reason, it’s important to ensure that your solution works well for a large number of records, rather than just the above example.

[Here](https://www.instacart.com/datasets/grocery-shopping-2017) you can find large datasets to test your code (see [here](https://gist.github.com/jeremystan/c3b39d947d9b88b3ccff3147dbcf6c6b) for its data dictionary).
You can test your code using the files `order_products_train.csv` and `order_products_prior.csv` together with the file `products.csv`.
Note, we will use it to test the full functionality of your code, along with other tests.

It's also important to use software engineering best practices like unit tests, especially since data is not always clean and predictable.


=======
I have used only the basic structures in Python to develop this code
***The objective here is to see if you can implement the solution using basic data structure building blocks and software engineering best practices (by writing clean, modular, and well-tested code).***



>>>>>>> 71000f3acbbfd44b7cb53832e00a151679848e28

## Repo directory structure

The directory structure for your repo should look like this:

    ├── README.md
    ├── run.sh
    ├── src
    │   └── purchase_analytics.py
    ├── input
    │   └── products.csv
    |   └── order_products.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── products.csv
            |   │   └── order_products.csv
            |   |__ output
            |   │   └── report.csv
            ├── your-own-test_1
                ├── input
                │   └── your-own-products.csv
                |   └── your-own-order_products.csv
                |── output
                    └── report.csv

<<<<<<< HEAD
**Don't fork this repo** and don't use this `README` instead of your own. The content of `src` does not need to be a single file called `purchase_analytics.py`, which is only an example. Instead, you should include your own source files and give them expressive names.

## Testing your directory structure and output format

To make sure that your code has the correct directory structure and the format of the output files are correct, we have included a test script called `run_tests.sh` in the `insight_testsuite` folder.

=======

## Testing your directory structure and output format

T
>>>>>>> 71000f3acbbfd44b7cb53832e00a151679848e28
The tests are stored simply as text files under the `insight_testsuite/tests` folder. Each test should have a separate folder with an `input` folder for `products.csv` and `order_products.csv` and an `output` folder for `report.csv`.

You can run the test with the following command from within the `insight_testsuite` folder:

    insight_testsuite~$ ./run_tests.sh

On a failed test, the output of `run_tests.sh` should look like:

    [FAIL]: test_1
    [Thu Mar 30 16:28:01 PDT 2017] 0 of 1 tests passed

On success:

    [PASS]: test_1
    [Thu Mar 30 16:25:57 PDT 2017] 1 of 1 tests passed




=======
>>>>>>> 71000f3acbbfd44b7cb53832e00a151679848e28
