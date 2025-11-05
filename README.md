# Menu creator

**Menu Creator** is a full-stack app packaged in Docker that uses local Artificial Intelligence (AI) to whip up menus and recipe ideas.

## Technologies

- **[FastAPI](https://fastapi.tiangolo.com/)**
- **[Vite](https://vite.dev/)**
- **[Vue](https://vuejs.org/)**
- **[Tailwind](https://tailwindcss.com/)** 
- **[MariaDB](https://mariadb.org/)**
- **[Ollama](https://ollama.com/)**
- **[Docker](https://www.docker.com/)**

## How to deploy

Install **Docker Desktop** (or similar software like OrbStack, Rancher Desktop etc) to create containers

Rename all `.example.env` files to `.env` to configure database credentials and port mappings

In the project root run the following command in your terminal

```bash
docker compose up -d --build
```

This will start four Docker containers

🖥️ **Web Application (Vite + Vue)**: http://localhost:8080

⚙️ **API (FastAPI)**: http://localhost:8000 (_to check available routes_)

🤖 **AI (Ollama)**: http://localhost:11434/api/tags (_to check installed models_)

- While we could pull different models during the Docker build, we prefer using a locally mounted version of the **Llama 3** model from **[Hugging Face](https://huggingface.co/)**. So, we need to download **Meta-Llama-3.1-8B-Instruct-Q5_K_M** from this **[link](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/tree/main)** and put it **[here](./ai/ollama_data)**

🗄️ **Database (MariaDB)**: Runs as a backend service with no UI. Can check example table and data **[here](./bbdd/init.sql)**

> [!NOTE]
> Responses from from Ollama's AI (llama3) may be slow. Keep in mind that this isn't a production application. If you were to deploy something similar in a real-world environment, I'd recommend using an AI with a faster API, like ChatGPT Pro or something similar.

> [!IMPORTANT]
> Bearer token for test is: **secret**

If you want to remove containers you can type this in your terminal

```bash
docker compose down
```
