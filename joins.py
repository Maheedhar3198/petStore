import pymysql
from playwright.sync_api import sync_playwright

from env import BASE_URL, USERNAME, PASSWORD
from sql_database import sql_server

playwright = sync_playwright().start()
browser = playwright.chromium.launch(channel="chromium", headless=False)
page = browser.new_page()

connection = sql_server()
cursor = connection.cursor()

def test_orders_with_customers():
    query = """
        SELECT o.order_id, o.pet_name, o.quantity, c.customer_id, c.customer_name
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("Orders with Customers:")
    for row in results:
        print(row)

    return results

def test_login_and_validate_orders():
    page.goto(BASE_URL)
    page.fill("//input[@name='username']", USERNAME)
    page.fill("//input[@name='password']", PASSWORD)
    page.click("//input[@name='signon']")

    if page.is_visible("text=Welcome"):
        data = test_orders_with_customers()
        if not data:
            print("No orders linked with customers")
        else:
            print("Orders are correctly linked with customers")
    else:
        browser.close()

    connection.close()


