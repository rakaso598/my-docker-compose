const express = require('express');
const axios = require('axios');
const app = express();
const PORT = 3000;

const SPRINGBOOT_API = 'http://userservice:8080/users'; // Spring Boot API URL
const PYTHON_CONTAINER_API = 'http://pythonbatch:5000/export'; // Python 컨테이너 API URL

app.use(express.static('public')); // 정적 파일 서빙
app.use(express.json());

// Spring Boot에서 데이터 가져오기
app.get('/api/get-data', async (req, res) => {
    try {
        const response = await axios.get(SPRINGBOOT_API);
        res.json(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to fetch data' });
    }
});

// Spring Boot에 데이터 추가하기
app.post('/api/add-data', async (req, res) => {
    try {
        const { name, email } = req.body;
        const response = await axios.post(SPRINGBOOT_API, { name, email });
        res.json(response.data);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to add data' });
    }
});

// Python 배치 작업 트리거
app.post('/api/export-data', async (req, res) => {
    try {
        // Python 서버에서 데이터를 가져옴
        const response = await axios.get(PYTHON_CONTAINER_API);

        if (response.data.file) {
            const fileName = response.data.file;

            // Python 서버에서 받은 파일 이름을 바탕으로 다운로드 URL 설정
            const downloadUrl = `http://pythonbatch:5000/export/${fileName}`;

            res.json({ message: "Export successful", fileUrl: downloadUrl });
        } else {
            res.status(404).json({ error: "No data to export" });
        }
    } catch (error) {
        console.error("Error triggering export:", error.message || error);
        res.status(500).json({ error: "Failed to trigger export" });
    }
});

app.listen(PORT, () => {
    console.log(`Node.js server running on port ${PORT}`);
});
