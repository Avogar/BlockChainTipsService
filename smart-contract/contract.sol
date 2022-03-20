// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.10;


struct Employee {
    /// Employee address that will be used for sending personal tips
    address addr;
    /// Employee reviews
    string[] reviews;
}

library IterableMapEmployees {
    // Iterable mapping from address to uint;
    struct Map {
        string[] keys;
        mapping(string => Employee) values;
        mapping(string => uint) indexOf;
        mapping(string => bool) inserted;
    }

    function get(Map storage map, string memory key) public view returns (Employee storage) {
        return map.values[key];
    }

    function getKeyAtIndex(Map storage map, uint index) public view returns (string storage) {
        return map.keys[index];
    }

    function size(Map storage map) public view returns (uint) {
        return map.keys.length;
    }

    function add(Map storage map, string memory key) public {
        if (map.inserted[key]) {
            return;
        }

        map.inserted[key] = true;
        map.indexOf[key] = map.keys.length;
        map.keys.push(key);
    }

    function remove(Map storage map, string memory key) public {
        if (!map.inserted[key]) {
            return;
        }

        delete map.inserted[key];
        delete map.values[key];

        uint index = map.indexOf[key];
        uint lastIndex = map.keys.length - 1;
        string storage lastKey = map.keys[lastIndex];

        map.indexOf[lastKey] = index;
        delete map.indexOf[key];

        map.keys[index] = lastKey;
        map.keys.pop();
    }

    function contains(Map storage map, string memory key) public view returns (bool) {
        return map.inserted[key];
    }

    function getKeys(Map storage map) public view returns (string[] storage) {
        return map.keys;
    }
}

 struct Organization {
    /// Organization address that will be used for sending tips to organization
    address addr;
    /// Employer id -> employer info
    IterableMapEmployees.Map employees;
    /// Reviews of the organization
    string[] reviews;
 }

library IterableMapOrganizations {
    // Iterable mapping from address to uint;
    struct Map {
        string[] keys;
        mapping(string => Organization) values;
        mapping(string => uint) indexOf;
        mapping(string => bool) inserted;
    }

    function get(Map storage map, string memory key) public view returns (Organization storage) {
        return map.values[key];
    }

    function getKeyAtIndex(Map storage map, uint index) public view returns (string storage) {
        return map.keys[index];
    }

    function size(Map storage map) public view returns (uint) {
        return map.keys.length;
    }

    function add(Map storage map, string memory key) public {
        if (map.inserted[key]) {
            return;
        }

        map.inserted[key] = true;
        map.indexOf[key] = map.keys.length;
        map.keys.push(key);
    }

    function remove(Map storage map, string memory key) public {
        if (!map.inserted[key]) {
            return;
        }

        delete map.inserted[key];
        delete map.values[key];

        uint index = map.indexOf[key];
        uint lastIndex = map.keys.length - 1;
        string storage lastKey = map.keys[lastIndex];

        map.indexOf[lastKey] = index;
        delete map.indexOf[key];

        map.keys[index] = lastKey;
        map.keys.pop();
    }

    function contains(Map storage map, string memory key) public view returns (bool) {
        return map.inserted[key];
    }

    function getKeys(Map storage map) public view returns (string[] storage) {
        return map.keys;
    }
}

library IterableMapActions {
    // Iterable mapping from address to uint;
    struct Map {
        string[] keys;
        mapping(string => uint) values;
        mapping(string => uint) indexOf;
        mapping(string => bool) inserted;
    }

    function get(Map storage map, string memory key) public view returns (uint) {
        return map.values[key];
    }

    function getKeyAtIndex(Map storage map, uint index) public view returns (string storage) {
        return map.keys[index];
    }

    function size(Map storage map) public view returns (uint) {
        return map.keys.length;
    }

    function set(Map storage map, string memory key, uint val) public {
        if (map.inserted[key]) {
            return;
        }

        map.inserted[key] = true;
        map.indexOf[key] = map.keys.length;
        map.keys.push(key);
        map.values[key] = val;
    }

    function remove(Map storage map, string memory key) public {
        if (!map.inserted[key]) {
            return;
        }

        delete map.inserted[key];
        delete map.values[key];

        uint index = map.indexOf[key];
        uint lastIndex = map.keys.length - 1;
        string storage lastKey = map.keys[lastIndex];

        map.indexOf[lastKey] = index;
        delete map.indexOf[key];

        map.keys[index] = lastKey;
        map.keys.pop();
    }

    function contains(Map storage map, string memory key) public view returns (bool) {
        return map.inserted[key];
    }

    function getKeys(Map storage map) public view returns (string[] storage) {
        return map.keys;
    }
}

