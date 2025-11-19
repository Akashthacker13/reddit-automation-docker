from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv()

class RedditBot:
    def __init__(self):
        # Docker-friendly Chrome setup
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        
    def login(self, username, password):
        """Login to Reddit"""
        try:
            self.driver.get('https://www.reddit.com/login')
            time.sleep(3)
            
            # Find and fill username
            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, 'loginUsername'))
            )
            username_field.send_keys(username)
            
            # Find and fill password
            password_field = self.driver.find_element(By.ID, 'loginPassword')
            password_field.send_keys(password)
            
            # Click login button
            login_btn = self.driver.find_element(By.XPATH, '//button[contains(text(), "Log In")]')
            login_btn.click()
            
            time.sleep(5)
            print(f"✅ Successfully logged in as {username}")
            return True
        except Exception as e:
            print(f"❌ Login failed: {e}")
            return False
    
    def post_to_subreddit(self, subreddit, title, content):
        """Create a text post in a subreddit"""
        try:
            self.driver.get(f'https://www.reddit.com/r/{subreddit}/submit')
            time.sleep(3)
            
            # Click on text post tab
            text_tab = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Text")]'))
            )
            text_tab.click()
            time.sleep(2)
            
            # Fill title
            title_field = self.driver.find_element(By.CSS_SELECTOR, 'textarea[placeholder*="Title"]')
            title_field.send_keys(title)
            
            # Fill content
            content_field = self.driver.find_element(By.CSS_SELECTOR, 'div[contenteditable="true"]')
            content_field.send_keys(content)
            
            # Click post button
            post_btn = self.driver.find_element(By.XPATH, '//button[contains(text(), "Post")]')
            post_btn.click()
            
            time.sleep(3)
            print(f"✅ Posted to r/{subreddit}: {title}")
            return True
        except Exception as e:
            print(f"❌ Failed to post to r/{subreddit}: {e}")
            return False
    
    def comment_on_post(self, post_url, comment_text):
        """Comment on a specific post"""
        try:
            self.driver.get(post_url)
            time.sleep(3)
            
            # Find comment box
            comment_box = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[contenteditable="true"]'))
            )
            comment_box.click()
            comment_box.send_keys(comment_text)
            
            # Click comment button
            comment_btn = self.driver.find_element(By.XPATH, '//button[contains(text(), "Comment")]')
            comment_btn.click()
            
            time.sleep(2)
            print(f"✅ Commented on post: {post_url}")
            return True
        except Exception as e:
            print(f"❌ Failed to comment: {e}")
            return False
    
    def upvote_post(self, post_url):
        """Upvote a post"""
        try:
            self.driver.get(post_url)
            time.sleep(2)
            
            upvote_btn = self.driver.find_element(By.CSS_SELECTOR, 'button[aria-label*="upvote"]')
            upvote_btn.click()
            
            print(f"✅ Upvoted post: {post_url}")
            return True
        except Exception as e:
            print(f"❌ Failed to upvote: {e}")
            return False
    
    def close(self):
        """Close the browser"""
        self.driver.quit()
        print("🔒 Browser closed")

# Main automation script
def main():
    # Get credentials from environment
    username = os.getenv('REDDIT_USERNAME')
    password = os.getenv('REDDIT_PASSWORD')
    
    if not username or not password:
        print("❌ Please set REDDIT_USERNAME and REDDIT_PASSWORD in .env file")
        return
    
    # Initialize bot
    bot = RedditBot()
    
    # Login
    if not bot.login(username, password):
        bot.close()
        return
    
    # Example: Post to multiple subreddits
    subreddits = ['test']  # Start with test subreddit
    post_title = "Testing automation"
    post_content = "This is an automated test post."
    
    for sub in subreddits:
        bot.post_to_subreddit(sub, post_title, post_content)
        time.sleep(600)  # 10 minutes between posts
    
    # Close browser
    bot.close()

if __name__ == "__main__":
    main()
