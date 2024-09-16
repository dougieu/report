import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import os
import subprocess
import time
import sys

def save_chrome_driver_path(path):
    with open('data.txt', 'w') as f:
        f.write(path)

def load_chrome_driver_path():
    if os.path.exists('data.txt'):
        with open('data.txt', 'r') as f:
            return f.read().strip()
    return None

def kill_existing_chrome_processes():
    if os.name == 'nt':  # For Windows
        subprocess.call(["taskkill", "/F", "/IM", "chrome.exe"])
    else:  # For Unix-based systems
        subprocess.call(["pkill", "chrome"])

def open_tiktok_profile():
    username = username_entry.get()
    if not username:
        messagebox.showerror("Error", "Please enter a username")
        return

    kill_existing_chrome_processes()

    chrome_driver_path = load_chrome_driver_path()
    if not chrome_driver_path:
        chrome_driver_path = ChromeDriverManager().install()
        save_chrome_driver_path(chrome_driver_path)

    options = Options()
    user_data_dir = "C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data".format(os.getenv('USERNAME'))
    options.add_argument(f"user-data-dir={user_data_dir}")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--app=https://www.tiktok.com')  # Open in app mode
    options.add_argument('--window-size=1280,1280')  # Set window size to a square
    options.add_argument('--window-position=0,0')  # Set window position

    service = Service(chrome_driver_path)
    
    # Suppress console output
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')

    global driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f"https://www.tiktok.com/@{username}")

    # Wait for 3 seconds
    time.sleep(3)

    # Click the button using XPath
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div[1]/div[1]"))
        )
        button.click()
    except Exception as e:
        print(f"Error clicking the button: {e}")

    # Hide specified elements
    elements_to_hide = [
        "/html/body/div[1]/div[1]/div",
        "/html/body/div[1]/div[1]",
        "/html/body/div[1]/div[2]/div[1]",
        "/html/body/div[1]/div[2]/div[2]/div/div/div[2]",
        "/html/body/div[1]/div[2]/div[3]/div/button",
        "/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[1]/svg/path"
    ]

    for xpath in elements_to_hide:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            driver.execute_script("arguments[0].style.display = 'none';", element)
        except Exception as e:
            print(f"Error hiding element {xpath}: {e}")

    # Disable scrolling
    driver.execute_script("document.body.style.overflow = 'hidden';")

    # Inject buttons into the page immediately
    driver.execute_script("""
        var startStopButton = document.createElement('button');
        startStopButton.innerHTML = 'Start';
        startStopButton.style.position = 'fixed';
        startStopButton.style.top = '10px';
        startStopButton.style.left = '10px';
        startStopButton.style.zIndex = '1000';
        startStopButton.style.backgroundColor = 'white';
        startStopButton.onclick = function() {
            if (startStopButton.innerHTML === 'Start') {
                startStopButton.innerHTML = 'Stop';
                window.isRunning = true;
                window.runSequenceLoop();
            } else {
                startStopButton.innerHTML = 'Start';
                window.isRunning = false;
            }
        };
        document.body.appendChild(startStopButton);

        var runSequenceButton = document.createElement('button');
        runSequenceButton.innerHTML = 'Run Sequence Once';
        runSequenceButton.style.position = 'fixed';
        runSequenceButton.style.top = '10px';
        runSequenceButton.style.left = '80px';
        runSequenceButton.style.zIndex = '1000';
        runSequenceButton.style.backgroundColor = 'white';
        runSequenceButton.onclick = function() {
            window.runSequenceOnce();
        };
        document.body.appendChild(runSequenceButton);
    """)

    # Define the runSequenceOnce function
    driver.execute_script("""
        window.runSequenceOnce = function() {
            var firstElement = document.evaluate("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            if (firstElement) {
                var event = new MouseEvent('mouseover', {
                    'view': window,
                    'bubbles': true,
                    'cancelable': true
                });
                firstElement.dispatchEvent(event);

                setTimeout(function() {
                    var reportButton = document.evaluate("//div[contains(@class, 'css-17g6wa2-DivActionItem') and .//p[contains(text(), 'Report')]]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                    if (reportButton) {
                        var actions = new MouseEvent('mouseover', {
                            'view': window,
                            'bubbles': true,
                            'cancelable': true
                        });
                        reportButton.dispatchEvent(actions);

                        setTimeout(function() {
                            reportButton.click();

                            setTimeout(function() {
                                var label1 = document.evaluate("/html/body/div[8]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/label", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                                if (label1) {
                                    var event = new MouseEvent('mouseover', {
                                        'view': window,
                                        'bubbles': true,
                                        'cancelable': true
                                    });
                                    label1.dispatchEvent(event);

                                    setTimeout(function() {
                                        label1.click();

                                        setTimeout(function() {
                                            var userOption = document.evaluate("//*[contains(text(), 'User could be under 13 years old')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                                            if (userOption) {
                                                var event = new MouseEvent('mouseover', {
                                                    'view': window,
                                                    'bubbles': true,
                                                    'cancelable': true
                                                });
                                                userOption.dispatchEvent(event);

                                                setTimeout(function() {
                                                    userOption.click();

                                                    setTimeout(function() {
                                                        var submitButton = document.evaluate("/html/body/div[8]/div/div[2]/div/div/div[2]/div/div/section/form/div[2]/div[3]/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                                                        if (submitButton) {
                                                            var event = new MouseEvent('mouseover', {
                                                                'view': window,
                                                                'bubbles': true,
                                                                'cancelable': true
                                                            });
                                                            submitButton.dispatchEvent(event);

                                                            setTimeout(function() {
                                                                submitButton.click();

                                                                setTimeout(function() {
                                                                    var doneButton = document.evaluate("/html/body/div[8]/div/div[2]/div/div/div[2]/div/div/section/div/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                                                                    if (doneButton) {
                                                                        var event = new MouseEvent('mouseover', {
                                                                            'view': window,
                                                                            'bubbles': true,
                                                                            'cancelable': true
                                                                        });
                                                                        doneButton.dispatchEvent(event);

                                                                        setTimeout(function() {
                                                                            doneButton.click();
                                                                            if (window.isRunning) {
                                                                                window.runSequenceLoop();
                                                                            }
                                                                        }, 1000);
                                                                    }
                                                                }, 1000);
                                                            }, 1000);
                                                        }
                                                    }, 1000);
                                                }, 1000);
                                            }
                                        }, 1000);
                                    }, 1000);
                                }
                            }, 1000);
                        }, 1000);
                    }
                }, 1000);
            }
        };

        window.runSequenceLoop = function() {
            if (window.isRunning) {
                window.runSequenceOnce();
            }
        };
    """)

    # Keep the browser open
    while True:
        time.sleep(1)

# Create the main window
root = tk.Tk()
root.title("Reporter")

# Create and pack the username entry
tk.Label(root, text="User you want to report").pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create and pack the Go button
go_button = tk.Button(root, text="Go", command=open_tiktok_profile)
go_button.pack()

# Start the GUI event loop
root.mainloop()