struct Info {
     string id;
     address addr;
 }

contract TipsService {
    using IterableMapOrganizations for IterableMapOrganizations.Map;
    using IterableMapEmployees for IterableMapEmployees.Map;
    using IterableMapActions for IterableMapActions.Map;

    IterableMapOrganizations.Map organizations;
    IterableMapActions.Map actions;
    string[] keys_to_remove;

    function addOrganization(Info memory org_info, Info[] memory employee_infos) public {
        organizations.add(org_info.id);
        Organization storage org = organizations.get(org_info.id);
        org.addr = org_info.addr;
        for (uint i = 0; i < employee_infos.length; i++) {
            Info memory info = employee_infos[i];
            org.employees.add(info.id);
            Employee storage employee = org.employees.get(info.id);
            employee.addr = info.addr;
        }
    }

    function removeOrganization(string memory organization_id) public {
        organizations.remove(organization_id);
    }

    function addEmployeeToOrganization(string memory organization_id, Info memory employee_info) public {
        organizations.get(organization_id).employees.add(employee_info.id);
        organizations.get(organization_id).employees.get(employee_info.id).addr = employee_info.addr;
    }

    function removeEmployeeFromOrganization(string memory organization_id, string memory employee_id) public {
        organizations.get(organization_id).employees.remove(employee_id);
    }

    function sendTipsToEmployee(string memory organization_id, string memory employee_id, string memory review, string memory action_id) public payable {
        require(checkAction(action_id), "Action denied");

        Organization storage org = organizations.get(organization_id);
        Employee storage employee = org.employees.get(employee_id);
        (bool sent, bytes memory data) = employee.addr.call{value: msg.value}("");
        require(sent, "Failed to send Ether");
        bytes memory tmp = bytes(review);
        if (tmp.length != 0) {
            employee.reviews.push(review);
        }
    }

    function sendTipsToOrganization(string memory organization_id, string memory review, string memory action_id) public payable {
        require(checkAction(action_id), "Action denied");
        Organization storage org = organizations.get(organization_id);
        (bool sent, bytes memory data) = org.addr.call{value: msg.value}("");
        require(sent, "Failed to send Ether");
        bytes memory tmp = bytes(review);
        if (tmp.length != 0) {
            org.reviews.push(review);
        }
    }

    function sendOrganizationReview(string memory organization_id, string memory review, string memory action_id) public {
        require(checkAction(action_id), "Action denied");
        organizations.get(organization_id).reviews.push(review);
    }

    function sendEmployeeReview(string memory organization_id, string memory employee_id, string memory review, string memory action_id) public {
        require(checkAction(action_id), "Action denied");
        organizations.get(organization_id).employees.get(employee_id).reviews.push(review);
    }

    function getOrganizationReviews(string memory organization_id) public view returns (string[] memory reviews) {
        return organizations.get(organization_id).reviews;
    }

    function getEmployeeReviews(string memory organization_id, string memory employee_id) public view returns (string[] memory reviews) {
        return organizations.get(organization_id).employees.get(employee_id).reviews;
    }

    function getAllOrganizations() public view returns (string[] memory) {
        return organizations.getKeys();
    }

    function getAllEmployeeInOrganization(string memory organization_id) public view returns (string[] memory) {
        return organizations.get(organization_id).employees.getKeys();
    }

    function checkAction(string memory action_id) private returns (bool) {
        string[] storage keys = actions.getKeys();
        uint now_time = block.timestamp;
        for (uint i = 0; i != keys.length; i++) {
            if (now_time - actions.get(keys[i]) > 24 * 3600) {
                keys_to_remove.push(keys[i]);
            }
        }
        for (uint i = 0; i != keys_to_remove.length; i++) {
            actions.remove(keys_to_remove[i]);
        }
        delete keys_to_remove;

        if (actions.contains(action_id)) {
            return false;
        }

        actions.set(action_id, now_time);
        return true;
    }
}
