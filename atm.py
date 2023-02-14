from sql_query import Sql_Atm


class ATM:

    def atm_logic(self):
        Sql_Atm.create_table()
        # Sql_Atm.insert_users((1234, 1111, 10000))
        # Sql_Atm.insert_users((2345, 2222, 10000))
        number_card = input("Введите пожалуйста номер карты: ")

        while True:
            if Sql_Atm.input_card(number_card):

                if Sql_Atm.input_code(number_card):

                    # Sql_Atm.info_balance(number_card)
                    # Sql_Atm.withdraw_money(number_card)
                    # Sql_Atm.deposition_money(number_card)
                    Sql_Atm.input_operation(number_card)
                    break

                else:
                    break
            else:
                break


start = ATM()
start.atm_logic()
