#!/usr/bin/env python3
"""
天气查询脚本 - Weather Query Script

功能：使用 wttr.in API 查询任意城市天气（无需 API key）
作者：Weather Query Skill
创建时间：2026-03-16

使用方法：
    python query_weather.py 城市名
    
示例：
    python query_weather.py 北京
    python query_weather.py Shanghai
"""

# 导入需要的模块
import sys  # 用于处理命令行参数
import json  # 用于处理 JSON 数据
import urllib.request  # 用于发送网络请求
import urllib.parse  # 用于处理 URL 编码


def query_weather(city, format="j1", lang="zh"):
    """
    查询城市天气的核心函数
    
    参数说明：
        city (str): 城市名，支持中文（如"北京"）或英文（如"Beijing"）
        format (str): 返回格式
            - "j1": JSON 格式，包含详细数据（推荐）
            - "3": 简洁文本格式
        lang (str): 语言设置
            - "zh": 中文
            - "en": 英文
    
    返回值：
        dict 或 str: 天气数据
            - 如果 format="j1"，返回字典（dict）
            - 如果 format="3"，返回字符串（str）
            - 如果出错，返回包含错误信息的字典 {"error": "错误信息"}
    """
    
    # 步骤 1：对城市名进行 URL 编码
    # 例如：北京 → %E5%8C%97%E4%BA%AC
    # 这样特殊字符（如空格、中文）才能正确传输
    encoded_city = urllib.parse.quote(city)
    
    # 步骤 2：构建完整的 API 请求 URL
    # 例如：https://wttr.in/%E5%8C%97%E4%BA%AC？format=j1&lang=zh
    url = f"https://wttr.in/{encoded_city}?format={format}&lang={lang}"
    
    # 步骤 3：发送网络请求并获取数据
    try:
        # 打开 URL，设置超时时间为 10 秒（防止网络卡住）
        with urllib.request.urlopen(url, timeout=10) as response:
            # 读取服务器返回的数据
            data = response.read().decode('utf-8')
            
            # 根据请求的格式返回不同类型的结果
            if format == "j1":
                # JSON 格式：解析成字典，方便后续处理
                return json.loads(data)
            else:
                # 文本格式：直接返回字符串
                return data.strip()
    
    # 步骤 4：错误处理
    # 如果网络请求失败（如网络断开、城市名错误等），捕获异常并返回错误信息
    except Exception as e:
        return {"error": str(e)}


def format_weather(data):
    """
    将天气数据格式化为易读的文本
    
    参数说明：
        data (dict): query_weather 函数返回的天气数据（JSON 格式）
    
    返回值：
        str: 格式化后的天气文本，包含 emoji 图标，方便阅读
    
    输出示例：
        🌤️ Beijing (China) 当前天气
        
        🌡️ 温度：14°C（体感 13°C）
        ☀️  状况：Sunny
        💨 风力：S 14km/h
        💧 湿度：24%
        
        📅 3 天预报：
        - 2026-03-16: Cloudy  14°C/6°C
        - 2026-03-17: Clear  16°C/5°C
        - 2026-03-18: Patchy rain nearby 12°C/5°C
    """
    
    # 步骤 1：检查是否有错误
    if "error" in data:
        return f"查询失败：{data['error']}"
    
    # 步骤 2：提取当前天气数据
    try:
        # current_condition 数组包含当前天气信息，取第一个元素
        current = data["current_condition"][0]
        
        # nearest_area 数组包含位置信息，取第一个元素
        location = data["nearest_area"][0]
        
        # 提取城市名和国家名
        city_name = location["areaName"][0]["value"]
        country = location["country"][0]["value"]
        
        # 步骤 3：提取当前天气详情
        temp_c = current["temp_C"]  # 当前温度（摄氏度）
        feels_like = current["FeelsLikeC"]  # 体感温度
        weather_desc = current.get("weatherDesc", [{}])[0].get("value", "Unknown")  # 天气描述
        humidity = current["humidity"]  # 湿度百分比
        wind_dir = current["winddir16Point"]  # 风向（如 N, S, NE 等）
        wind_speed = current["windspeedKmph"]  # 风速（公里/小时）
        
        # 步骤 4：构建输出文本
        output = []  # 用列表存储每一行文本
        
        # 添加标题行：城市名和国家
        output.append(f"🌤️ {city_name} ({country}) 当前天气")
        output.append("")  # 空行，增加可读性
        
        # 添加当前天气详情
        output.append(f"🌡️ 温度：{temp_c}°C（体感 {feels_like}°C）")
        output.append(f"☀️  状况：{weather_desc}")
        output.append(f"💨 风力：{wind_dir} {wind_speed}km/h")
        output.append(f"💧 湿度：{humidity}%")
        output.append("")  # 空行
        
        # 步骤 5：添加 3 天预报
        if "weather" in data:
            output.append("📅 3 天预报：")
            
            # 遍历前 3 天的预报数据
            for day in data["weather"][:3]:
                date = day["date"]  # 日期（格式：YYYY-MM-DD）
                max_temp = day["maxtempC"]  # 最高温度
                min_temp = day["mintempC"]  # 最低温度
                desc = day["hourly"][0].get("weatherDesc", [{}])[0].get("value", "Unknown")  # 天气描述
                
                # 添加每天的预报信息
                output.append(f"- {date}: {desc} {max_temp}°C/{min_temp}°C")
        
        # 步骤 6：用换行符连接所有行，形成完整的文本
        return "\n".join(output)
    
    # 步骤 7：错误处理
    # 如果数据格式不对或缺少字段，返回错误信息
    except Exception as e:
        return f"格式化失败：{str(e)}"


def main():
    """
    主函数 - 程序的入口点
    
    功能：
        1. 检查命令行参数
        2. 调用查询函数获取天气
        3. 格式化并输出结果
    """
    
    # 步骤 1：检查命令行参数
    # sys.argv 是一个列表，包含所有命令行参数
    # sys.argv[0] 是脚本名（query_weather.py）
    # sys.argv[1] 是第一个参数（城市名）
    if len(sys.argv) < 2:
        # 如果用户没有提供城市名，显示使用说明
        print("用法：python query_weather.py 城市名")
        print("示例：python query_weather.py 北京")
        print("      python query_weather.py Shanghai")
        sys.exit(1)  # 退出程序，返回错误码
    
    # 步骤 2：获取用户输入的城市名
    city = sys.argv[1]
    print(f"正在查询 {city} 的天气...\n")
    
    # 步骤 3：调用查询函数获取天气数据
    # format="j1" 表示获取 JSON 格式的详细数据
    data = query_weather(city, format="j1")
    
    # 步骤 4：调用格式化函数，将数据转换为易读的文本
    result = format_weather(data)
    
    # 步骤 5：输出结果
    print(result)


# 步骤 6：程序入口判断
# 这行代码确保只有直接运行此脚本时才会执行 main() 函数
# 如果被其他程序导入，不会自动执行
if __name__ == "__main__":
    main()
