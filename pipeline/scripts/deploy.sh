poetry export -f requirements.txt > requirements.txt
docker-compose build
docker push cgarciae/test-pipeline:latest
python pipeline.py
kfp pipeline upload-version pipeline.yml -p c554c4c8-b672-4c0f-90d6-24e7132ee06c -v test-pipeline-$(date +%s)