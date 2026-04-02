#!/usr/bin/env python3
"""
Weather Query Script - 天气查询脚本

使用 wttr.in API 查询任意城市天气（无需 API key）

用法：
    python query_weather.py 城市名
    python query_weather.py 北京
    python query_weather.py Shanghai
"""

import sys
import json
import urllib.request
import urllib.parse

def query_weather(city, format="j1", lang="zh"):
    """
    查询城市天气
    
    Args:
        city: 城市名（支持中文）
        format: 返回格式（j1=JSON 详细，3=简洁文本）
        lang: 语言（zh=中文）
    
    Returns:
        天气数据字典
    """
    # URL 编码城市名
    encoded_city = urllib.parse.quote(city)
    url = f"https://wttr.in/{encoded_city}?format={format}&lang={lang}"
    
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read().decode('utf-8')
            
            if format == "j1":
                return json.loads(data)
            else:
                return data.strip()
    except Exception as e:
        return {"error": str(e)}

def format_weather(data):
    """
    格式化天气数据为易读文本
    
    Args:
        data: wttr.in 返回的 JSON 数据
    
    Returns:
        格式化的天气文本
    """
    if "error" in data:
        return f"查询失败：{data['error']}"
    
    try:
        current = data["current_condition"][0]
        location = data["nearest_area"][0]
        
        # 提取位置信息
        city_name = location["areaName"][0]["value"]
        country = location["country"][0]["value"]
        
        # 当前天气
        temp_c = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        # 尝试获取中文描述，失败则用英文
        weather_desc = current.get("weatherDesc", [{}])[0].get("value", "Unknown")
        humidity = current["humidity"]
        wind_dir = current["winddir16Point"]
        wind_speed = current["windspeedKmph"]
        
        # 构建输出
        output = []
        output.append(f"🌤️ {city_name} ({country}) 当前天气")
        output.append("")
        output.append(f"🌡️ 温度：{temp_c}°C（体感 {feels_like}°C）")
        output.append(f"☀️  状况：{weather_desc}")
        output.append(f"💨 风力：{wind_dir} {wind_speed}km/h")
        output.append(f"💧 湿度：{humidity}%")
        output.append("")
        
        # 3 天预报
        if "weather" in data:
            output.append("📅 3 天预报：")
            for day in data["weather"][:3]:
                date = day["date"]
                max_temp = day["maxtempC"]
                min_temp = day["mintempC"]
                desc = day["hourly"][0].get("weatherDesc", [{}])[0].get("value", "Unknown")
                output.append(f"- {date}: {desc} {max_temp}°C/{min_temp}°C")
        
        return "\n".join(output)
    
    except Exception as e:
        return f"格式化失败：{str(e)}"

def main():
    if len(sys.argv) < 2:
        print("用法：python query_weather.py 城市名")
        print("示例：python query_weather.py 北京")
        print("      python query_weather.py Shanghai")
        sys.exit(1)
    
    city = sys.argv[1]
    print(f"正在查询 {city} 的天气...\n")
    
    # 查询天气
    data = query_weather(city, format="j1")
    
    # 格式化输出
    result = format_weather(data)
    print(result)

if __name__ == "__main__":
    main()
