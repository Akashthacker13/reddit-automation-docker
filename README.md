# Reddit Automation with Docker 🤖

Automate Reddit posting, commenting, and engagement using Selenium and Docker. Perfect for marketing automation, content distribution, and community engagement at scale.

## ✨ Features

- 🔐 **Secure Login** - Automated Reddit authentication
- 📝 **Auto Posting** - Create text posts in multiple subreddits
- 💬 **Auto Commenting** - Comment on specific posts
- ⬆️ **Auto Upvoting** - Upvote posts automatically
- 🐳 **Docker Ready** - Containerized for easy deployment
- 📦 **Multi-Account Support** - Run multiple accounts in parallel
- 🔒 **Headless Mode** - Runs in background without GUI

## 🚀 Quick Start

### Prerequisites

- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Reddit account(s) with 50+ karma recommended
- Git (optional)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Akashthacker13/reddit-automation-docker.git
cd reddit-automation-docker
```

2. **Create .env file**
```bash
cp .env.example .env
```

3. **Edit .env with your credentials**
```bash
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
```

4. **Build Docker image**
```bash
docker build -t reddit-bot .
```

5. **Run the bot**
```bash
docker run --env-file .env reddit-bot
```

## 📖 Usage Examples

### Post to Multiple Subreddits

Edit `bot.py` to customize:

```python
subreddits = ['StockMarket', 'Trading', 'IndianStockMarket']
post_title = "Your Post Title"
post_content = "Your post content here"
```

### Comment on Posts

```python
bot.comment_on_post(
    post_url='https://reddit.com/r/test/comments/xyz',
    comment_text='Great post!'
)
```

### Upvote Posts

```python
bot.upvote_post('https://reddit.com/r/test/comments/xyz')
```

## 🔧 Configuration

### Customize Automation

Edit `bot.py` main() function:

```python
def main():
    bot = RedditBot()
    bot.login(username, password)
    
    # Your custom automation here
    bot.post_to_subreddit('test', 'Title', 'Content')
    
    bot.close()
```

### Timing Between Actions

Adjust delays to avoid rate limiting:

```python
time.sleep(600)  # 10 minutes between posts
```

## 🎯 Use Cases

### Marketing Automation
- Share blog posts across relevant subreddits
- Promote products/services
- Build brand awareness

### Community Engagement
- Respond to mentions
- Engage with specific keywords
- Build community presence

### Content Distribution
- Cross-post content
- Share updates automatically
- Schedule posts

## 🔐 Security Best Practices

1. **Never commit .env file** - Added to .gitignore
2. **Use strong passwords** - Enable 2FA on Reddit
3. **Respect rate limits** - Add delays between actions
4. **Follow Reddit TOS** - Use responsibly

## 📊 Multi-Account Setup

### Run Multiple Accounts

1. Create separate .env files:
```bash
.env.account1
.env.account2
.env.account3
```

2. Run multiple containers:
```bash
docker run --env-file .env.account1 --name bot1 reddit-bot
docker run --env-file .env.account2 --name bot2 reddit-bot
docker run --env-file .env.account3 --name bot3 reddit-bot
```

## 🐛 Troubleshooting

### Login Fails
- Check credentials in .env
- Verify 2FA is disabled or use app password
- Check for Reddit maintenance

### Container Exits Immediately
- Check Docker logs: `docker logs <container-id>`
- Verify .env file is properly formatted
- Ensure all dependencies installed

### Rate Limiting
- Increase delays between actions
- Use fewer accounts per IP
- Rotate IP addresses

## ⚠️ Important Notes

- **Reddit TOS**: Ensure your automation complies with [Reddit's Terms of Service](https://www.redditinc.com/policies/user-agreement)
- **Rate Limiting**: Reddit has rate limits. Add appropriate delays.
- **Karma Requirements**: Some subreddits require minimum karma to post.
- **Subreddit Rules**: Check individual subreddit rules before posting.

## 🛠️ Development

### Local Testing

```bash
python3 bot.py
```

### Debug Mode

Remove `--headless` from bot.py to see browser:

```python
# chrome_options.add_argument('--headless')  # Comment this line
```

## 📝 License

MIT License - See LICENSE file

## 🤝 Contributing

Pull requests welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open pull request

## 📧 Support

For issues or questions:
- Open an issue on GitHub
- Check existing issues first

## 🎯 Roadmap

- [ ] Add scheduling functionality
- [ ] Implement keyword monitoring
- [ ] Add analytics dashboard
- [ ] Support for image/video posts
- [ ] Integrate with APIs (n8n, Zapier)

---

**Built with ❤️ for Reddit marketing automation**

**Repository**: [github.com/Akashthacker13/reddit-automation-docker](https://github.com/Akashthacker13/reddit-automation-docker)
