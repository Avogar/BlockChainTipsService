// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 */

struct Employee {
    /// Employee address that will be used for sending personal tips
    address addr;
    /// Employee reviews
    string[] reviews;
}

 struct Organization {
    /// Organization address that will be used for sending tips to organization
    address addr;
    /// Employer id -> employer info
    mapping (string => Employee) employees;
    /// Reviews of the organization
    string[] reviews;
 }

 struct EmployeeInfo {
     string id;
     address addr;
 }

contract TipsService {

    mapping (string => Organization) organizations;

    function addOrganization(string memory organization_id, EmployeeInfo[] memory employee_infos) public {
        for (uint i = 0; i < employee_infos.length; i++) {
            EmployeeInfo memory info = employee_infos[i];
            Employee memory new_employee;
            new_employee.addr = info.addr;
            organizations[organization_id].employees[info.id] = new_employee;
        }
    }

    function removeOrganization(string memory organization_id) public {
        delete organizations[organization_id];
    }

    function addEmployeeToOrganization(string memory organization_id, EmployeeInfo memory employee_info) public {
        Employee memory new_employee;
        new_employee.addr = employee_info.addr;
        organizations[organization_id].employees[employee_info.id] = new_employee;
    }

    function removeEmployeeFromOrganization(string memory organization_id, string memory employee_id) public {
        delete organizations[organization_id].employees[employee_id];
    }

    function sendTipsToEmployee(string memory organization_id, string memory employee_id, string memory review) public payable {
        Organization storage org = organizations[organization_id];
        Employee storage employee = org.employees[employee_id];
        (bool sent, bytes memory data) = employee.addr.call{value: msg.value}("");
        require(sent, "Failed to send Ether");
        bytes memory tmp = bytes(review);
        if (tmp.length != 0) {
            employee.reviews.push(review);
        }
    }

    function sendTipsToOrganization(string memory organization_id, string memory review) public payable {
        Organization storage org = organizations[organization_id];
        (bool sent, bytes memory data) = org.addr.call{value: msg.value}("");
        require(sent, "Failed to send Ether");
        bytes memory tmp = bytes(review);
        if (tmp.length != 0) {
            org.reviews.push(review);
        }
    }

    function sendOrganizationReview(string memory organization_id, string memory review) public {
        organizations[organization_id].reviews.push(review);
    }

    function sendEmployeeReview(string memory organization_id, string memory employee_id, string memory review) public {
        organizations[organization_id].employees[employee_id].reviews.push(review);
    }

    function getOrganizationReviews(string memory organization_id) public view returns (string[] memory reviews) {
        return organizations[organization_id].reviews;
    }

    function getEmployeeReviews(string memory organization_id, string memory employee_id) public view returns (string[] memory reviews) {
        return organizations[organization_id].employees[employee_id].reviews;
    }

    function getAllorganizations() public view returns (string[] memory rganizations_list) {
        /// TODO: implement itarable mapping
        string[] memory res;
        return res;
    }

    function getAllEmployeeInOrganization(string memory organization_id) public view returns (string[] memory employees) {
        /// TODO: implement itarable mapping
        string[] memory res;
        return res;
    }
}
