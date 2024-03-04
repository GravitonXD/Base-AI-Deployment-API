FROM python:3.11-slim

# Add files into the container
COPY requirements.txt /breadcrumbs/requirements.txt
COPY api /breadcrumbs/api
COPY db /breadcrumbs/db
COPY ai_processor /breadcrumbs/ai_processor

# Working Directory
WORKDIR /breadcrumbs

# Setup Python Paths
ENV PYTHONPATH "${PYTHONPATH}:/breadcrumbs"

# Run the following commands on build
RUN pip install --upgrade pip
RUN pip3 --timeout=1000 install -r /breadcrumbs/requirements.txt


# Execute the following command on container startup
CMD ["echo", "API Container Running..."]