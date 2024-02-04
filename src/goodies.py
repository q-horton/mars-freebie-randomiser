import json
import random


class Goodies():

	def __init__(self, file: str):
		self.file = file
		self.file_save = self.save_file_from_file(file)
		self.create_from_file(file)
		print(f"{len(self.data)} varieties of freebies read in.")

	def save_file_from_file(self, file: str):
		file_parts = file.split(".")
		file_parts.insert(len(file_parts)-1, "_saved")
		return ".".join(file_parts)

	def create_from_file(self, file: str):
		self.file = file
		self.save_file = self.save_file_from_file(file)
		with open(file, 'r') as f:
			self.data = json.load(f)
	
	def get_remaining_breakdown(self):
		result = [0]
		for i in self.data:
			result.append(result[-1] + i["amount"])
		return result

	def get_random_item(self) -> int:
		breakdown = self.get_remaining_breakdown()
		choice = random.randint(1, breakdown[-1])
		for i in range(1, len(breakdown)):
			if breakdown[i-1] < choice <= breakdown[i]:
				return i-1

	def update_stored(self):
		with open(self.save_file, 'w') as f:
			json.dump(self.data, f, indent=4)

	def draw_goodie(self) -> (str, str):
		item_index = self.get_random_item()
		self.data[item_index]["amount"] -= 1
		self.update_stored()
		print(f"Drew one {self.data[item_index]['name']}, {self.data[item_index]['amount']} remain.")
		return (self.data[item_index]["name"], self.data[item_index]["background"])
