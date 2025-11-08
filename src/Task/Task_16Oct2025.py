"""Q-1 You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request"""

num = int(input("enter response"))
if num ==200 :
    print("✅")
elif num ==404 :
    print("❌")
"""Q-2 In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches"""

expected_title = "Dashboard"
actual_title = "Dashboard "
actual = actual_title.strip()

if actual == expected_title :
    print("Equal")
else :
    print("Not Equal")


"""You want to check whether a web page loads within 3 seconds (performance test condition).

load_time = 4.2
⚠️ Page load too slow: 4.2 seconds"""
num = float(input("enter response"))
if num<3 :
    print("Page is fast")
else :
    print("Page is slow")

"""Q4 
Check if the user can log in based on correct username and password.
I/p
username = "admin"
password = "1234"
O/p ✅ Login Successful
For the Fail condition Other O/P = ❌ Invalid Credentials"""

username = str(input("enter username"))
password = str(input("enter password"))
if username == "admin" and password == "1234" :
    print("Login Successful")
else :
    print("Login Failed")