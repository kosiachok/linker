import requests

# клиентский интерфейс
class ClientInterface():
    # Список скрытых атрибутов класса:
    # classroom                  —    аудитория
    # package_list               —    список пакетов из реестра предметов
    # timetable_dict             —    расписание занятий из реестра предметов
    # package_names              —    список названий пакетов из скраппера
    # installed_packages_status  —    установка завершена/не завершена
    pass


# класс запроса в реестр предметов
class RegisterDataGetter():

    # получение списка пакетов из реестра предметов
    def packagelist_getter(self):
        return ['package1', 'package2', 'package3']

    # получение расписания из реестра предметов
    def timetable_getter(self):
        return {'day': {'time': 'subject/package'}}


# адаптер класса запроса в реестр предметов
class RegisterDataAdapter(ClientInterface, RegisterDataGetter):

    def get_packagelist(self):
        return self.packagelist_getter()

    def get_timetable(self):
        return self.timetable_getter()


# класс запроса на установку и удаление пакетов
class PackageInstaller():

    def install(self):
        return True

    def uninstall(self):
        return True


# класс пакетного менеджера
class PackageManager():

    # получение списка названий пакетов из скраппера
    def get_names_via_scrapper(self):
        return ['package1_name', 'package2_name', 'package3_name']

    # контроль установленных пакетов
    def installing_packages(self):
        return True


# класс адаптера пакетного менеджера
class PackageManagerAdapter(ClientInterface, PackageManager):

    def get_packagenames(self):
        return True

    def installed_packages_status(self):
        return True


# клиентский код
def client_code(register_data_adapter_obj, package_manager_adapter_obj: ClientInterface):
    ClientInterface.package_list = register_data_adapter_obj.get_packagelist()
    ClientInterface.timetable_dict = register_data_adapter_obj.get_timetable()
    ClientInterface.package_names = package_manager_adapter_obj.get_packagenames()
    ClientInterface.installed_packages_status = package_manager_adapter_obj.installed_packages_status()
    return ClientInterface.installed_packages_status


if __name__ == "__main__":
    register_data_adapter_obj = RegisterDataAdapter()
    package_manager_adapter_obj = PackageManagerAdapter()
    print(client_code(register_data_adapter_obj, package_manager_adapter_obj))
