from hash_table import HashTable

def main():
	# Тестуємо нашу хеш-таблицю:
	H = HashTable(5)
	H.insert("apple", 10)
	H.insert("orange", 20)
	H.insert("banana", 30)
	H.insert("kiwi", 40)

	print(H.get("apple"))   # Виведе: 10
	print(H.get("orange"))  # Виведе: 20
	print(H.get("banana"))  # Виведе: 30
	print(H.get("kiwi"))    # Виведе: 40
      
	H.delete("apple", 10)
	H.delete("kiwi", 40)
      
	print(H.table)

if __name__ == "__main__":
    main()