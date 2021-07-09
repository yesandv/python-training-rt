class TicketOffice:
    def __init__(self):
        self._tickets_pricing = {}
        self._proceeds = []

    def get_tickets_pricing(self, list_of_categories_and_fees):
        for i in range(0, len(list_of_categories_and_fees) - 1, 2):
            self._tickets_pricing[list_of_categories_and_fees[i]] = list_of_categories_and_fees[i+1]
        return self._tickets_pricing

    def calculate_total_amount_by_group(self, list_of_categories_and_num_of_people):
        total_amount = 0
        for i in range(0, len(list_of_categories_and_num_of_people) - 1, 2):
            if list_of_categories_and_num_of_people[i] in self._tickets_pricing.keys():
                total_amount += self._tickets_pricing.get(list_of_categories_and_num_of_people[i]) * list_of_categories_and_num_of_people[i+1]
        self._proceeds.append(total_amount)
        return total_amount

    def calculate_proceeds(self):
        return sum(self._proceeds)


if __name__ == "__main__":
    office = TicketOffice()

    list_of_categories_and_fees = []
    num_of_categories = int(input('Укажите кол-во категорий посетителей: '))
    for ctgr in range(num_of_categories):
        category = input('Задайте категорию посетителей: ')
        list_of_categories_and_fees.append(category)
        fee = int(input('Задайте стоимость билета для этой категории: '))
        list_of_categories_and_fees.append(fee)

    office.get_tickets_pricing(list_of_categories_and_fees)

    num_of_groups = int(input('Укажите, сколько групп обслужили за день: '))
    for grp in range(num_of_groups):
        list_of_categories_and_num_of_people = []

        num_of_categories = int(input(f'Сколько категорий посетителей в группе {group+1}? '))

        for ctg in range(num_of_categories):
            category = input('Укажите категорию посетителей: ')
            list_of_categories_and_num_of_people.append(category)
            num_of_people = int(input('Сколько человек в этой категории? '))
            list_of_categories_and_num_of_people.append(num_of_people)

        print(office.calculate_total_amount_by_group(list_of_categories_and_num_of_people))

    print(office.calculate_proceeds())
