# Structured Programming - Opdracht 3. Business Rules
# NAAM: Justin Klein - 1707815
# KLAS: V1B (Projectgroep 1)

import psycopg2

# ------------------------------------------------------- #
# ---------------- Calculation Functions ---------------- #
def CalculateFrequency(lst):
    """
    This function counts the amount of times something occurs
    in the list and then stores it in a dictionary.
    @param lst: list
    @return: dictionary
    """
    freqs = dict()
    for nummer in lst:
        if nummer in freqs:
            freqs[nummer] += 1
        elif nummer not in freqs:
            freqs[nummer] = 1
    return freqs

def CalculateModi(lst):
    """
    This function calculates what object in the list occurs the most.
    It uses the CalculateFrequency() function to accurately calculate this.
    @param lst: list
    @return: list
    """
    lst.sort()
    modi = []
    dict = CalculateFrequency(lst)
    x = 0
    for i in dict:
        if modi == []:
            modi.append(i)
            x = dict[i]
            continue
        if dict[i] > x:
            modi = [i]
            x = dict[i]
            continue
        elif dict[i] == x:
            modi.append(i)

    if modi == []:
        for i in lst:
            modi.append(i)

    return sorted(modi)


# --------------------------------------------------- #
# ---------------- Regular Functions ---------------- #
def CreateDrop_Tables():
    """
    This function creates the neccesary tables so that the other
    functions can store recommendations in them. If the tables
    already exist it removes them and creates (empty) new ones.
    """
    # Create connection with postgreSQL database #
    connectie = psycopg2.connect(
        host='localhost',
        database='SP-3',
        user='postgres',
        password='postgres')

    cursor = connectie.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS rec_contentfilter CASCADE")
        cursor.execute("DROP TABLE IF EXISTS rec_collabfilter CASCADE")
        cursor.execute("""CREATE TABLE rec_contentfilter
                                (id VARCHAR PRIMARY KEY,
                                 name VARCHAR,
                                 brand VARCHAR,
                                 category VARCHAR,
                                 subcategory VARCHAR,
                                 subsubcategory VARCHAR,
                                 targetaudience VARCHAR,
                                 sellingprice INTEGER);""")
        cursor.execute("""CREATE TABLE rec_collabfilter
                                (id VARCHAR PRIMARY KEY,
                                 name VARCHAR,
                                 brand VARCHAR,
                                 category VARCHAR,
                                 subcategory VARCHAR,
                                 subsubcategory VARCHAR,
                                 targetaudience VARCHAR,
                                 sellingprice INTEGER);""")

    except (Exception, psycopg2.Error) as error:
        if (connectie):
            print("| Creation of recommendation-tables has failed. |\n", error)

    finally:
        # Commit the creation of the tables and close the connection with the postgreSQL database. #
        print("\n| Tables have been successfully created in the postgreSQL database. |")
        connectie.commit()
        cursor.close()
        connectie.close()


