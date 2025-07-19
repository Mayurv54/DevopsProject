# DevOps Project

This is a simple DevOps pipeline project demonstrating CI/CD automation using *Jenkins, **Docker, and **Docker Compose*. The application is containerized and deployed locally using Docker Compose.

---

## 🚀 Project Features

- GitHub integrated CI/CD pipeline using Jenkins
- Dockerfile for application containerization
- Docker Compose for multi-container orchestration
- API test automation using curl or Postman (can be extended)
- DockerHub integration for image push

---

## 🧰 Tech Stack

- Jenkins
- Git & GitHub
- Docker & Docker Compose
- Bash Shell Scripts
- (Optional) Node.js / Python / Java (based on app)
- (Optional) Postman / REST Assured for API testing

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

bash
git clone https://github.com/Mayurv54/DevopsProject.git
cd DevopsProject
`

### 2. Build Docker Image

bash
docker build -t devops-app .


### 3. Run with Docker Compose

bash
docker-compose up -d


### 4. Test API Endpoint

bash
curl http://localhost:5000/your-endpoint


---

## 📦 Jenkins Pipeline Steps

1. *Clone Repository*
2. *Build Docker Image*
3. *Run Docker Compose*
4. *API Testing*
5. *Push Docker Image to DockerHub*

---

## 🔐 Jenkins Credentials Used

* *GitHub PAT* for private repo access (recommended)
* *DockerHub username/password* (stored in Jenkins credentials)

---

## 📸 Sample Pipeline Output

text
[Pipeline] git
Fetching changes from the remote Git repository
...
[Pipeline] sh
docker build -t devops-app .
...
[Pipeline] sh
curl http://localhost:5000/your-endpoint


---

## 📁 Project Structure


DevopsProject/
│
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── README.md
└── src/ or app/        # Your application code (optional)


---

## 📤 DockerHub Image (Optional)

Push your image to DockerHub using:

bash
docker tag devops-app your-dockerhub-username/devops-app:latest
docker push your-dockerhub-username/devops-app:latest


---

## 🤝 Contribution

Feel free to fork this repository, raise issues or submit PRs.

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Author

* [Mayur V] (https://github.com/Mayurv54)
* [Bhagyavan]
