#Ciclos for (com listas)

print('Regimes políticos:')
political_regimes = ['democracia', 'república', 'monarquia', 'tirania']
portuguese_regime = 'democracia'
for regime in political_regimes:
    print(regime, end='-> ')
print('FIM')

print('Regime português:')
for regime in political_regimes:
    if regime == portuguese_regime:
        print(regime)
