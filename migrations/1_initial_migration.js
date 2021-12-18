const Migrations = artifacts.require("Migrations");
const IPFSContract = artifacts.require("IPFSContract");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(IPFSContract);
};
