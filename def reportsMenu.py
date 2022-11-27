def reportsMenu():
    """
    ============================================================================
    Function:       reportsMenu()
    Purpose:        provides user options for accessing reports
    Parameter(s):   -None- 
    Return:         users desired action
    ============================================================================
    """
    os.system('cls')

    now = datetime.datetime.now()
    print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
    print(("isbn-22 " + VERNO + " " + VERNA).rjust(80))
    print("-----------------------".rjust(80))
    print(Style.RESET_ALL)

    goAgain = 1

    # reports menu and options
    # ------------------------
    while goAgain == 1:
        print('')
        print(Fore.GREEN + 'REPORTS')
        print(Fore.GREEN + '-------------------')
        print(Style.RESET_ALL)
        print('1\tShow All Records')
        print('2\tShow Filtered Records')
        print('')
        print('')
        print('')
        print(Fore.RED + '0\tRETURN')
        print(Style.RESET_ALL)
        print('')
        print('')    

        menuOption = input("selection: ")

        # all records report
        # -------------------
        if menuOption == '1':
            print(Fore.GREEN + 'All Records')
            print(Fore.GREEN + '-------------------')
            print(Style.RESET_ALL)
            print('')
            mysql_search_query = ("SELECT * FROM isbn")
            cursor = CONNECTION.cursor(buffered = True)
            cursor.execute(mysql_search_query)    
            mytable = from_db_cursor(cursor)
            mytable.align = "l"
            print(mytable)
            print('')
            # send report to browser
            # -----------------------
            printRep = input(Fore.YELLOW + 'To send this report to the browser '
                            'for printing or saving enter b or B, otherwise press '
                            'enter to return: ')
            print(Style.RESET_ALL)
            if printRep == "b" or printRep == "B":
                # generate data for report
                # ------------------------
                mysql_search_query = ("SELECT * FROM isbn")
                cursor = CONNECTION.cursor(buffered = True)
                cursor.execute(mysql_search_query)
                mytable = pd.read_sql("select * from isbn", CONNECTION)
                pd.set_option('display.expand_frame_repr', False)
                mytable2 = build_table(mytable,
                                     'grey_light',
                                     font_size = 'small',
                                     font_family = 'Open Sans, courier',
                                     text_align = 'left ')
                # generate html content
                # ---------------------
                html_content = f"<html> \
                                <head> <h2> Unfiltered Report - All Records\
                                </h2> \
                                <h3> <script>\
                                var timestamp = Date.now();\
                                var d = new Date(timestamp);\
                                document.write(d);\
                                </script>\
                                </h3>\
                                </head> \
                                <body> {mytable2} \
                                </body> \
                                </html>"
                with open("report/all_no_filter.html", "w") as html_file:
                    html_file.write(html_content)
                    print("Created")
                time.sleep(2)
                # display in browser
                # ------------------
                webbrowser.open_new_tab("report\\all_no_filter.html")
                print('')
                wait = input("Press ENTER to return")

        # filtered records report
        # -----------------------
        if menuOption == '2':
            print(Fore.GREEN + 'Filtered Records')
            print(Fore.GREEN + '-------------------')
            print(Style.RESET_ALL)
            print('')
            print('Select Filter:')
            print('')
            print('1\tISBN')
            print('2\tyear')
            print('3\tpublisher')
            print('4\tauthor')
            print('5\ttitle')
            print('6\tgenre')
            print('')
            print('7\tcreate a custom filter')
            print('')
            filt = input("select filter: ")
            if filt == '1':
                fil = "isbn"
            if filt == '2':
                fil = "year"
            if filt == '3':
                fil = "publisher"
            if filt == '4':
                fil = "author"
            if filt == '15':
                fil = "title"
            if filt == '6':
                fil = "genre"
            if filt == '7':
                fil = "custom"
            # create custom query for report data
            # ------------------------------------
            if fil == "custom":
                os.system('cls')
                print(Fore.GREEN + now.strftime("%Y-%m-%d %H:%M:%S").rjust(80))
                print(("isbn-22 " + VERNO + " " + VERNA).rjust(80))
                print("-----------------------".rjust(80))
                print(Style.RESET_ALL)
                print('On this screen you can enter your own SQL WHERE statement\n'
                    'to be used in the query. Please be aware that this staement\n'
                    'must be entered correctly, following proper SQL syntax')
                print('')
                # define custom query
                # -------------------
                customQuery = input("Please enter your WHERE clause here,"
                                    " starting with WHERE:  ")
                mysql_search_query = ("SELECT * FROM isbn " + customQuery)
                cursor = CONNECTION.cursor(buffered = True)
                cursor.execute(mysql_search_query)    
                mytable = from_db_cursor(cursor)
                mytable.align = "l"
                print('')
                print(mytable)
                print('')
                printRep = input(Fore.YELLOW + 'To send this report to the '
                                'browser for printing or saving enter b or B, '
                                'otherwise press enter to return: ')
                print(Style.RESET_ALL)
                # send report to browser
                # -----------------------
                if printRep == "b" or printRep == "B":
                    mysql_search_query = ("SELECT * FROM isbn " + customQuery)
                    cursor = CONNECTION.cursor(buffered = True)
                    cursor.execute(mysql_search_query)
                    mytable = pd.read_sql("SELECT * FROM isbn " + 
                                            customQuery, CONNECTION)
                    pd.set_option('display.expand_frame_repr', False)
                    mytable2 = build_table(mytable,
                                         'grey_light',
                                         font_size = 'small',
                                         font_family = 'Open Sans, courier',
                                         text_align = 'left ')
                    # generate html content
                    # ---------------------
                    html_content = f"<html> \
                                    <head> <h2>Filtered Report - Filter: \
                                    {customQuery} \
                                    </h2> \
                                    <h3> <script>\
                                    var timestamp = Date.now();\
                                    var d = new Date(timestamp);\
                                    document.write(d);\
                                    </script>\
                                    </h3>\
                                    </head> \
                                    <body> {mytable2} \
                                    </body> \
                                    </html>"
                    with open("report/all_filtered.html", "w") as html_file:
                        html_file.write(html_content)
                        print("Created")
                    time.sleep(2)
                    # display in browser
                    # ------------------
                    webbrowser.open_new_tab("report\\all_filtered.html")
                    print('')
                print("The custom query was " + Fore.RED + customQuery + 
                        Style.RESET_ALL + " would you like to save this query?")
                saveQ = input("If you want to save this query, enter y or Y: ")
                if saveQ == 'y' or saveQ == 'Y':
                    saveQname = input("Please enter a simple query name: ")
                    saveQdesc = input("Please enter a brief description of the "
                                "query: ")
                    print('')
                    print("Available types are:")
                    print("--------------------")
                    mysql_search_type = ("SELECT * FROM cqType")
                    cursor = CONNECTION.cursor(buffered = True)
                    cursor.execute(mysql_search_type)
                    mytable = pd.read_sql("select * from cqType", CONNECTION)
                    pd.set_option('display.expand_frame_repr', False)
                    mytable.align = "l"
                    print(mytable)
                    print('')
                    saveQtype = input("Please enter a query type: ")
                    #saveQuser = input("User: ")
                    today = date.today()
                    data = (saveQname, saveQdesc, saveQtype, mysql_search_query,\
                            USER, today)
                    cq_insert_query = (
                    "INSERT INTO cQuery (cq_name, cq_desc, cq_type, cq_query,\
                                        cq_creator, cq_created)"
                    "VALUES (%s, %s, %s, %s, %s, %s)"
                    )
                    cursor = CONNECTION.cursor()
                    cursor.execute(cq_insert_query, data)
                    CONNECTION.commit()
                    print('')
                    print(Fore.YELLOW + "cQuery "+ saveQname + " created")
                    print(Style.RESET_ALL)
                    








            else:
                # get data for report
                # -------------------
                filterValue = input("select value to filter by: ")
                mysql_search_query = ("SELECT * FROM isbn WHERE " + fil + " = " + 
                                    filterValue)
                cursor = CONNECTION.cursor(buffered = True)
                cursor.execute(mysql_search_query)    
                mytable = from_db_cursor(cursor)
                mytable.align = "l"
                print('')
                # display report
                # --------------
                mytable.align = "l"
                print(mytable)
                print('')
                printRep = input(Fore.YELLOW + 'To send this report to the browser '
                                'for printing or saving enter b or B, otherwise '
                                'press enter to return: ')
                print(Style.RESET_ALL)
                # send report to browser
                # -----------------------
                if printRep == "b" or printRep == "B":
                    mysql_search_query = ("SELECT * FROM isbn WHERE " + fil + 
                                        " = " + filterValue)
                    cursor = CONNECTION.cursor(buffered = True)
                    cursor.execute(mysql_search_query)
                    mytable = pd.read_sql("SELECT * FROM isbn WHERE " + fil + 
                                        " = " + filterValue, CONNECTION)
                    pd.set_option('display.expand_frame_repr', False)
                    mytable2 = build_table(mytable,
                                         'grey_light',
                                         font_size = 'small',
                                         font_family = 'Open Sans, courier',
                                         text_align = 'left ')
                    # generate html content
                    # ---------------------
                    html_content = f"<html> \
                                    <head> <h2>Filtered Report - Filter: \
                                    {mysql_search_query} \
                                    </h2> \
                                    <h3> <script>\
                                    var timestamp = Date.now();\
                                    var d = new Date(timestamp);\
                                    document.write(d);\
                                    </script>\
                                    </h3>\
                                    </head> \
                                    <body> {mytable2} \
                                    </body> \
                                    </html>"
                    with open("report/all_filtered.html", "w") as html_file:
                        html_file.write(html_content)
                        print("Created")
                    time.sleep(2)
                    # display in browser
                    # ------------------
                    webbrowser.open_new_tab("report\\all_filtered.html")
                    print('')
                    wait = input("Press ENTER to return")
            wait = input("Press ENTER to return")

        elif menuOption == '0':
            goAgain = 0   




