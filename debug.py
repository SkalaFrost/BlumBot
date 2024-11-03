import aiohttp
import asyncio
import json

async def fetch_data():
    url = "https://raw.githubusercontent.com/SkalaFrost/m-data/refs/heads/main/blum.json"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Kiểm tra phản hồi có phải JSON không
            if response.content_type == 'application/json':
                data = await response.json()
            else:
                # Nếu không phải JSON, giải mã theo text và chuyển đổi thành JSON
                text_data = await response.text()
                data = json.loads(text_data)
            print(data)

# Chạy hàm bất đồng bộ
asyncio.run(fetch_data())
