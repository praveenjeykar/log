#! /usr/bin/env python

import psycopg2

db_name = "news"


def query_pj(query):
    conn = psycopg2.connect('dbname=' + db_name)
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows


def top_three_articles():
    # query 1: What are the three most popular articles of all time?

    query = """
        select articles.title, count(*) as num
        from articles
        join log
        on log.path like concat('/article/%', articles.slug)
        group by articles.title
        order by num desc
        limit 3;
    """

# executing query for top articles.
    outcome = query_pj(query)

# printing outcomes.
    print('\ntop three articles:')
    c = 1
    for a in outcome:
        print('' + str(c) + '. "' + a[0] + '" with ' + str(a[1]) + " views")
        c = c + 1


def top_three_authors():
    # query 2: Who are the most popular article authors of all time?

    query = """
        select authors.name, count(*) as num
        from authors
        join articles
        on authors.id = articles.author
        join log
        on log.path like concat('/article/%', articles.slug)
        group by authors.name
        order by num desc
        limit 3;
    """

# executing query for top authors.
    outcome = query_pj(query)

# printing outcomes.
    print('\ntop three authors:')
    c = 1
    for a in outcome:
        print('' + str(c) + '. ' + a[0] + ' with ' + str(a[1]) + " views")
        c = c + 1


def error_days():
    # query 3: On which day did more than 1% of requests lead to errors?

    query = """
        select total.day,
          round(((errors.error_requests*1.0) / total.requests), 3) as percent
        from (
          select date_trunc('day', time) "day", count(*) as error_requests
          from log
          where status like '404%'
          group by day
        ) as errors
        join (
          select date_trunc('day', time) "day", count(*) as requests
          from log
          group by day
          ) as total
        on total.day = errors.day
        where (round(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        order by percent desc;
    """

# executing query.
    outcome = query_pj(query)

# printing outcomes
    print('\ndays with more than 1% errors:')
    for a in outcome:
        err = str(round(a[1]*100, 1)) + "%" + " errors"
        dur = a[0].strftime('%B %d, %Y')
        print(dur + " -- " + err)

print('\nfetching the results..')
top_three_articles()
top_three_authors()
error_days()
