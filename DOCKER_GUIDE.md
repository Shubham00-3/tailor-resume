# 🐳 Docker Deployment Guide

Complete guide for containerizing and deploying the Resume Tailor AI backend.

---

## 📦 What's Included

- ✅ **Dockerfile** - Production-ready backend container
- ✅ **docker-compose.yml** - Easy local deployment
- ✅ **.dockerignore** - Optimized build context
- ✅ **Health checks** - Container health monitoring
- ✅ **Non-root user** - Security best practices

---

## 🚀 Quick Start

### **Option 1: Docker Compose (Recommended)**

```powershell
# 1. Make sure .env file exists with GROQ_API_KEY
cp .env.example .env
# Edit .env and add your GROQ_API_KEY

# 2. Build and run
docker-compose up --build

# 3. Access the API
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

**To stop:**
```powershell
docker-compose down
```

### **Option 2: Docker CLI**

```powershell
# 1. Build the image
docker build -t resume-tailor-ai .

# 2. Run the container
docker run -d \
  -p 8000:8000 \
  -e GROQ_API_KEY=your_groq_api_key_here \
  -e MODEL_NAME=llama-3.3-70b-versatile \
  --name resume-tailor \
  resume-tailor-ai

# 3. Check logs
docker logs -f resume-tailor

# 4. Stop the container
docker stop resume-tailor
docker rm resume-tailor
```

---

## 🏗️ Build Commands

### **Build the Image**

```powershell
# Basic build
docker build -t resume-tailor-ai .

# Build with specific tag
docker build -t resume-tailor-ai:v1.0.0 .

# Build with no cache (fresh build)
docker build --no-cache -t resume-tailor-ai .

# Build with progress
docker build --progress=plain -t resume-tailor-ai .
```

### **Check Build Size**

```powershell
docker images resume-tailor-ai
```

Expected size: ~400-600 MB

---

## 🎯 Run Commands

### **Run in Detached Mode**

```powershell
docker run -d \
  --name resume-tailor \
  -p 8000:8000 \
  -e GROQ_API_KEY=gsk_your_key_here \
  -e MODEL_NAME=llama-3.3-70b-versatile \
  resume-tailor-ai
```

### **Run with Environment File**

```powershell
# Using .env file
docker run -d \
  --name resume-tailor \
  -p 8000:8000 \
  --env-file .env \
  resume-tailor-ai
```

### **Run in Interactive Mode (for debugging)**

```powershell
docker run -it \
  --name resume-tailor \
  -p 8000:8000 \
  -e GROQ_API_KEY=gsk_your_key_here \
  resume-tailor-ai
```

### **Run with Volume Mount (for development)**

```powershell
docker run -d \
  --name resume-tailor \
  -p 8000:8000 \
  -e GROQ_API_KEY=gsk_your_key_here \
  -v ${PWD}/app:/app/app \
  resume-tailor-ai
```

---

## 📊 Management Commands

### **View Running Containers**

```powershell
docker ps
```

### **View All Containers**

```powershell
docker ps -a
```

### **View Logs**

```powershell
# Follow logs in real-time
docker logs -f resume-tailor

# Last 100 lines
docker logs --tail 100 resume-tailor

# With timestamps
docker logs -t resume-tailor
```

### **Execute Commands in Container**

```powershell
# Open bash shell
docker exec -it resume-tailor bash

# Run Python command
docker exec -it resume-tailor python -c "print('Hello from container')"

# Check Python version
docker exec -it resume-tailor python --version
```

### **Health Check Status**

```powershell
docker inspect --format='{{.State.Health.Status}}' resume-tailor
```

### **Resource Usage**

```powershell
docker stats resume-tailor
```

---

## 🐙 Push to Docker Hub

### **Step 1: Create Docker Hub Account**

Visit: https://hub.docker.com/signup

### **Step 2: Login**

```powershell
docker login
# Enter your Docker Hub username and password
```

### **Step 3: Tag Your Image**

```powershell
# Tag for Docker Hub (replace YOUR_USERNAME)
docker tag resume-tailor-ai YOUR_USERNAME/resume-tailor-ai:latest
docker tag resume-tailor-ai YOUR_USERNAME/resume-tailor-ai:v1.0.0
```

### **Step 4: Push to Docker Hub**

```powershell
# Push latest tag
docker push YOUR_USERNAME/resume-tailor-ai:latest

# Push specific version
docker push YOUR_USERNAME/resume-tailor-ai:v1.0.0
```

### **Step 5: Pull and Run from Docker Hub**

```powershell
# Pull the image
docker pull YOUR_USERNAME/resume-tailor-ai:latest

# Run it
docker run -d \
  -p 8000:8000 \
  -e GROQ_API_KEY=your_key \
  YOUR_USERNAME/resume-tailor-ai:latest
```

---

## 📦 Push to GitHub Container Registry

### **Step 1: Create Personal Access Token**

1. Go to GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select scopes: `write:packages`, `read:packages`, `delete:packages`
4. Copy the token

### **Step 2: Login to GHCR**

```powershell
# Login to GitHub Container Registry
echo YOUR_TOKEN | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
```

### **Step 3: Tag for GHCR**

```powershell
# Tag for GitHub Container Registry
docker tag resume-tailor-ai ghcr.io/YOUR_GITHUB_USERNAME/resume-tailor-ai:latest
docker tag resume-tailor-ai ghcr.io/YOUR_GITHUB_USERNAME/resume-tailor-ai:v1.0.0
```

### **Step 4: Push to GHCR**

```powershell
# Push to GitHub Container Registry
docker push ghcr.io/YOUR_GITHUB_USERNAME/resume-tailor-ai:latest
docker push ghcr.io/YOUR_GITHUB_USERNAME/resume-tailor-ai:v1.0.0
```

### **Step 5: Make Package Public (Optional)**

1. Go to GitHub → Your Profile → Packages
2. Click on `resume-tailor-ai`
3. Package settings → Change visibility → Public

### **Step 6: Pull and Run from GHCR**

```powershell
# Pull from GHCR
docker pull ghcr.io/YOUR_GITHUB_USERNAME/resume-tailor-ai:latest

