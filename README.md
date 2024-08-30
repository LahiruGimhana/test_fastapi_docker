# execute host files from docker container

docker build -t fastapi-server .

docker run -d -p 8500:8500 --name fastapi-container fastapi-server


docker run -d -p 8500:8500 \
  -v /home/Gimhana/Test/sample:/scripts \
  --name fastapi-container fastapi-server

















--------------------------------------------------------
# create run.sh files those locations
/home/Gimhana/TT/T1/run.sh
/home/Gimhana/TT/T2/run.sh
/home/Gimhana/TT/T3/run.sh

chmod +x run.sh



#
curl -X POST "http://localhost:8500/execute-script/" -H "Content-Type: application/json" -d '{"file_path": "/scripts/T1/run.sh"}'

#
curl -X POST "http://localhost:8500/execute-script/" -H "Content-Type: application/json" -d '{"file_path": "/scripts/T2/run.sh"}'