def Content_Filtering(profile_id):
    """
    This function generates recommendations based on product pages
    the person (profile_id) has previously visited and stores them in
    a postgreSQL database. (Table: rec_contentfilter)
    @param profile_id: string
    """
    print("\n| Starting Content-filter |")
    # Create connection with postgreSQL database #
    connectie = psycopg2.connect(
        host='localhost',
        database='SP-3',
        user='postgres',
        password='postgres')

    cursor = connectie.cursor()

    print("Gathering products of selected profile, please wait...")

    # Get all the products that have been seen by profile_id. #
    cursor.execute(f"SELECT prodid FROM profiles_previously_viewed WHERE profid = '{profile_id}'")
    allproducts = cursor.fetchall()
    products = []
    for item in allproducts:
        if item[0] not in allproducts:  # Ensures there are no duplicate products in the list.
            products.append(item[0])

    print(f"Found {len(allproducts)} unique product ID's.")

    # Get all the categories and (sub(sub))categories of said visited products. It also #
    # makes sure that products with 'null' categories are skipped to prevent errors.    #
    cats = []
    subcats = []
    subsubcats = []
    cursor.execute(f"SELECT category, subcategory, subsubcategory "
                   f"FROM products "
                   f"WHERE id IN {tuple(products)} "
                   f"AND category IS NOT NULL "
                   f"AND subcategory IS NOT NULL "
                   f"AND subsubcategory IS NOT NULL")
    recproducts = cursor.fetchall()
    for item in recproducts:
        cats.append(item[0])
        subcats.append(item[1])
        subsubcats.append(item[2])

    print(f"\nMost viewed categories:\n"
          f"Category: '{CalculateModi(cats)[0]}'\n"
          f"Subategory: '{CalculateModi(subcats)[0]}'\n"
          f"Subsubategory: '{CalculateModi(subsubcats)[0]}'\n")

    # Select possible recommendations that fall into the same categories as the #
    # previously visited products that occur the most. (Most viewed categories) #
    cursor.execute(f"SELECT id,name,brand,category,subcategory,subsubcategory,targetaudience,sellingprice "
                   f"FROM products "
                   f"WHERE category = '{CalculateModi(cats)[0]}' "
                   f"AND subcategory = '{CalculateModi(subcats)[0]}' "
                   f"AND subsubcategory = '{CalculateModi(subsubcats)[0]}'")
    possible_recommendations = cursor.fetchall()

    # Insert all the fetched recommendations and insert them in the content-filter recommendation table.
    try:
        for item in possible_recommendations:
            Insert_query = (" INSERT INTO rec_contentfilter (id,name,brand,category,subcategory,subsubcategory,targetaudience,sellingprice) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
            Info = (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            cursor.execute(Insert_query, Info)

    except (Exception, psycopg2.Error) as error:
        if (connectie):
            print("| Processing contentfilter-recommendations has failed. |\n", error)

    finally:
        # Commit the changes to the table and close the connection with the postgreSQL database.
        print("| Recommendations processed. |\n"
              "| All possible recommendations have been added to the postgreSQL database. |\n")
        connectie.commit()
        cursor.close()
        connectie.close()


def Collaborative_Filtering(profile_id):
    """
    This function generates recommendations based on product pages
    that similar profiles (based on the main profile 'profile_id') have previously
    visited and stores them in a postgreSQL database. (Table: rec_collabfilter)
    @param profile_id: string
    """
    print("\n| Starting Collaborationfilter |")
    # Create connection with postgreSQL database
    connectie = psycopg2.connect(
        host='localhost',
        database='SP-3',
        user='postgres',
        password='postgres')

    cursor = connectie.cursor()

    # Get all the similar profiles of the main profile (profile_id) #
    # that have visited 1 or more of the same products.             #
    cursor.execute(f"SELECT prodid FROM profiles_previously_viewed WHERE profid = '{profile_id}'")
    allprofileproducts = cursor.fetchall()
    totalprofiles = []
    for product in allprofileproducts:
        cursor.execute(f"SELECT profid FROM profiles_previously_viewed WHERE prodid = '{product[0]}'")
        profiles = cursor.fetchall()
        for profile in profiles:
            if profile[0] not in totalprofiles:  # Ensures there are no duplicate profiles in the list.
                totalprofiles.append(profile[0])

    print(f"ID: '{profile_id}' has {len(totalprofiles)} similar profiles.\n"
          f"Gathering products of selected profiles, please wait...")

    # Gathers all the unique product ID's that the similar profiles have seen as well #
    cursor.execute(f"SELECT prodid FROM profiles_previously_viewed WHERE profid IN {tuple(totalprofiles)}")
    selectedproducts = cursor.fetchall()
    totalproducts = []
    for product in selectedproducts:
        if product[0] not in totalproducts:  # Ensures there are no duplicate products in the list.
            totalproducts.append(product[0])

    print(f"Found {len(totalproducts)} unique product ID's.")

    # Get all the categories and (sub(sub))categories of said visited products. It also #
    # makes sure that products with 'null' categories are skipped to prevent errors.    #
    cats = []
    subcats = []
    subsubcats = []
    cursor.execute(f"SELECT category,subcategory,subsubcategory "
                   f"FROM products "
                   f"WHERE id IN {tuple(totalproducts)} "
                   f"AND category IS NOT NULL "
                   f"AND subcategory IS NOT NULL "
                   f"AND subsubcategory IS NOT NULL")
    recproducts = cursor.fetchall()
    for item in recproducts:
        cats.append(item[0])
        subcats.append(item[1])
        subsubcats.append(item[2])

    print(f"\nMost viewed categories:\n"
          f"Category: '{CalculateModi(cats)[0]}'\n"
          f"Subategory: '{CalculateModi(subcats)[0]}'\n"
          f"Subsubategory: '{CalculateModi(subsubcats)[0]}'\n")

    # Select possible recommendations that fall into the same categories as the #
    # previously visited products that occur the most. (Most viewed categories) #
    cursor.execute(f"SELECT id,name,brand,category,subcategory,subsubcategory,targetaudience,sellingprice "
                   f"FROM products "
                   f"WHERE category = '{CalculateModi(cats)[0]}' "
                   f"OR subcategory = '{CalculateModi(subcats)[0]}' "
                   f"OR subsubcategory = '{CalculateModi(subsubcats)[0]}'")
    possible_recommendations = cursor.fetchall()

    # Insert all the fetched recommendations and insert them in the new recommendation table.
    try:
        for item in possible_recommendations:
            Insert_query = (" INSERT INTO rec_collabfilter (id,name,brand,category,subcategory,subsubcategory,targetaudience,sellingprice) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")
            Info = (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
            cursor.execute(Insert_query, Info)

    except (Exception, psycopg2.Error) as error:
        if (connectie):
            print("| Processing collabfilter-recommendations has failed. |\n", error)

    finally:
        # Commit the changes to the table and close the connection with the postgreSQL database.
        print("| Recommendations processed. |\n"
              "| All possible recommendations have been added to the postgreSQL database. |\n")
        connectie.commit()
        cursor.close()
        connectie.close()


# ------------------------------------------- #
# ---------------- Execution ---------------- #
CreateDrop_Tables()
Content_Filtering('5a393d68ed295900010384ca')
Collaborative_Filtering('5a3884658d11a5e91c26fb04')