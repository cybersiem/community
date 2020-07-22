#   Copyright (C) 2020 CyberSIEM(R)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from abc import ABC
from abc import abstractmethod


class Keyring(ABC):

    @abstractmethod
    def set_password(self, service: str, key: str, value: str):
        pass

    @abstractmethod
    def get_password(self, service: str, key: str) -> str:
        pass

    @abstractmethod
    def delete_password(self, service: str, key: str):
        pass


class Ldap(ABC):

    def connect(self):
        pass

    def disconnect(self):
        pass

    def search(self):
        pass

    def entries(self):
        pass
