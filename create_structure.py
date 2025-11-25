import os

# Define the folder structure
structure = {
    "GenAI-Architect-Roadmap": [
        "README.md",
        "roadmap.pdf",
        ".gitignore",
        {
            "phases": [
                {
                    "phase-01-core-foundations": [
                        {
                            "month-1-python-ml": [
                                "notebooks/",
                                "assignments/",
                                "code/",
                                {
                                    "mini-project-ml-workbench": [
                                        "notebooks/",
                                        "src/",
                                        "api/",
                                        "docker/",
                                        "datasets/"
                                    ]
                                }
                            ]
                        },
                        {
                            "month-2-deep-learning-transformers": [
                                "notebooks/",
                                "assignments/",
                                "code/",
                                {
                                    "project-transformer-workbench": [
                                        "notebooks/",
                                        "src/",
                                        "models/",
                                        "api/",
                                        "datasets/"
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "phase-02-genai-engineering-core": [
                        {
                            "month-3-embeddings-rag": [
                                "notebooks/",
                                "assignments/",
                                "vector-dbs/",
                                "code/",
                                {
                                    "project-basic-rag-system": [
                                        "src/",
                                        "notebooks/",
                                        "api/",
                                        "datasets/"
                                    ]
                                }
                            ]
                        },
                        {
                            "month-4-advanced-rag": [
                                "notebooks/",
                                "assignments/",
                                "code/",
                                "advanced-patterns/",
                                "graph-rag/",
                                {
                                    "project-enterprise-rag": [
                                        "src/",
                                        "pipelines/",
                                        "api/",
                                        "notebooks/",
                                        "dashboards/"
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "phase-03-llmops-production": [
                        {
                            "month-8a-llmops-evaluation": [
                                "notebooks/",
                                "assignments/",
                                "mlflow/",
                                "wandb/",
                                "ragas/",
                                "deepeval/",
                                "langsmith/",
                                "cost-optimization/",
                                "dashboards/"
                            ]
                        },
                        {
                            "month-8b-local-llms": [
                                "notebooks/",
                                "assignments/",
                                "ollama/",
                                "llamacpp/",
                                "quantization/",
                                {
                                    "project-private-llm-platform": [
                                        "src/",
                                        "environments/",
                                        "api/",
                                        "datasets/"
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "phase-04-multimodal": [
                        "vision/",
                        "audio/",
                        "video/",
                        "multimodal-embeddings/",
                        "image-generation/",
                        "document-intelligence/",
                        {
                            "project-multimodal-platform": [
                                "notebooks/",
                                "src/",
                                "api/",
                                "datasets/"
                            ]
                        }
                    ]
                },
                {
                    "phase-05-finetuning-training": [
                        "notebooks/",
                        "assignments/",
                        "datasets/",
                        "lora/",
                        "qlora/",
                        "rlhf/",
                        "dpo/",
                        {
                            "project-llm-factory": [
                                "data-pipeline/",
                                "training/",
                                "evaluation/",
                                "api/",
                                "models/",
                                "datasets/"
                            ]
                        }
                    ]
                },
                {
                    "phase-06-mcp-tools": [
                        "notebooks/",
                        "assignments/",
                        "servers/",
                        "tools/",
                        "security/",
                        {
                            "project-mcp-ecosystem": [
                                "servers/",
                                "gateway/",
                                "monitoring/",
                                "api/"
                            ]
                        }
                    ]
                },
                {
                    "phase-07-agentic-ai": [
                        "notebooks/",
                        "assignments/",
                        "langchain-agents/",
                        "crewai/",
                        "autogen/",
                        "llamaindex-agents/",
                        {
                            "project-multi-agent-team": [
                                "agents/",
                                "memory/",
                                "workflows/",
                                "api/",
                                "datasets/"
                            ]
                        }
                    ]
                },
                {
                    "phase-08-inference-serving": [
                        "notebooks/",
                        "assignments/",
                        "vllm/",
                        "tgi/",
                        "triton/",
                        "ray-serve/",
                        "quantization/",
                        {
                            "project-high-perf-serving": [
                                "src/",
                                "routing/",
                                "caching/",
                                "api/",
                                "dashboards/"
                            ]
                        }
                    ]
                },
                {
                    "phase-09-vector-databases": [
                        "notebooks/",
                        "assignments/",
                        "pinecone/",
                        "qdrant/",
                        "weaviate/",
                        "milvus/",
                        "pgvector/",
                        "elasticsearch/",
                        {
                            "project-distributed-vector-search": [
                                "src/",
                                "pipelines/",
                                "api/",
                                "dashboards/"
                            ]
                        }
                    ]
                },
                {
                    "phase-10-kubernetes-deployment": [
                        "notebooks/",
                        "assignments/",
                        "docker/",
                        "k8s-core/",
                        "monitoring/",
                        "autoscaling/",
                        "istio/",
                        "helm/",
                        "cicd/",
                        {
                            "project-k8s-genai-platform": [
                                "manifests/",
                                "charts/",
                                "pipelines/",
                                "dashboards/"
                            ]
                        }
                    ]
                },
                {
                    "phase-11-fastapi-microservices": [
                        "notebooks/",
                        "assignments/",
                        "fastapi-core/",
                        "auth/",
                        "security/",
                        "microservices/",
                        "streaming/",
                        "kafka/",
                        "redis-streams/",
                        {
                            "project-genai-microservices-platform": [
                                "services/",
                                "apis/",
                                "orchestrator/",
                                "gateway/",
                                "monitoring/",
                                "docker/"
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

# Function to create the folder structure
def create_structure(base_path, structure):
    for item in structure:
        if isinstance(item, str):
            # Create a file or folder
            if item.endswith("/"):
                os.makedirs(os.path.join(base_path, item), exist_ok=True)
            else:
                open(os.path.join(base_path, item), 'a').close()
        elif isinstance(item, dict):
            for folder, sub_structure in item.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                create_structure(folder_path, sub_structure)

# Create the structure
base_directory = "GenAI-Architect-Roadmap"
create_structure(".", structure[base_directory])