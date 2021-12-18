// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract IPFSContract {

  // Data Structure untuk Manufacture
  struct ModuleManufacturer{
    string sid;
    string system_information;
    string system_create;
    string mid;
    string manufacture_id;
    string manufacture_date;
    string filename;
    string ipfs_file_cid;
  }

  ModuleManufacturer[] public data_manufacturers;

  // function to add data Manufacture
  function addDataManufacturer(
    string memory _sid,
    string memory _system_information,
    string memory _system_create,
    string memory _mid,
    string memory _manufacture_id,
    string memory _manufacture_date,
    string memory _filename,
    string memory _ipfs_file_cid
  ) public {
    data_manufacturers.push(
      ModuleManufacturer({
        sid: _sid,
        system_information: _system_information,
        system_create: _system_create,
        mid: _mid,
        manufacture_id: _manufacture_id,
        manufacture_date: _manufacture_date,
        filename: _filename,
        ipfs_file_cid: _ipfs_file_cid
      })
    );
  }

  function getJumlahData() view public returns (uint) {
    return data_manufacturers.length;
  }

  constructor() public {
    addDataManufacturer("SM_1.0", "brake_System", "Friday.17-12=2021", "Mbs_1.1.0", "MM1", "Friday.17-12-2021", "lm555.pdf", "QmbXe2mZchuJT3QwX7WDk7uR7Tp5JMnvBc5vLJTP4Vx5fN");
    addDataManufacturer("SM_1.0", "brake_System", "Friday.17-12=2021", "Mbs_1.1.0", "MM1", "Friday.17-12-2021", "7402.pdf", "QmYNaENxb2s3GCXX6EkpuY3NkVkkKmn5Xk13zQAEk5767Y");
  }
}

