# 🚀 Skypass Website Deployment Guide

## Publishing skypassvisas.com for FREE using GitHub Pages

This guide will help you deploy your Skypass Visa Services website to your domain **skypassvisas.com** completely free.

---

## 📋 Prerequisites

- [x] Git installed (already done ✓)
- [ ] GitHub account (free) - Create at https://github.com/signup
- [ ] Access to your domain registrar (where you bought skypassvisas.com)

---

## 🎯 Step-by-Step Deployment

### **Step 1: Create GitHub Repository**

1. Go to https://github.com/new
2. Repository name: `skypass-website` (or any name you prefer)
3. Set to **Public** (required for free GitHub Pages)
4. **DO NOT** initialize with README, .gitignore, or license
5. Click **Create repository**

### **Step 2: Push Your Code to GitHub**

Run these commands in your terminal (already in `/Users/amal/Skypass`):

```bash
# Add all files to git
git add .

# Commit the files
git commit -m "Initial commit - Skypass Visa Services website"

# Add your GitHub repository as remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/skypass-website.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Note:** Replace `YOUR_USERNAME` with your actual GitHub username.

### **Step 3: Enable GitHub Pages**

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under "Source", select **main** branch
5. Click **Save**
6. Wait 1-2 minutes for deployment

Your site will be live at: `https://YOUR_USERNAME.github.io/skypass-website/`

### **Step 4: Configure Custom Domain (skypassvisas.com)**

#### A. On GitHub:
1. Still in **Settings → Pages**
2. Under "Custom domain", enter: `skypassvisas.com`
3. Click **Save**
4. Check **Enforce HTTPS** (wait a few minutes if not available yet)

#### B. On Your Domain Registrar:

You need to add DNS records. Log in to where you bought **skypassvisas.com** (GoDaddy, Namecheap, Google Domains, etc.)

**Add these DNS records:**

| Type  | Name/Host | Value/Points to              | TTL  |
|-------|-----------|------------------------------|------|
| A     | @         | 185.199.108.153              | 3600 |
| A     | @         | 185.199.109.153              | 3600 |
| A     | @         | 185.199.110.153              | 3600 |
| A     | @         | 185.199.111.153              | 3600 |
| CNAME | www       | YOUR_USERNAME.github.io      | 3600 |

**Replace `YOUR_USERNAME` with your GitHub username!**

**Example:**
If your GitHub username is `amaldev`, the CNAME record should point to: `amaldev.github.io`

### **Step 5: Wait for DNS Propagation**

- DNS changes can take **5 minutes to 48 hours** (usually 15-30 minutes)
- Check status at: https://www.whatsmydns.net/#A/skypassvisas.com
- Once propagated, your site will be live at **https://skypassvisas.com** 🎉

---

## 🔄 How to Update Your Website

Whenever you make changes to your website:

```bash
# Save your changes in your code editor first, then:
git add .
git commit -m "Description of changes"
git push
```

GitHub Pages will automatically rebuild and deploy in 1-2 minutes!

---

## 🆓 Alternative Free Hosting Options

If you prefer not to use GitHub Pages, here are other excellent free options:

### **Option 2: Netlify (Easiest)**
1. Go to https://netlify.com
2. Sign up for free
3. Drag and drop your `/Users/amal/Skypass` folder
4. Configure custom domain in Netlify settings
5. Update DNS at your registrar to point to Netlify

**DNS for Netlify:**
- Add CNAME record: `www` → `YOUR_SITE.netlify.app`
- Add A record: `@` → (Netlify will provide IP)

### **Option 3: Vercel**
1. Go to https://vercel.com
2. Sign up with GitHub
3. Import your repository
4. Add custom domain in project settings
5. Follow Vercel's DNS instructions

### **Option 4: Cloudflare Pages**
1. Go to https://pages.cloudflare.com
2. Connect your GitHub repository
3. Deploy automatically
4. Add custom domain (especially easy if domain is on Cloudflare)

---

## 📞 Need Help?

### Common Issues:

**"Site not loading after DNS change"**
- Wait longer (DNS can take up to 48 hours)
- Clear browser cache (Cmd+Shift+R on Mac)
- Try incognito mode

**"HTTPS not working"**
- Wait 24 hours after DNS propagation
- Make sure "Enforce HTTPS" is checked in GitHub Pages settings

**"404 error"**
- Make sure `index.html` is in the root of your repository
- Check that GitHub Pages is enabled and set to `main` branch

### Video Tutorials:
- GitHub Pages: https://www.youtube.com/results?search_query=github+pages+custom+domain
- Netlify Deploy: https://www.youtube.com/results?search_query=netlify+custom+domain

---

## ✅ Checklist

- [ ] Create GitHub account
- [ ] Create repository
- [ ] Push code to GitHub
- [ ] Enable GitHub Pages
- [ ] Configure custom domain on GitHub
- [ ] Update DNS records at domain registrar
- [ ] Wait for DNS propagation
- [ ] Enable HTTPS
- [ ] Test website at skypassvisas.com

---

## 🎉 Success!

Once complete, your website will be:
- ✅ Live at **https://skypassvisas.com**
- ✅ Secured with free SSL certificate
- ✅ Hosted on fast global CDN
- ✅ 100% FREE forever
- ✅ Automatically deployed on every update

---

**Created:** January 4, 2026
**Website:** Skypass Visa Services
**Domain:** skypassvisas.com
