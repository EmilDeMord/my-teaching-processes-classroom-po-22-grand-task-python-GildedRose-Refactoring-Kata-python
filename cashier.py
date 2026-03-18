class Cashier:
    def __init__(self):
        self.coins = [50, 25, 10, 5, 1] 

    def calculate_change(self, amount_paid, item_price):
        change = amount_paid - item_price
        change_coins = []
        
        for coin in self.coins:
            while change >= coin:
                change -= coin
                change_coins.append(coin)
        
        return change_coins

    
    def budget_options(self, budget, current_items):
        all_possible_combinations = []
        for i in range(1, len(current_items) + 1):
            for combo in combinations(current_items, i):
                total_price = sum(item[1] for item in combo)
                if total_price <= budget:
                    all_possible_combinations.append((combo, total_price))

        for combo, price in all_possible_combinations:
            names = [current_items[0] for item in combo]
            print(f"Набор{','.join(names)}, Итог{price}")