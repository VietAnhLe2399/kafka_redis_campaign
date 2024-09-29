# kafka_redis_campaign
Các bước chạy code:
### 1. Cài docker. Nếu không có docker, cần tự cài kafka, zookeeper, redis
### 2. Chạy file docker-compose.yaml để pull image và start container.
Một số lệnh với docker:
- Start tất cả container trong docker-compose: ```docker-compose up -d```. Câu này cần chạy ngay lúc đầu.
- Stop tất cả container trong docker-compose (chạy khi đã làm việc xong, tắt cho đỡ tốn tài nguyên): ```docker-compose down```
- Check trạng thái của các container. Nếu không hiện đủ 3 container thì có lỗi gì đó: ```docker ps```
- Xem log của container: ```docker logs <container_id>```
- Stop container: ```docker stop <container_id>```
- Start container: ```docker start <container_id>```
### 3. Cài các lib cần dùng:
```pip install -r requirements.txt```
### 4. Chạy file utils/kafka_producer.py nếu cần test data mới. Liên tục refresh data mới nếu cần.
### 5. Chạy service theo 2 cách.
#### 5.1. Flask app
- Chạy file app.py: ```python app.py```
- Để bắt đầu consume, vào browser tại: http://localhost:5000/consume

#### 5.2. Kafka consumer với pure python
- Chạy file: ```python pure_python.py```

### 6. **Cố lên nhé các bạn!**