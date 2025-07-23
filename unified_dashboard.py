# === CamboStationVision™ Unified Dashboard ===
# Multi-Page Sidebar Navigation | All Features Integrated

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import time
from datetime import datetime
import streamlit.components.v1 as components

# === Page Configuration ===
st.set_page_config(
    page_title="CamboStationVision™ - Trading Command Center",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# === Custom CSS Styling ===
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #00ff88;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,255,136,0.3);
    }
    .section-header {
        font-size: 1.5rem;
        color: #ff6b6b;
        border-bottom: 2px solid #ff6b6b;
        padding-bottom: 0.5rem;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .strategy-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# === Sidebar Navigation ===
st.sidebar.markdown("# 🚀 CamboStation")
st.sidebar.markdown("### Navigation Menu")

# Navigation options
pages = {
    "🏠 Dashboard Home": "home",
    "📈 Trading Charts": "charts", 
    "🧠 AI Analysis": "ai_analysis",
    "⚡ Strategy Lab": "strategies",
    "📚 Education Center": "education",
    "📰 News & Sentiment": "news",
    "🎯 Execution Center": "execution",
    "⚙️ Settings": "settings"
}

selected_page = st.sidebar.selectbox("Select Page", list(pages.keys()))
current_page = pages[selected_page]

# Sidebar Status Panel
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 System Status")
st.sidebar.success("🟢 All Systems Online")
st.sidebar.info(f"🕒 {datetime.now().strftime('%H:%M:%S')}")
st.sidebar.metric("Active Strategies", "4", "↗️ +1")

# === MAIN CONTENT AREA ===

# === HOME PAGE ===
if current_page == "home":
    st.markdown('<h1 class="main-header">🚀 CamboStationVision™ Command Center</h1>', unsafe_allow_html=True)
    
    # Quick Stats Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Portfolio Value", "$125,430", "↗️ +2.3%")
    with col2:
        st.metric("Active Positions", "7", "↗️ +2")
    with col3:
        st.metric("Win Rate", "73.2%", "↗️ +1.1%")
    with col4:
        st.metric("AI Confidence", "87%", "↗️ +5%")
    
    st.markdown("---")
    
    # Quick Access Panels
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">📈 Market Overview</div>', unsafe_allow_html=True)
        
        # Sample market data
        market_data = {
            "SPY": {"price": 421.17, "change": "+0.85%", "status": "🟢"},
            "QQQ": {"price": 367.23, "change": "-0.23%", "status": "🔴"},
            "IWM": {"price": 198.45, "change": "+1.12%", "status": "🟢"},
            "VIX": {"price": 18.67, "change": "-2.34%", "status": "🟢"}
        }
        
        for symbol, data in market_data.items():
            st.markdown(f"""
            <div class="metric-card">
                <strong>{symbol}</strong> {data['status']}<br>
                ${data['price']} ({data['change']})
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-header">🎯 Active Signals</div>', unsafe_allow_html=True)
        
        signals = [
            {"symbol": "AAPL", "signal": "BUY", "strength": "85%", "type": "Momentum"},
            {"symbol": "TSLA", "signal": "HOLD", "strength": "72%", "type": "AI Sentiment"},
            {"symbol": "NVDA", "signal": "BUY", "strength": "91%", "type": "Breakout"},
            {"symbol": "MSFT", "signal": "SELL", "strength": "68%", "type": "Mean Reversion"}
        ]
        
        for signal in signals:
            color = "🟢" if signal["signal"] == "BUY" else "🔴" if signal["signal"] == "SELL" else "🟡"
            st.markdown(f"""
            <div class="strategy-card">
                <strong>{signal['symbol']}</strong> {color} {signal['signal']}<br>
                {signal['type']} • Strength: {signal['strength']}
            </div>
            """, unsafe_allow_html=True)

# === TRADING CHARTS PAGE ===
elif current_page == "charts":
    st.markdown('<h1 class="main-header">📈 Trading Charts & Analysis</h1>', unsafe_allow_html=True)
    
    # Ticker Input
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        ticker = st.text_input("Enter Ticker Symbol", value="AAPL", placeholder="e.g. AAPL, TSLA").upper()
    with col2:
        timeframe = st.selectbox("Timeframe", ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y"])
    with col3:
        chart_type = st.selectbox("Chart Type", ["Candlestick", "Line", "OHLC"])
    
    if ticker:
        try:
            # Download data
            df = yf.download(ticker, period=timeframe, progress=False)
            
            if not df.empty:
                # Technical Indicators
                st.markdown('<div class="section-header">📊 Technical Indicators</div>', unsafe_allow_html=True)
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    current_price = df['Close'].iloc[-1]
                    prev_price = df['Close'].iloc[-2]
                    change = ((current_price - prev_price) / prev_price) * 100
                    st.metric("Current Price", f"${current_price:.2f}", f"{change:+.2f}%")
                
                with col2:
                    ma20 = df['Close'].rolling(20).mean().iloc[-1]
                    st.metric("MA20", f"${ma20:.2f}")
                
                with col3:
                    ma50 = df['Close'].rolling(50).mean().iloc[-1]
                    st.metric("MA50", f"${ma50:.2f}")
                
                with col4:
                    volume = df['Volume'].iloc[-1]
                    st.metric("Volume", f"{volume:,.0f}")
                
                # Chart
                st.markdown('<div class="section-header">📈 Price Chart</div>', unsafe_allow_html=True)
                
                fig = go.Figure()
                
                if chart_type == "Candlestick":
                    fig.add_trace(go.Candlestick(
                        x=df.index,
                        open=df['Open'],
                        high=df['High'],
                        low=df['Low'],
                        close=df['Close'],
                        name=ticker
                    ))
                else:
                    fig.add_trace(go.Scatter(
                        x=df.index,
                        y=df['Close'],
                        mode='lines',
                        name=f'{ticker} Close',
                        line=dict(color='#00ff88', width=2)
                    ))
                
                # Add moving averages
                if len(df) >= 20:
                    fig.add_trace(go.Scatter(
                        x=df.index,
                        y=df['Close'].rolling(20).mean(),
                        mode='lines',
                        name='MA20',
                        line=dict(color='orange', width=1)
                    ))
                
                if len(df) >= 50:
                    fig.add_trace(go.Scatter(
                        x=df.index,
                        y=df['Close'].rolling(50).mean(),
                        mode='lines',
                        name='MA50',
                        line=dict(color='red', width=1)
                    ))
                
                fig.update_layout(
                    title=f"{ticker} - {timeframe.upper()} Chart",
                    xaxis_title="Date",
                    yaxis_title="Price ($)",
                    template="plotly_dark",
                    height=600
                )
                
                st.plotly_chart(fig, use_container_width=True)
                
        except Exception as e:
            st.error(f"Error loading data for {ticker}: {str(e)}")

# === AI ANALYSIS PAGE ===
elif current_page == "ai_analysis":
    st.markdown('<h1 class="main-header">🧠 AI Analysis Center</h1>', unsafe_allow_html=True)
    
    # AI Analysis Input
    ticker = st.text_input("Analyze Ticker", value="AAPL", placeholder="Enter symbol for AI analysis").upper()
    
    if ticker:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="section-header">🤖 AI Pattern Detection</div>', unsafe_allow_html=True)
            
            if st.button("🔍 Run AI Analysis", type="primary"):
                with st.spinner("AI analyzing patterns..."):
                    time.sleep(2)  # Simulate processing
                    
                    # Mock AI results
                    patterns = [
                        {"pattern": "Bullish Flag", "confidence": "87%", "timeframe": "4H"},
                        {"pattern": "Volume Breakout", "confidence": "92%", "timeframe": "1D"},
                        {"pattern": "RSI Divergence", "confidence": "74%", "timeframe": "1H"}
                    ]
                    
                    for pattern in patterns:
                        st.success(f"✅ {pattern['pattern']} - {pattern['confidence']} confidence ({pattern['timeframe']})")
        
        with col2:
            st.markdown('<div class="section-header">📊 Sentiment Analysis</div>', unsafe_allow_html=True)
            
            # Mock sentiment data
            sentiment_score = np.random.randint(60, 95)
            sentiment_color = "🟢" if sentiment_score > 70 else "🟡" if sentiment_score > 50 else "🔴"
            
            st.metric("Overall Sentiment", f"{sentiment_score}%", f"{sentiment_color}")
            
            # Sentiment breakdown
            st.markdown("**Sentiment Sources:**")
            sources = [
                {"source": "News Headlines", "score": "82%", "trend": "↗️"},
                {"source": "Social Media", "score": "76%", "trend": "↗️"},
                {"source": "Options Flow", "score": "68%", "trend": "↘️"},
                {"source": "Insider Trading", "score": "91%", "trend": "↗️"}
            ]
            
            for source in sources:
                st.markdown(f"• {source['source']}: {source['score']} {source['trend']}")
    
    # AI Insights Panel
    st.markdown("---")
    st.markdown('<div class="section-header">💡 AI Market Insights</div>', unsafe_allow_html=True)
    
    insights = [
        "🔥 High volatility expected in tech sector this week",
        "📈 Bullish momentum building in energy stocks",
        "⚠️ Watch for potential reversal in growth stocks",
        "💰 Options activity suggests upcoming catalyst events"
    ]
    
    for insight in insights:
        st.info(insight)

# === STRATEGY LAB PAGE ===
elif current_page == "strategies":
    st.markdown('<h1 class="main-header">⚡ Strategy Lab</h1>', unsafe_allow_html=True)
    
    st.info("🚀 Strategy Lab - Connect your existing strategy modules here!")
    
    # Mock strategy performance
    performance_data = {
        "Strategy": ["Momentum", "Mean Reversion", "Breakout Hunter", "AI Sentiment"],
        "Win Rate": ["78%", "65%", "82%", "71%"],
        "Avg Return": ["4.2%", "2.8%", "6.1%", "3.9%"],
        "Max Drawdown": ["-8.5%", "-5.2%", "-12.1%", "-6.8%"],
        "Sharpe Ratio": ["1.85", "1.42", "2.01", "1.67"]
    }
    
    df_performance = pd.DataFrame(performance_data)
    st.dataframe(df_performance, use_container_width=True)
    
    # Performance Chart
    fig = go.Figure()
    
    # Mock cumulative returns
    dates = pd.date_range(start='2024-01-01', end='2024-12-01', freq='D')
    returns = np.cumsum(np.random.normal(0.001, 0.02, len(dates))) * 100
    
    fig.add_trace(go.Scatter(
        x=dates,
        y=returns,
        mode='lines',
        name='Portfolio Performance',
        line=dict(color='#00ff88', width=2)
    ))
    
    fig.update_layout(
        title="Strategy Portfolio Performance",
        xaxis_title="Date",
        yaxis_title="Cumulative Return (%)",
        template="plotly_dark",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

# === EDUCATION CENTER PAGE ===
elif current_page == "education":
    st.markdown('<h1 class="main-header">📚 Education Center</h1>', unsafe_allow_html=True)
    
    # Education Categories
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="section-header">📖 Learning Modules</div>', unsafe_allow_html=True)
        
        modules = [
            "🔰 Trading Basics",
            "📊 Technical Analysis", 
            "🧠 AI Trading Strategies",
            "💰 Risk Management",
            "📈 Options Trading",
            "🎯 Psychology of Trading"
        ]
        
        selected_module = st.selectbox("Choose Module", modules)
    
    with col2:
        st.markdown(f'<div class="section-header">{selected_module}</div>', unsafe_allow_html=True)
        
        if "Trading Basics" in selected_module:
            st.markdown("""
            ### Welcome to Trading Fundamentals
            
            **Key Concepts:**
            - **Bull Market**: Rising prices and optimistic sentiment
            - **Bear Market**: Falling prices and pessimistic sentiment  
            - **Support**: Price level where buying interest emerges
            - **Resistance**: Price level where selling pressure increases
            
            **Essential Terms:**
            - **Bid**: Highest price buyers are willing to pay
            - **Ask**: Lowest price sellers are willing to accept
            - **Spread**: Difference between bid and ask prices
            - **Volume**: Number of shares traded
            """)
            
        elif "Technical Analysis" in selected_module:
            st.markdown("""
            ### Technical Analysis Fundamentals
            
            **Moving Averages:**
            - Simple Moving Average (SMA): Average price over N periods
            - Exponential Moving Average (EMA): Gives more weight to recent prices
            
            **Momentum Indicators:**
            - RSI (Relative Strength Index): Measures overbought/oversold conditions
            - MACD: Shows relationship between two moving averages
            
            **Chart Patterns:**
            - Head and Shoulders: Reversal pattern
            - Double Top/Bottom: Reversal patterns
            - Triangles: Continuation patterns
            """)
            
        elif "AI Trading" in selected_module:
            st.markdown("""
            ### AI-Powered Trading Strategies
            
            **Machine Learning Applications:**
            - Pattern Recognition: Identifying complex chart patterns
            - Sentiment Analysis: Processing news and social media
            - Predictive Modeling: Forecasting price movements
            
            **AI Advantages:**
            - Process vast amounts of data quickly
            - Identify subtle patterns humans might miss
            - Remove emotional bias from decisions
            - Operate 24/7 without fatigue
            """)
    
    # Interactive Quiz Section
    st.markdown("---")
    st.markdown('<div class="section-header">🎯 Knowledge Check</div>', unsafe_allow_html=True)
    
    quiz_question = st.selectbox(
        "Test your knowledge:",
        [
            "What does RSI measure?",
            "What is a bull market?", 
            "What is the difference between bid and ask?",
            "What is a moving average?"
        ]
    )
    
    if st.button("Submit Answer"):
        st.success("✅ Correct! Great job learning.")
        st.balloons()

# === NEWS & SENTIMENT PAGE ===
elif current_page == "news":
    st.markdown('<h1 class="main-header">📰 News & Market Sentiment</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">📰 Latest Market News</div>', unsafe_allow_html=True)
        
        # Mock news data
        news_items = [
            {
                "headline": "Fed Signals Potential Rate Cut in Q2 2024",
                "sentiment": "Bullish",
                "time": "2 hours ago",
                "source": "Reuters"
            },
            {
                "headline": "Tech Stocks Rally on AI Breakthrough",
                "sentiment": "Bullish", 
                "time": "4 hours ago",
                "source": "Bloomberg"
            },
            {
                "headline": "Energy Sector Faces Headwinds",
                "sentiment": "Bearish",
                "time": "6 hours ago",
                "source": "CNBC"
            },
            {
                "headline": "Crypto Market Shows Signs of Recovery",
                "sentiment": "Neutral",
                "time": "8 hours ago",
                "source": "CoinDesk"
            }
        ]
        
        for news in news_items:
            sentiment_color = "🟢" if news["sentiment"] == "Bullish" else "🔴" if news["sentiment"] == "Bearish" else "🟡"
            
            st.markdown(f"""
            <div class="strategy-card">
                <strong>{news['headline']}</strong><br>
                {sentiment_color} {news['sentiment']} • {news['time']} • {news['source']}
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-header">📊 Sentiment Dashboard</div>', unsafe_allow_html=True)
        
        # Sentiment metrics
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Market Sentiment", "Bullish", "↗️ +5%")
        with col_b:
            st.metric("Fear & Greed Index", "72", "↗️ +8")
        
        # Sentiment chart
        fig = go.Figure()
        
        dates = pd.date_range(start='2024-11-01', end='2024-12-01', freq='D')
        sentiment_scores = 50 + np.cumsum(np.random.normal(0, 5, len(dates)))
        
        fig.add_trace(go.Scatter(
            x=dates,
            y=sentiment_scores,
            mode='lines+markers',
            name='Sentiment Score',
            line=dict(color='#ff6b6b', width=2)
        ))
        
        fig.add_hline(y=50, line_dash="dash", line_color="gray", annotation_text="Neutral")
        fig.add_hline(y=70, line_dash="dash", line_color="green", annotation_text="Bullish")
        fig.add_hline(y=30, line_dash="dash", line_color="red", annotation_text="Bearish")
        
        fig.update_layout(
            title="Market Sentiment Trend",
            xaxis_title="Date",
            yaxis_title="Sentiment Score",
            template="plotly_dark",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

# === EXECUTION CENTER PAGE ===
elif current_page == "execution":
    st.markdown('<h1 class="main-header">🎯 Execution Center</h1>', unsafe_allow_html=True)
    
    # Order Entry Panel
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="section-header">📝 Order Entry</div>', unsafe_allow_html=True)
        
        with st.form("order_form"):
            symbol = st.text_input("Symbol", value="AAPL")
            action = st.selectbox("Action", ["BUY", "SELL"])
            quantity = st.number_input("Quantity", min_value=1, value=100)
            order_type = st.selectbox("Order Type", ["Market", "Limit", "Stop"])
            
            if order_type == "Limit":
                limit_price = st.number_input("Limit Price", value=150.00, step=0.01)
            
            submitted = st.form_submit_button("🚀 Submit Order")
            
            if submitted:
                st.success(f"✅ {action} order for {quantity} shares of {symbol} submitted!")
    
    with col2:
        st.markdown('<div class="section-header">📊 Portfolio Positions</div>', unsafe_allow_html=True)
        
        # Mock portfolio data
        positions = {
            "Symbol": ["AAPL", "TSLA", "NVDA", "MSFT"],
            "Shares": [100, 50, 25, 75],
            "Avg Cost": ["$145.50", "$210.25", "$420.80", "$285.90"],
            "Current Price": ["$150.25", "$205.10", "$445.60", "$295.40"],
            "P&L": ["+$475", "-$257", "+$620", "+$712"],
            "P&L %": ["+3.3%", "-2.4%", "+5.9%", "+3.3%"]
        }
        
        df_positions = pd.DataFrame(positions)
        st.dataframe(df_positions, use_container_width=True)
    
    # Recent Orders
    st.markdown("---")
    st.markdown('<div class="section-header">📋 Recent Orders</div>', unsafe_allow_html=True)
    
    orders = {
        "Time": ["09:30:15", "10:45:22", "11:20:08", "14:15:33"],
        "Symbol": ["AAPL", "TSLA", "NVDA", "SPY"],
        "Action": ["BUY", "SELL", "BUY", "BUY"],
        "Quantity": [100, 25, 10, 200],
        "Price": ["$150.25", "$205.10", "$445.60", "$421.17"],
        "Status": ["✅ Filled", "✅ Filled", "🟡 Partial", "✅ Filled"]
    }
    
    df_orders = pd.DataFrame(orders)
    st.dataframe(df_orders, use_container_width=True)

# === SETTINGS PAGE ===
elif current_page == "settings":
    st.markdown('<h1 class="main-header">⚙️ Settings & Configuration</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">🎨 Display Settings</div>', unsafe_allow_html=True)
        
        theme = st.selectbox("Theme", ["Dark", "Light", "Auto"])
        chart_style = st.selectbox("Chart Style", ["Candlestick", "Line", "OHLC"])
        refresh_rate = st.slider("Refresh Rate (seconds)", 1, 60, 5)
        
        st.markdown('<div class="section-header">🔔 Notifications</div>', unsafe_allow_html=True)
        
        email_alerts = st.checkbox("Email Alerts", value=True)
        push_notifications = st.checkbox("Push Notifications", value=True)
        sound_alerts = st.checkbox("Sound Alerts", value=False)
    
    with col2:
        st.markdown('<div class="section-header">🎯 Trading Settings</div>', unsafe_allow_html=True)
        
        default_quantity = st.number_input("Default Order Quantity", value=100)
        risk_limit = st.slider("Risk Limit (%)", 1, 10, 2)
        auto_stop_loss = st.checkbox("Auto Stop Loss", value=True)
        
        if auto_stop_loss:
            stop_loss_pct = st.slider("Stop Loss %", 1, 20, 5)
        
        st.markdown('<div class="section-header">🔐 API Settings</div>', unsafe_allow_html=True)
        
        api_key = st.text_input("API Key", type="password", placeholder="Enter your API key")
        api_secret = st.text_input("API Secret", type="password", placeholder="Enter your API secret")
    
    # Save Settings Button
    if st.button("💾 Save Settings", type="primary"):
        st.success("✅ Settings saved successfully!")

# === Footer ===
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    🚀 CamboStationVision™ | Advanced Trading Platform | Version 2.0
</div>
""", unsafe_allow_html=True)