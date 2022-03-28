import pyupbit

access = "EKtKOnKwq3s4DHgp3IZI8Iq0pgWcXf2PssPqfZOx"          # 본인 값으로 변경
secret = "fsoaVhnE4ociv5CaU5TrNqNeZZJNyP4hWqyU1XIt"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회