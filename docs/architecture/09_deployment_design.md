# Deployment Design

## Model Serving

The trained model is deployed as a REST API using FastAPI.

## Infrastructure

- Hosted on :contentReference[oaicite:24]{index=24}
- Model artifacts loaded at runtime

## API Endpoints

- /predict → Returns stock price prediction

## Workflow

Client → API Request → Model Inference → Response

## Future Improvements

- CI/CD pipeline for automated deployment
- Containerization using Docker
- Deployment using managed services like SageMaker endpoints