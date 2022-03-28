import pyupbit
import numpy as np

#OHLCV(open, high, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC", count=7)
df['range'] = (df['high'] - df['low']) * 0.5 # 변동폭*k 계산 -> (고가-저가)*k값
df['target'] = df['open'] + df['range'].shift(1) #target(매수가) -> range 컬럼을 한 칸씩 밑으로 내림(.shift(1))

# ror(수익률) -> np.where(조건문, 참일 때 값 & 거짓일 때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

df['hpr'] = df['ror'].cumprod() #누적 곱 계산(comprod) => 누적 수익률
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100 #Draw Dwon 계산 (누적 최대값과 현재 hpr 차이 / 누적 최대값 * 100)
print("MDD(%): ", df['dd'].max()) # MDD 계산
df.to_excel("result.xlsx") # 엑셀로 출력