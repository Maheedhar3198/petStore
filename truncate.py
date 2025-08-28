import pymysql
from playwright.sync_api import sync_playwright

from env import BASE_URL, USERNAME, PASSWORD
from sql_database import sql_server

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel="chromium", headless=False)
page = browser.new_page()

connection = sql_server()
cursor = connection.cursor()

def test_truncate_cart():
    query = "SELECT * FROM cart"
    cart_details = cursor.execute(query)
    # cursor.execute("TRUNCATE TABLE customers")
    # cursor.execute("DROP TABLE cart)
    print(cart_details)
    cursor.execute("TRUNCATE TABLE cart")
    connection.commit()
    connection.close()

def test_login():
    page.goto(BASE_URL)
    page.fill("//input[@name='username']", USERNAME)
    page.fill("//input[@name='password']", PASSWORD)
    page.click("//input[@name='signon']")
    if page.is_visible("text=Welcome"):
        test_truncate_cart()
    else:
        browser.close()