# Run it
docker run -d \
  -p 8000:8000 \
  -e GROQ_API_KEY=your_key \
  ghcr.io/YOUR_GITHUB_USERNAME/resume-tailor-ai:latest
```

---

## 🔍 Debugging

### **Common Issues**

**Issue 1: Build fails**
```powershell
# Check build logs
docker build --progress=plain -t resume-tailor-ai .

# Remove cached layers
docker build --no-cache -t resume-tailor-ai .
```

**Issue 2: Container exits immediately**
```powershell
# Check logs
docker logs resume-tailor

# Run in interactive mode
docker run -it resume-tailor-ai
```

**Issue 3: Port already in use**
```powershell
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process
taskkill /PID <process_id> /F

# Or use a different port
docker run -p 8001:8000 -e GROQ_API_KEY=key resume-tailor-ai
```

**Issue 4: GROQ_API_KEY not found**
```powershell
# Make sure to pass the env variable
docker run -e GROQ_API_KEY=your_actual_key resume-tailor-ai

# Or use .env file
docker run --env-file .env resume-tailor-ai
```

### **Inspect Container**

```powershell
# Container details
docker inspect resume-tailor

# Environment variables
docker inspect --format='{{.Config.Env}}' resume-tailor

# Network settings
docker inspect --format='{{.NetworkSettings.IPAddress}}' resume-tailor
```

---

## 🧹 Cleanup

### **Remove Container**

```powershell
# Stop and remove
docker stop resume-tailor
docker rm resume-tailor
```

### **Remove Image**

```powershell
docker rmi resume-tailor-ai
```

### **Clean Up Everything**

```powershell
# Stop all containers
docker stop $(docker ps -aq)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

# Remove unused data
docker system prune -a
```

---

## 📝 Docker Compose Commands

### **Build and Run**

```powershell
# Build and run in detached mode
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### **Rebuild Specific Service**

```powershell
docker-compose up -d --build resume-tailor-api
```

### **Scale Services**

```powershell
# Run multiple instances
docker-compose up -d --scale resume-tailor-api=3
```

---

## 🔐 Production Deployment

### **Best Practices:**

1. **Use specific tags, not `latest`**
   ```powershell
   docker tag resume-tailor-ai:v1.0.0
   ```

2. **Set resource limits**
   ```yaml
   services:
     resume-tailor-api:
       deploy:
         resources:
           limits:
             cpus: '1'
             memory: 512M
   ```

3. **Use secrets for sensitive data**
   ```powershell
   docker secret create groq_api_key ./groq_key.txt
   ```

4. **Enable restart policy**
   ```yaml
   restart: unless-stopped
   ```

5. **Monitor with health checks**
   Already configured in Dockerfile!

---

## 📊 Example Deployment Workflow

### **Full Workflow:**

```powershell
# 1. Build the image
docker build -t resume-tailor-ai:v1.0.0 .

# 2. Test locally
docker run -d \
  --name test-resume-tailor \
  -p 8000:8000 \
  -e GROQ_API_KEY=your_key \
  resume-tailor-ai:v1.0.0

# 3. Test the API
curl http://localhost:8000/health

# 4. Tag for registry
docker tag resume-tailor-ai:v1.0.0 YOUR_USERNAME/resume-tailor-ai:v1.0.0
docker tag resume-tailor-ai:v1.0.0 YOUR_USERNAME/resume-tailor-ai:latest

# 5. Push to Docker Hub
docker push YOUR_USERNAME/resume-tailor-ai:v1.0.0
docker push YOUR_USERNAME/resume-tailor-ai:latest

# 6. Deploy on production server
ssh user@production-server
docker pull YOUR_USERNAME/resume-tailor-ai:latest
docker run -d \
  --name resume-tailor \
  -p 8000:8000 \
  -e GROQ_API_KEY=production_key \
  --restart unless-stopped \
  YOUR_USERNAME/resume-tailor-ai:latest
```

---

## 🎯 Quick Reference

| Command | Description |
|---------|-------------|
| `docker build -t name .` | Build image |
| `docker run -d name` | Run detached |
| `docker ps` | List running containers |
| `docker logs -f name` | Follow logs |
| `docker exec -it name bash` | Enter container |
| `docker stop name` | Stop container |
| `docker rm name` | Remove container |
| `docker rmi name` | Remove image |
| `docker-compose up -d` | Start services |
| `docker-compose down` | Stop services |

---

## ✅ Checklist

Before deploying to production:

- [ ] `.env` file configured with valid GROQ_API_KEY
- [ ] Docker image builds successfully
- [ ] Container starts without errors
- [ ] Health check passes (`/health` endpoint)
- [ ] API documentation accessible (`/docs`)
- [ ] Test `/tailor` endpoint works
- [ ] Logs show no errors
- [ ] Image tagged with version number
- [ ] Pushed to container registry
- [ ] Production environment variables set

---

## 📞 Support

**Issues?**
- Check logs: `docker logs resume-tailor`
- Health status: `docker inspect --format='{{.State.Health.Status}}' resume-tailor`
- GitHub Issues: https://github.com/Shubham00-3/tailor-resume/issues

---

**Your backend is now fully Dockerized and ready for deployment!** 🚀

